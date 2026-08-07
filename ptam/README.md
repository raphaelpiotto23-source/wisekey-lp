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

Confirmados pelo contrato social consolidado (Alteração Contratual nº 03,
registrada na JUCESP em 15/07/2026 sob nº 277.827/26-7) e pelo Certificado de
Licenciamento Integrado (Portal Facilita SP, protocolo SPP2630499283).

- **Nome empresarial:** WISEKEY ESTRATEGIA E ASSESSORIA LTDA — sem acento em
  "ESTRATEGIA", conforme cláusula Primeira do contrato consolidado
- **CNPJ:** 58.501.287/0001-13 · **NIRE:** 35265750384 (18/12/2024)
- **Natureza jurídica:** Sociedade Empresária Limitada unipessoal · ME
- **Sede:** Rua Inocêncio Papiani, 400, Sala 2 · Pousada do Sol ·
  São João da Boa Vista/SP · CEP 13874-590
- **Responsável técnico:** Raphael Piotto Cardoso — **CRECI/SP 319841-F**

O **objeto social** (cláusula Terceira) inclui expressamente "corretagem e
assessoria na compra, venda e **avaliação de imóveis**" — é o que ampara a
emissão de PTAM pela sociedade.

A cláusula Décima Primeira atribui a responsabilidade técnica pela atividade de
intermediação imobiliária ao sócio administrador, nos termos da Lei nº 6.530/78
e da Resolução COFECI nº 327/92, com redação "conforme modelo aprovado pelo
CRECI/SP". Por isso o responsável técnico consta do timbre, do quadro de
referência e do bloco de assinatura, sempre com o número **319841-F** — o
sufixo `-F` integra a inscrição.

**CPF, RG e endereço residencial do sócio não são usados** em nenhum dos
documentos: são dados pessoais sem função no PTAM.

Duas decisões tomadas, já refletidas nos documentos:

1. **Bairro: Pousada do Sol.** O Certificado de Licenciamento Integrado traz
   "Loteamento Colinas do Alegre" para o mesmo endereço e CEP. Prevalece o
   contrato social, que é o instrumento que fixa a sede.
2. **Sem CRECI de pessoa jurídica.** Os documentos identificam apenas o
   responsável técnico, com o CRECI/SP 319841-F. Quando a inscrição da PJ sair,
   acrescente o número ao timbre, ao lado do CNPJ, e ao rodapé — a partir daí a
   sociedade passa a figurar como emissora, e não apenas como prestadora com
   responsável técnico designado.

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
