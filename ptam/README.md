# PTAM — materiais de avaliação de imóveis

Documentos de apoio para o Parecer Técnico de Avaliação Mercadológica (PTAM),
com a identidade visual da Wisekey.

## Arquivos

| Arquivo | Para quem | Páginas |
|---|---|---|
| `wisekey-o-que-enviar-cliente.pdf` | **Cliente** — lista do que ele precisa enviar, em linguagem simples | 2 |
| `wisekey-checklist-ptam-interno.pdf` | **Uso interno** — checklist técnico completo, com a metodologia | 3 |

Os `.html` são o fonte de cada PDF. Edite o HTML e gere o PDF de novo.

## Como gerar o PDF novamente

Com Chrome ou Chromium instalado:

```bash
chromium --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=wisekey-o-que-enviar-cliente.pdf \
  wisekey-o-que-enviar-cliente.html
```

O `logo-wisekey.png` precisa estar na mesma pasta do HTML.

## O que costuma mudar entre um atendimento e outro

- **Nome do cliente e endereço do imóvel** — a versão do cliente é genérica de
  propósito; para personalizar, acrescente na capa (`.capa`).
- **Bairro e cidade** — aparecem na capa do checklist interno.
- **Prazo de entrega** (hoje: 5 dias úteis) e **validade do parecer** (6 meses).
- **Honorários** — nenhum dos dois documentos menciona valor. Se você cobra pelo
  PTAM, inclua antes de enviar ao cliente.

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
