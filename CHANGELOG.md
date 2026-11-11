# Changelog

## 0.1.0a8

- README rewritten for integrators: requirements, installation, credentials from environment variables, homologation examples that issue, consult and cancel an NF-e and an NFS-e, and the method list per product. The technical details that were in the README moved unchanged to `docs/INTEGRATION.md`, `docs/TESTING.md`, `docs/OPERATIONS.md` and `examples/homologacao/README.md`. Documentation only.
- README: the SDK is presented as available from the public GitHub repository and installed from a clone (`git clone https://github.com/webmaniabr/webmania-python.git`); it is still not published to a package registry. Documentation only: code and contract are unchanged.
- Regenerated from the updated public contract: tax-class list totals (`tributos_federais`, `tributos_estaduais`) accept the empty string the API returns for unset values; tax-class `situacao_tributaria` is 2 digits for IPI, PIS and COFINS and 2 to 3 digits for ICMS; NFS-e `impostos.reducao` and `impostos.cp` accept a string or a number.
- The homologation example treats `reprovado` (the API 1.0 status of a refused NF-e) as terminal.
- The homologation example requires `WEBMANIA_LIVE_ALLOWED_HOSTS` (exit 77 before any credential or request when it is missing or empty) and fails the run when the consult after a cancellation does not show `cancelado`.
- The homologation example requires a writable `WEBMANIA_LIVE_LEDGER` before the first mutation of an `nfe`, `nfse` or `all` scope (exit 77 with reason `ledger` and no request otherwise), so an unknown outcome is always recorded.
- Generated from the current public contract (14 modules, 103 operations, 102 enabled), pinned by `contract_digest` and per-module SHA-256 instead of a commit. Issuance request models follow the operation-derived `<OperationId>Payload` names.
- Legacy report download accepts CSV and XLSX labeled `text/xml`, identified by bytes (ZIP signature = XLSX, otherwise CSV kept byte-exact); XML, HTML and JSON bodies are refused as reports. Declared report formats must match their bytes.
- New `ReportFilesClient.download_report_v2` (`fiscalDownloadReportV2`) and `download_url` for current report URLs on the configured API2 origin, with explicit access mode and no redirects.
- Recovery references keep caller selectors when an unexpected `Location` only contains route segments; diagnostics stay masked.
- `nfeDownloadIbsCbsEventXml` reports "not available in this SDK release" without sending a request.
- Generator reads and writes UTF-8 bytes explicitly; quickstart checks survive `python -O`; the installed-package receipt records only measured counts.
- New neutral homologation example (`examples/homologacao`) and tests for report formats, current report URLs, many chunk-size lines, post-send timeout/cancellation and explicit origins.

## 0.1.0a7

- Treat only fiscalDownloadReport as possibly effectful under its pinned download-quota policy. Post-send ambiguity and invalid successful file representations now preserve unknown outcome; complete HTTP422 and pre-send cancellation keep their existing classification. Capability recovery, credentials and no-retry rules remain unchanged.

## 0.1.0a6

- Vincula DNS/socket ao processo filho com deadline, Event, close e reap; mantém reuse entre chamadas explícitas e distingue handshake de dispatch.
- Inspeciona todos os 1xx, cabeçalhos e trailers com limites; Location limita diagnósticos e recuperação, inclusive em respostas abortadas.
- Preserva vocabulário público/booleanos e aplica fronteiras apenas a capabilities curtas; credenciais e sobreposições literais mantêm proteção.
- Preserva inteiros semânticos de resposta como int exato e recusa underflow/fracionários arredondados a inteiro; rejeita JSON não finito por overflow, ciclos, profundidade excessiva e surrogates antes de I/O; lê contratos explicitamente como UTF-8.
- Acrescenta max_items/continuation vinculados a filtros e per_page e retorna importação terminal invalido com erro.
- Exige status/MIME exatos e valida estrutura limitada de XML, ZIP, XLSX e PDF clássico; estruturas fora do subconjunto são recusadas.

## 0.1.0a5

- Protege a união de segredos sobrepostos no texto original dos diagnósticos, incluindo UUIDs contextuais, representações numéricas e URLs, antes de inserir os marcadores de redação.
- Mantém a correspondência literal sensível à caixa dos segredos opacos, a equivalência ASCII contextual dos UUIDs e os limites de diagnóstico existentes.

## 0.1.0a4

- Mantém a redação de UUIDs de path quando Location tem autoridade malformada, sem aceitar/reparar a URI nem aplicar equivalência de caixa à autoridade, userinfo ou query opaca.

## 0.1.0a3

- Redige UUIDs conhecidos no path de Location também em grafias ASCII hex equivalentes, mantendo tokens opacos da query com correspondência literal.

## 0.1.0a2

- Retorna o 302 documentado do PDF NFS-e como FileRedirectResponse, com Location protegida e recuperação explícita, sem resolução, acesso ou autorização automática do destino.
- Preserva resultado incerto e referência protegida após redirecionamento inesperado de mutação; recusa Location inválida/ambígua sem expor capacidades nos diagnósticos.
- Fecha corretamente respostas de corpo vazio antes de reutilizar a conexão e mantém a interface FileResponse dos arquivos 2xx.

## 0.1.0a1

- Corrige leitura de respostas completas com Content-Length e fechamento de conexão, preservando truncamento e deadlines.
- Trata a presença de error como falha e deixa a autoridade de calendário das estatísticas com o provedor.
- Preserva referências fiscais em recuperação explícita protegida, sem publicá-las nos diagnósticos comuns.
- Conserva campos e obrigatoriedade em composições de modelos, com consumidores estáticos positivos/negativos.
- Normaliza somente download=1 previsto no contrato e redige valores de toda a profundidade aceita a partir do snapshot serializado.

## 0.1.0a0

- Primeira prévia Python síncrona para Emissor Fiscal e Monitor Fiscal, gerada de 13 módulos públicos e 102 operações.
- Autenticação isolada por serviço, transporte reutilizável com TLS verificado, deadlines/limites/cancelamento e nenhuma repetição automática.
- Modelos tipados, validação JSON Schema e limites decimais exatos, arquivos com modalidades explícitas, paginação e esperas limitadas.
- Corpus sintético HTTP/TLS e verificação de wheel/sdist instalados. Testes fiscais reais ficam para versões posteriores.
