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

## Identificação da empresa

Confirmada pelo Certificado de Licenciamento Integrado (Portal Facilita SP,
protocolo SPP2630499283):

- **Nome empresarial:** WISEKEY ESTRATEGIA E ASSESSORIA LTDA
- **CNPJ:** 58.501.287/0001-13
- **Natureza jurídica:** Sociedade Empresária Limitada
- **Município:** São João da Boa Vista, SP

Dois pontos a confirmar antes de usar os documentos em escala:

1. **Acentuação.** O certificado grafa "ESTRATEGIA" sem acento, como é praxe
   nos cadastros oficiais. Se o contrato social registrado na Junta Comercial
   trouxer "ESTRATÉGIA", o timbre deve seguir o contrato social.
2. **Inscrição no CRECI como pessoa jurídica.** O nome empresarial e a
   atividade licenciada ("Escritório Administrativo") não indicam intermediação
   imobiliária. O PTAM é emitido pelo corretor pessoa física — por isso o
   CRECI-SP 319841 aparece apenas no quadro "Responsável técnico" e no bloco de
   assinatura, nunca ao lado da razão social no timbre. Se a empresa vier a ser
   inscrita no CRECI-SP como PJ, o número da PJ pode ser acrescentado ao timbre.

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
