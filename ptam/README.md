# PTAM — materiais de avaliação de imóveis

Documentos de apoio para o Parecer Técnico de Avaliação Mercadológica (PTAM),
com a identidade visual da Wisekey.

## Arquivos

| Arquivo | Para quem | Páginas |
|---|---|---|
| `relacao-documentos-ptam.pdf` | **Cliente** — documento formal com a relação de documentos e informações | 3 |
| `wisekey-checklist-ptam-interno.pdf` | **Uso interno** — checklist técnico de conferência, com a metodologia | 3 |

Os `.html` são o fonte de cada PDF. Edite o HTML e gere o PDF de novo.

O documento do cliente segue estrutura de correspondência formal: papel
timbrado, quadro de referência, carta de abertura, seções numeradas (1 a 6),
fecho e assinatura, com numeração de página em todas as folhas.

## Como gerar os PDFs novamente

```bash
pip install pypdf reportlab
python3 gerar.py                            # gera todos
python3 gerar.py relacao-documentos-ptam.html   # gera um
```

O script converte o HTML com Chrome/Chromium headless e carimba a numeração de
página. Se o navegador não estiver no PATH, aponte com `CHROME_BIN`.
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
