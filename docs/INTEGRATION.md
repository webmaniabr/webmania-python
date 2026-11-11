# Detalhes técnicos de integração

Este documento reúne os detalhes técnicos do SDK para Python que complementam o [README](../README.md): autenticação, URL base, limites de transporte, arquivos, relatórios e o tratamento do resultado fiscal. O texto é o mesmo que estava no README até esta versão.

## Escopo e disponibilidade

Integração de **Emissor Fiscal e Monitor Fiscal** em aplicações de servidor. O Emissor abrange NF-e/NFC-e na API1 e NFS-e, CT-e/CT-e OS, MDF-e, NFCom e DC-e na API2, com arquivos, eventos e as três operações gerenciais B2B públicas da API1. O Monitor mantém apenas as famílias de documentos e capacidades do seu contrato documentado.

Disponível no repositório público [github.com/webmaniabr/webmania-python](https://github.com/webmaniabr/webmania-python), com instalação a partir do clone (veja a seção Instalação). Ainda não há publicação em registro de pacotes; os nomes e versões abaixo identificam os pacotes gerados a partir desta fonte. Regras do provedor, aceitação fiscal real e plataformas adicionais permanecem com limitações explícitas.

## Visão geral para desenvolvedores

| Item | Detalhe |
|---|---|
| Status | Disponível no GitHub: versão `0.1.0a8` (distribuição `webmania-sdk`, pacote `webmania`), instalada a partir do clone do repositório; ainda sem publicação no PyPI |
| Runtime | CPython >= 3.11 (classificadores 3.11 a 3.14); dependência `jsonschema[format-nongpl]` |
| Clientes | `NfeClient` (NF-e/NFC-e API 1.0), `EmitterClient` (emissor API 2.0), `NfeFilesClient` e `EmitterFilesClient` (arquivos), `ReportFilesClient` (relatórios atuais), `MonitorClient` (Monitor Fiscal), `ResellerClient` (gerencial B2B API 1.0) |
| Cobertura | 102 operações habilitadas de 103 do contrato fixado; `nfeDownloadIbsCbsEventXml` não está disponível nesta versão do SDK |
| Erros | `WebmaniaError`, com `kind`, `status` e `outcome` |
| Contrato | OpenAPI de [webmania-openapi](https://github.com/webmaniabr/webmania-openapi) fixado em [contracts.lock.json](../contracts.lock.json) pelo `contract_digest` e pelo SHA-256 de cada módulo |

### Autenticação

- **NF-e/NFC-e (API 1.0)** — `NfeClient(CompanyCredentials(...))` envia os quatro cabeçalhos `X-Consumer-Key`, `X-Consumer-Secret`, `X-Access-Token` e `X-Access-Token-Secret`. `ResellerClient` usa os mesmos cabeçalhos com `ResellerCredentials`, que não substituem as credenciais da empresa.
- **API 2.0** — `EmitterClient(issuer_token)` e `MonitorClient(monitor_token)` enviam `Authorization: Bearer <token>`. O token do emissor e o do Monitor são credenciais distintas.

Leia as credenciais de variáveis de ambiente ou de um cofre de segredos, como no exemplo abaixo (`WEBMANIA_CONSUMER_KEY`, `WEBMANIA_CONSUMER_SECRET`, `WEBMANIA_ACCESS_TOKEN`, `WEBMANIA_ACCESS_TOKEN_SECRET`).

## Requisitos

Cliente síncrono CPython 3.11–3.14. O ciclo de processos e transporte é testado em Linux/Docker; não há cliente assíncrono nem testes desta versão em outras plataformas.

## Instalação

Clone o repositório público, gere o wheel a partir do clone e instale-o:

```sh
git clone https://github.com/webmaniabr/webmania-python.git
python -m pip install build
python -m build --outdir dist webmania-python
python -m pip install --constraint webmania-python/requirements-runtime.lock dist/webmania_sdk-0.1.0a8-py3-none-any.whl
```

O wheel já contém modelos, schemas e runtime. Resolva as dependências do manifesto; requirements-runtime.lock registra o conjunto fixado. O consumidor não executa o gerador.

## Primeira consulta

Configure somente a credencial do serviço escolhido, por instância, a partir de ambiente privado ou cofre de segredos. O exemplo não emite nem cancela documentos. Execute consultas apenas com conta e ambiente autorizados; uma origem de fixture controlada deve ser configurada explicitamente pela API do cliente.

```python
import os
from webmania import CompanyCredentials, NfeClient, WebmaniaError

credentials = CompanyCredentials(
    consumer_key=os.environ['WEBMANIA_CONSUMER_KEY'],
    consumer_secret=os.environ['WEBMANIA_CONSUMER_SECRET'],
    access_token=os.environ['WEBMANIA_ACCESS_TOKEN'],
    access_token_secret=os.environ['WEBMANIA_ACCESS_TOKEN_SECRET'],
)
with NfeClient(credentials) as client:
    try:
        certificate = client.get_certificate_validity()  # expiration: dias >= 1
        sefaz = client.get_sefaz_status()                # online | offline
    except WebmaniaError as error:
        # Os detalhes já são limitados e redigidos; examine somente o necessário.
        print(error.kind, error.status)
```

A construção do cliente não comprova habilitação da conta. Respostas de sucesso e conversões explícitas para JSON podem conter dados fiscais, credenciais novas ou URLs privadas. Exponha apenas os campos necessários à aplicação.

## Ambiente e URL base

Cada cliente aceita `base_url` explícito; o padrão é a origem pública do serviço. A URL precisa ser HTTPS (HTTP somente em loopback para testes), sem usuário, query, fragmento ou segmentos `.`/`..`, e pode ter um prefixo de caminho. Os clientes de arquivo exigem também `trusted_origins` com a origem escolhida. As variáveis abaixo são usadas pelo exemplo de homologação; a SDK não lê ambiente por conta própria.

| Serviço | Cliente | Variável do exemplo | Padrão |
|---|---|---|---|
| API1 (NF-e/NFC-e) | `NfeClient` | `WEBMANIA_API1_BASE_URL` | `https://webmania.com.br/api` |
| Arquivos API1 | `NfeFilesClient` | `WEBMANIA_FILES_BASE_URL` | `https://nfe.webmania.com.br` |
| API2 (emissor, arquivos, relatórios atuais, Monitor) | `EmitterClient`, `EmitterFilesClient`, `ReportFilesClient`, `MonitorClient` | `WEBMANIA_API2_BASE_URL` | `https://api.webmania.com.br` |

```python
nfe = NfeClient(credentials, base_url=os.environ.get('WEBMANIA_API1_BASE_URL', 'https://webmania.com.br/api'))
```

## Integração e limites

Use strings para valores decimais exatos, códigos, chaves e identificadores. A SDK não converte strings em números, nem aplica arredondamento fiscal. Números JSON aceitos pelo contrato mantêm a representação numérica nativa do Python; `Decimal`, NaN e infinito não são serializados implicitamente. Campos omitidos, `None`, `False`, `0` e campos adicionais permitidos pelo schema continuam distintos. Campos adicionais de respostas são preservados.

Cada cliente reutiliza sua conexão HTTP/1.1 e pode ser fechado com `with` ou `close()`. Chamadas concorrentes na mesma instância são serializadas e respeitam cancelamento/deadline enquanto aguardam a conexão. Credenciais não são globais. TLS e hostname são sempre verificados; `ca_file` acrescenta uma CA explícita por cliente. `base_url` aceita HTTPS ou HTTP loopback para testes. Proxies de ambiente, cookies e autenticação de `.netrc` não são usados.

`FileAuth('document_token', token)` exige uma capability de documento já existente e envia somente o token. `FileAuth('issuer')` usa o Bearer configurado em `EmitterFilesClient`. MDF-e admite somente esse modo no contrato API 2. `FileAuth('anonymous')` é uma escolha explícita nas rotas API 2 que a permitem; não demonstra autenticação ou ausência de proteção. O relatório API 1 usa `FileAuth('capability')` e não recebe cabeçalhos empresariais. Falhas nunca provocam tentativa com outra modalidade.

`EmitterFilesClient.get_nfse_pdf` (e o helper `download_url` quando seleciona essa rota) retorna `FileResponse | FileRedirectResponse`. Em HTTP 2xx, `FileResponse.data` conserva os bytes, `media_type`, status e `content_disposition`. Status e MIME precisam ser declarados juntos na operação. HTML e JSON não são promovidos a PDF/XML; ZIP em uma rota XML gera `protected_file`. XML é analisado integralmente com limites, sem DTD/entidades externas, e atributos duplicados são rejeitados inclusive em UTF-16. ZIP clássico stored/deflate precisa concordar em flags, método, nomes, offsets, CRC e tamanhos locais/centrais/descritores; membros sobrepostos ou repetidos são recusados. Há descompressão limitada somente em memória (8 MiB por membro, 32 MiB total, 2048 membros, razão limitada), nunca extração no sistema de arquivos. XLSX exige tipos de conteúdo, namespaces e relacionamentos internos coerentes para todas as planilhas. XML tem profundidade 64 e limites de elementos/atributos.

## Relatórios

`NfeFilesClient.download_report` atende relatórios legados (`/relatorio/{uuid}/`). CSV e XLSX desse download podem chegar rotulados `text/xml`: a SDK identifica o formato pelos bytes (assinatura ZIP = XLSX; qualquer outro corpo é CSV devolvido byte a byte, sem decodificação) e informa o formato detectado em `FileResponse.media_type`. Um XML, uma página HTML ou um JSON nesse download é recusado com `protocol`; nenhuma outra operação de arquivo ganha essa tolerância.

Relatórios atuais são baixados por `ReportFilesClient` (`fiscalDownloadReportV2`, `GET /relatorios/{uuid}` na API2). Use `download_url` com a `url` devolvida por `create_or_poll_report`: só a origem configurada e a rota `/relatorios/{uuid}` são aceitas, sem redirecionamento, e a credencial enviada é a do modo explícito (`FileAuth('anonymous')`, `FileAuth('company')` com `credentials`, ou `FileAuth('issuer')` com o Bearer da empresa). Um JSON com `error`, mesmo em HTTP 200, é falha. A URL do relatório é uma capability sensível.

## Credenciais e resultado fiscal

Credenciais da empresa API1, revenda API1, Bearer do emissor API2 e Bearer Monitor pertencem a escopos diferentes. Arquivos exigem a modalidade de acesso documentada. Uma falha não autoriza trocar automaticamente o modo ou a credencial. Mantenha segredos no servidor.

O catálogo contém 102 operações habilitadas. `nfeDownloadIbsCbsEventXml` não está disponível nesta versão do SDK: a chamada falha com `capability` e nenhuma requisição é enviada. Condições fiscais, municipais, de cadastro e de provedor continuam sujeitas ao contrato e ao serviço. Validação local, cálculo ou prévia não comprovam autorização fiscal.

Os downloads de relatório (API1 e API2) podem consumir quota ou registrar acesso mesmo por GET; após possível envio sem resultado conhecido, `outcome=unknown` não autoriza repetir o download. A capability do relatório não é exposta como referência de recuperação.

Não há retry automático de operação nem seguimento automático de redirects. Depois de possível envio de uma operação com efeito, uma falha pode indicar resultado desconhecido. Preserve o seletor original com segurança, consulte a tentativa anterior e decida explicitamente como prosseguir. Uma referência protegida exige acesso deliberado e pode estar ausente; não é uma chave de idempotência.

## Arquivos e processamento

Verifique tipo de resultado, status e representação antes de consumir bytes. JSON pendente, HTML e redirect não comprovam PDF pronto. Proteção de PDF/ZIP é distinta da autorização de download; não há descriptografia automática nem confirmação de autenticidade fiscal. O reconhecimento de formatos cobre somente o perfil documentado desta implementação. Uma Location revelada continua privada e exige decisão explícita de origem e autenticação para outra transferência.

Paginação e espera são optativas e limitadas quando disponíveis. Um estado futuro ou desconhecido não significa conclusão. Não repita emissão, cancelamento ou importação inicial como se fossem consultas de processamento.

Para migrar uma integração anterior, remapeie métodos, modelos e escopos de credencial pela referência desta versão. Não há promessa de substituição automática de outro SDK; compare também o changelog quando disponível.

## Documentação para assistentes e contratos

Índices em Markdown para assistentes: [documentação Webmania](https://webmania.com.br/docs/llms.txt) e [API 2.0](https://api.webmania.com.br/llms.txt). Contratos OpenAPI: [API 2.0](https://api.webmania.com.br/docs/openapi) e [NF-e](https://webmania.com.br/docs/rest-api-nfe/?format=openapi).

No catálogo de SDKs, `python` aparece como disponível no repositório público, com instalação pelo clone; plataforma Python >= 3.11. Estar listado nesses índices não amplia a cobertura documentada deste SDK.
