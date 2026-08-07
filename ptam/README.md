# PTAM — materiais de avaliação de imóveis

Documentos de apoio para o Parecer Técnico de Avaliação Mercadológica (PTAM),
com a identidade visual da Wisekey.

## Arquivos

| Arquivo | Para quem | Páginas |
|---|---|---|
| `Wisekey - PTAM - Relação de Documentos.pdf` | **Cliente** — documento formal com a relação de documentos e informações | 3 |
| `Wisekey - PTAM - Checklist Interno.pdf` | **Uso interno** — checklist técnico de conferência, com a metodologia | 3 |

O nome do arquivo é o primeiro contato do cliente com o documento, antes de
abri-lo. Mantenha o padrão `Wisekey - PTAM - <Documento>` ao criar novos: marca,
tipo de trabalho e conteúdo, nessa ordem. O `Checklist Interno` traz "Interno"
no nome justamente para não ser enviado por engano.

Os `.html` são o fonte de cada PDF. Edite o HTML e gere o PDF de novo.

O documento do cliente segue estrutura de correspondência formal: papel
timbrado, quadro de referência, carta de abertura, seções numeradas (1 a 6),
fecho e assinatura, com numeração de página em todas as folhas.

## Como gerar os PDFs novamente

```bash
pip install pypdf reportlab
python3 gerar.py                            # gera todos
python3 gerar.py "Wisekey - PTAM - Relação de Documentos.html"   # gera um
```

O script converte o HTML com Chrome/Chromium headless, carimba a numeração de
página e grava os metadados do PDF (título, autor e assunto). Se o navegador
não estiver no PATH, aponte com `CHROME_BIN`.
O `logo-wisekey.png` precisa estar na mesma pasta do HTML.

## O que preencher antes de enviar

O documento do cliente tem três campos em branco no quadro de referência:
**Solicitante**, **Imóvel avaliando** e **Data**, mais o **Documento nº** para
controle interno. Preencha no HTML e gere o PDF, ou imprima e complete à mão.

## O que costuma mudar entre um atendimento e outro

- **Prazo de elaboração** (hoje: 5 dias úteis) e **validade do parecer**
  (6 meses) — seção 6.
- **Honorários** — nenhum dos dois documentos menciona valor. Se você cobra pelo
  PTAM, inclua na seção 6 antes de enviar ao cliente.
- **Bairro e cidade** — aparecem na capa do checklist interno.

## Identificação da empresa e do responsável técnico

Confirmados por dois documentos: o Certificado de Licenciamento Integrado
(Portal Facilita SP, protocolo SPP2630499283) e a Alteração Contratual 03,
registrada na JUCESP em 15/07/2026 sob nº 277.827/26-7.

- **Nome empresarial:** WISEKEY ESTRATEGIA E ASSESSORIA LTDA
- **CNPJ:** 58.501.287/0001-13
- **Natureza jurídica:** Sociedade Empresária Limitada
- **Município e foro:** São João da Boa Vista, SP
- **Responsável técnico:** Raphael Piotto Cardoso — **CRECI/SP 319841-F**

A cláusula Décima Primeira da alteração contratual atribui a responsabilidade
técnica pela atividade de intermediação imobiliária ao sócio administrador,
nos termos da Lei nº 6.530/78 e da Resolução COFECI nº 327/92 — que é a
estrutura exigida para a sociedade atuar no ramo. Por isso o responsável
técnico consta do timbre, do quadro de referência e do bloco de assinatura,
sempre com o número **319841-F** (o sufixo `-F` identifica a inscrição de
pessoa física e faz parte do número).

Pendente de confirmação:

1. **Acentuação de "ESTRATEGIA".** Tanto o certificado quanto o nome do arquivo
   da alteração contratual grafam sem acento. Se o contrato social consolidado
   trouxer "ESTRATÉGIA", ajuste o timbre para seguir o contrato.
2. **Número de inscrição da PJ no CRECI-SP.** A designação de responsável
   técnico é o pressuposto da inscrição, mas o número da pessoa jurídica não
   consta dos documentos consultados. Ao obtê-lo, acrescente ao timbre, ao lado
   do CNPJ.

Endereço de rua foi omitido de propósito: o certificado declara "A empresa terá
estabelecimento? Não".

## Identidade visual

Cores e tipografia vêm da landing page (`../index.html`):

- Azul institucional `#132F70` — cabeçalhos
- Roxo `#2D1E80` e roxo escuro `#1c1259` — destaques e blocos finais
- Lilás `#EFEAFC` / `#DCD2FA` — fundos de apoio
- Fonte: Poppins na web; nos PDFs cai para a sans-serif do sistema, já que a
  fonte não é embutida.

## Base normativa

O PTAM pode ser emitido por corretor de imóveis habilitado, nos termos da
Resolução COFECI nº 1.066/2014, com metodologia baseada na NBR 14653 (Método
Comparativo Direto de Dados de Mercado). Para finalidades judiciais, periciais
ou operações que exijam laudo de engenharia, pode ser necessária avaliação por
engenheiro ou arquiteto habilitado, conforme exigência do órgão destinatário.
