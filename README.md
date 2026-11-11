<p align="center"><img src=".github/assets/webmania-logo.png" alt="Webmania" width="320"></p>

# Webmania SDK para Python

Através do emissor fiscal da Webmania®, você conta com a emissão e o arquivamento dos seus documentos fiscais, cálculo automático de impostos, geração do DANFE para impressão e envio automático de e-mails para os clientes. Com este SDK, o seu sistema em Python se integra à nossa REST API para emitir, consultar e cancelar NF-e, NFC-e, NFS-e, CT-e, MDF-e, NFCom e DC-e, baixar XML e PDF dos documentos e usar o Monitor Fiscal.

- Emissor de Nota Fiscal Webmania®: [Saiba mais](https://webmania.com.br/nota-fiscal-eletronica/)
- Documentação da REST API: [Visualizar](https://webmania.com.br/docs/)
- Índice da documentação para assistentes de IA: [llms.txt](https://webmania.com.br/docs/llms.txt)

## Requisitos

- Contrate um dos planos de Nota Fiscal Eletrônica da Webmania®: [Assine agora mesmo](https://webmania.com.br/nota-fiscal-eletronica/#plans-section).
- Python 3.11 ou superior. A única dependência, [jsonschema](https://pypi.org/project/jsonschema/), é instalada junto com o SDK.
- Credenciais de acesso da sua empresa, disponíveis no [Painel de Controle](https://webmania.com.br/painel/).

## Instalação

O SDK é distribuído pelo repositório [github.com/webmaniabr/webmania-python](https://github.com/webmaniabr/webmania-python) e ainda não está publicado no PyPI. Clone o repositório, gere o pacote e instale-o no ambiente da sua aplicação:

```sh
git clone https://github.com/webmaniabr/webmania-python.git
python -m pip install build
python -m build --outdir dist webmania-python
python -m pip install --constraint webmania-python/requirements-runtime.lock dist/webmania_sdk-0.1.0a8-py3-none-any.whl
```

Depois disso, importe o SDK na sua aplicação com `import webmania`.

## Credenciais

Cada serviço usa a sua própria credencial. Guarde-as em variáveis de ambiente (ou em um cofre de segredos) no servidor e nunca as escreva no código-fonte:

| Variável de ambiente | Uso |
|---|---|
| `WEBMANIA_CONSUMER_KEY`, `WEBMANIA_CONSUMER_SECRET`, `WEBMANIA_ACCESS_TOKEN`, `WEBMANIA_ACCESS_TOKEN_SECRET` | NF-e e NFC-e (`NfeClient`) e arquivos da NF-e (`NfeFilesClient`) |
| `WEBMANIA_ISSUER_TOKEN` | NFS-e, CT-e, MDF-e, NFCom e DC-e (`EmitterClient`) e seus arquivos (`EmitterFilesClient`) |
| `WEBMANIA_MONITOR_TOKEN` | Monitor Fiscal (`MonitorClient`) |

```python
import os
from webmania import CompanyCredentials, EmitterClient, NfeClient

credenciais = CompanyCredentials(
    consumer_key=os.environ['WEBMANIA_CONSUMER_KEY'],
    consumer_secret=os.environ['WEBMANIA_CONSUMER_SECRET'],
    access_token=os.environ['WEBMANIA_ACCESS_TOKEN'],
    access_token_secret=os.environ['WEBMANIA_ACCESS_TOKEN_SECRET'],
)

nfe = NfeClient(credenciais)                                  # NF-e e NFC-e
emissor = EmitterClient(os.environ['WEBMANIA_ISSUER_TOKEN'])  # NFS-e, CT-e, MDF-e, NFCom e DC-e
```

Cada cliente mantém uma conexão aberta: reutilize a mesma instância e chame `close()` ao terminar, ou use o cliente em um bloco `with`.

## Utilização

Os exemplos abaixo usam o ambiente de **homologação** (`ambiente` 2), em que os documentos não têm validade fiscal. Para emitir em produção, envie `ambiente` 1. Informe valores decimais como texto (`'44.90'`) para manter a precisão.

### Status do SEFAZ e certificado A1

```python
sefaz = nfe.get_sefaz_status()
print(sefaz['status'])  # online ou offline

certificado = nfe.get_certificate_validity()
print(certificado['expiration'])  # dias restantes até o vencimento do certificado A1
```

### Emitir NF-e

Para emitir uma NF-e, utilize o método `issue_document`. O mesmo método emite NFC-e com `'modelo': 2`.

```python
nota = nfe.issue_document({
    'operacao': 1,  # 1 = saída
    'natureza_operacao': 'Venda de produção do estabelecimento',
    'modelo': 1,  # 1 = NF-e, 2 = NFC-e
    'finalidade': 1,  # 1 = NF-e normal
    'ambiente': 2,  # 2 = homologação, 1 = produção
    'cliente': {
        'cpf': '000.000.000-00',
        'nome_completo': 'Nome do Cliente',
        'endereco': 'Av. Brg. Faria Lima',
        'numero': '1000',
        'bairro': 'Itaim Bibi',
        'cidade': 'São Paulo',
        'uf': 'SP',
        'cep': '00000-000',
        'email': 'nome@email.com',
    },
    'produtos': [{
        'nome': 'Nome do produto',
        'codigo': 'nome-do-produto',
        'ncm': '6109.10.00',
        'quantidade': '1',
        'unidade': 'UN',
        'origem': 0,
        'subtotal': '44.90',
        'total': '44.90',
        'classe_imposto': 'REF1000',  # classe de imposto cadastrada no Painel
    }],
    'pedido': {
        'presenca': 2,  # operação não presencial, pela internet
        'modalidade_frete': 9,  # sem frete
        'pagamento': 0,  # pagamento à vista
        'forma_pagamento': '01',  # dinheiro
        'total': '44.90',
    },
})

print(nota['uuid'])         # identificador único da nota fiscal
print(nota['status'])       # aprovado, reprovado, processamento, contingencia...
print(nota.get('nfe'))      # número da NF-e
print(nota.get('serie'))    # série
print(nota.get('chave'))    # chave de acesso
print(nota.get('xml'))      # URL do XML
print(nota.get('danfe'))    # URL do DANFE (PDF)
print(nota.get('motivo'))   # retorno do SEFAZ
```

Somente o status `aprovado` indica uma nota autorizada. Quando o retorno for `processamento`, consulte a nota alguns segundos depois.

### Consultar NF-e

```python
consulta = nfe.get_document(query={'uuid': nota['uuid']})
print(consulta['status'])
```

A consulta também aceita a chave de acesso (`{'chave': ...}`).

### Cancelar NF-e

```python
cancelamento = nfe.cancel_document({
    'uuid': nota['uuid'],
    'motivo': 'Cancelamento por erro no pedido.',  # mínimo de 15 caracteres
})
print(cancelamento['status'])
```

### Baixar o DANFE e o XML

```python
from webmania import FileAuth, NfeFilesClient

with NfeFilesClient(credentials=credenciais, trusted_origins=['https://nfe.webmania.com.br']) as arquivos:
    danfe = arquivos.download_danfe(identifier=nota['uuid'], auth=FileAuth('company'))
    with open('danfe.pdf', 'wb') as pdf:
        pdf.write(danfe.data)

    xml = arquivos.download_xml(identifier=nota['uuid'], auth=FileAuth('company'))
    with open('nfe.xml', 'wb') as arquivo:
        arquivo.write(xml.data)
```

### Emitir, consultar e cancelar NFS-e

A NFS-e é emitida a partir de um ou mais RPS com o método `issue_nfse` do `EmitterClient`:

```python
nfse = emissor.issue_nfse({
    'ambiente': 2,  # 2 = homologação, 1 = produção
    'rps': [{
        'servico': {
            'valor_servicos': '15.00',
            'discriminacao': 'Prestação de serviço referente ao mês 10/2026',
            'classe_imposto': 'REF000000',  # classe de imposto cadastrada no Painel
        },
        'tomador': {
            'cpf': '000.000.000-00',
            'nome_completo': 'Nome do tomador',
        },
    }],
})
uuid_nfse = nfse['uuid']
print(nfse['status'])

consulta = emissor.get_nfse(identifier=uuid_nfse)
print(consulta['status'], consulta.get('numero'), consulta.get('pdf_nfse'))

cancelamento = emissor.cancel_nfse({
    'uuid': uuid_nfse,
    'motivo': '1',  # código do motivo de cancelamento (veja a documentação da NFS-e)
    'justificativa': 'Serviço cancelado a pedido do tomador.',  # mínimo de 15 caracteres
})
print(cancelamento['status'])
```

### Tratamento de erros

Toda falha gera uma `WebmaniaError`:

```python
from webmania import WebmaniaError

try:
    nota = nfe.issue_document(dados_da_nota)
except WebmaniaError as erro:
    print(erro.kind)      # validation (dados recusados antes do envio), business (recusa da API ou do SEFAZ), http, timeout...
    print(erro.status)    # status HTTP, quando houver
    print(erro.response)  # resposta da API, com dados sensíveis mascarados
    if erro.outcome == 'unknown':
        # A requisição pode ter sido processada: consulte a nota antes de emitir de novo.
        ...
```

O SDK não repete requisições automaticamente. Se uma emissão ou um cancelamento terminar com `outcome == 'unknown'`, consulte o documento antes de tentar novamente, para não emitir em duplicidade.

## Métodos disponíveis

**NF-e e NFC-e** — `NfeClient`

- **issue_document**: Emissão de NF-e ou NFC-e junto ao SEFAZ.
- **get_document**: Consulta da nota fiscal pelo UUID, pela chave de acesso ou pelo ID do pedido.
- **cancel_document**: Cancelamento de NF-e ou NFC-e.
- **create_correction**: Carta de correção.
- **void_numbering**: Inutilização de sequência de numeração.
- **issue_return**: Emissão de NF-e de devolução.
- **issue_complement**: Emissão de NF-e complementar.
- **issue_adjustment**: Emissão de NF-e de ajuste.
- **create_manifestation**: Manifestação do destinatário.
- **create_payment_event** / **cancel_payment_event**: Evento de conciliação financeira (ECONF) e o seu cancelamento.
- **create_ibs_cbs_event** / **cancel_ibs_cbs_event**: Eventos de IBS/CBS e o seu cancelamento.
- **list_tax_classes** / **save_tax_classes** / **delete_tax_classes**: Classes de imposto.
- **create_or_poll_report**: Relatórios fiscais.
- **update_company**: Atualização dos dados da empresa emissora.
- **get_sefaz_status**: Verifica se o SEFAZ está online ou offline.
- **get_certificate_validity**: Verifica quantos dias faltam para o certificado A1 expirar.

**NFS-e** — `EmitterClient`

- **issue_nfse**: Emissão de NFS-e a partir de RPS.
- **get_nfse**: Consulta da NFS-e.
- **cancel_nfse**: Cancelamento da NFS-e.
- **replace_nfse**: Substituição de NFS-e.
- **manifest_nfse**: Manifestação sobre NFS-e nacional.
- **get_nfse_provider_status**: Recursos do provedor de NFS-e do município da empresa.

**CT-e e CT-e OS** — `EmitterClient`

- **issue_cte** / **issue_simplified_cte**: Emissão de CT-e, CT-e OS e CT-e simplificado.
- **get_cte**: Consulta do CT-e.
- **cancel_cte**: Cancelamento do CT-e.
- **correct_cte**: Carta de correção do CT-e.
- **confirm_cte_delivery** / **cancel_cte_delivery**: Comprovante de entrega e o seu cancelamento.
- **link_cte_payment** / **cancel_cte_payment_link** / **get_cte_payment_events**: Eventos de pagamento do CT-e.

**MDF-e** — `EmitterClient`

- **issue_mdfe**: Emissão do MDF-e.
- **get_mdfe**: Consulta do MDF-e pela chave de acesso.
- **close_mdfe**: Encerramento do MDF-e.
- **cancel_mdfe**: Cancelamento do MDF-e.
- **add_mdfe_conductor**: Inclusão de condutor.

**NFCom e DC-e** — `EmitterClient`

- **issue_nfcom** / **get_nfcom** / **cancel_nfcom**: Emissão, consulta e cancelamento da NFCom.
- **get_nfcom_payment_events**: Eventos de pagamento da NFCom.
- **get_nfcom_service_status**: Disponibilidade do serviço da NFCom no SEFAZ.
- **issue_dce** / **get_dce** / **cancel_dce**: Emissão, consulta e cancelamento da DC-e.

**Arquivos (XML e PDF)** — `NfeFilesClient` e `EmitterFilesClient`

- **download_danfe** / **download_simple_danfe** / **download_label_danfe**: DANFE completo, simplificado e etiqueta.
- **download_xml** / **download_cancellation_xml**: XML da NF-e e do cancelamento.
- **download_correction_pdf** / **download_correction_xml**: PDF e XML da carta de correção.
- **get_nfse_xml** / **get_nfse_pdf** / **get_nfse_rps_pdf**: XML e PDF da NFS-e e PDF do RPS.
- **get_cte_xml** / **get_cte_pdf** / **get_mdfe_xml** / **get_mdfe_pdf** / **get_nfcom_xml** / **get_nfcom_pdf** / **get_dce_xml** / **get_dce_pdf**: XML e PDF de CT-e, MDF-e, NFCom e DC-e.

**Monitor Fiscal** — `MonitorClient`

- **search_documents** / **get_document** / **list_document_events**: Busca e consulta de documentos recebidos e do histórico de eventos.
- **manifest_document**: Manifestação do destinatário.
- **import_document** / **get_import_status**: Importação por chave de acesso, XML ou ZIP.
- **list_companies** / **create_company** / **update_company**: Empresas monitoradas.

**Gerencial B2B** — `ResellerClient`

- **create_companies** / **list_companies** / **get_processed_requests**: Cadastro de empresas, listagem e contagem de notas processadas por empresa.

A lista completa, com todos os métodos do Monitor Fiscal e dos arquivos, está em [docs/OPERATIONS.md](docs/OPERATIONS.md).

## Exemplo completo em homologação

A pasta [examples/homologacao](examples/homologacao) traz um programa que emite, consulta, baixa os arquivos e cancela uma NF-e e uma NFS-e em homologação, usando as credenciais das variáveis de ambiente. Por segurança, ele só envia requisições quando `WEBMANIA_LIVE=1` está definido e `WEBMANIA_LIVE_ALLOWED_HOSTS` lista os hosts da API. Para rodar só as consultas (status do SEFAZ, certificado e provedor de NFS-e):

```sh
WEBMANIA_LIVE=1 WEBMANIA_LIVE_SCOPE=readonly WEBMANIA_LIVE_ALLOWED_HOSTS=webmania.com.br,nfe.webmania.com.br,api.webmania.com.br sh examples/homologacao/run.sh
```

As variáveis aceitas e o formato da saída estão em [examples/homologacao/README.md](examples/homologacao/README.md).

## Documentação

- Documentação da REST API: [NF-e / NFC-e](https://webmania.com.br/docs/rest-api-nfe/) · [NFS-e](https://webmania.com.br/docs/rest-api-nfse/) · [CT-e](https://webmania.com.br/docs/rest-api-cte/) · [MDF-e](https://webmania.com.br/docs/rest-api-mdfe/) · [NFCom](https://webmania.com.br/docs/rest-api-nfcom/) · [DC-e](https://webmania.com.br/docs/rest-api-dce/) · [Monitor Fiscal](https://webmania.com.br/docs/rest-api-monitor-fiscal/) · [Gerencial B2B](https://webmania.com.br/docs/rest-api-gerencial-b2b/)
- Contratos OpenAPI: [API 2.0](https://api.webmania.com.br/docs/openapi) e [NF-e](https://webmania.com.br/docs/rest-api-nfe/?format=openapi)
- Detalhes técnicos do SDK (URL base, arquivos, relatórios, limites): [docs/INTEGRATION.md](docs/INTEGRATION.md)
- Lista completa de operações: [docs/OPERATIONS.md](docs/OPERATIONS.md)
- Desenvolvimento e testes do SDK: [docs/TESTING.md](docs/TESTING.md)
- Histórico de versões: [CHANGELOG.md](CHANGELOG.md)

## Suporte

Qualquer dúvida entre em contato na nossa [Central de Ajuda](https://ajuda.webmania.com.br) ou acesse o [Painel de Controle](https://webmania.com.br/painel/) para conversar em tempo real no Chat ou Abrir um chamado.

## Licença

Licença proprietária Webmania®: veja [LICENSE](LICENSE) e os [Termos de Uso](https://webmania.com.br/termos-de-uso/). As dependências de terceiros mantêm as suas próprias licenças.
