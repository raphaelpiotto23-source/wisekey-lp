# Calculadora de imóveis Wisekey — o que foi feito e o que ficou aberto

Documento de passagem da sessão de 20/08/2026.
Branch: `claude/calculadora-avaliacao-imoveis-jphr4e` · Repositório: `raphaelpiotto23-source/wisekey-lp`

---

## 1. O que existe agora

Quatro telas, numa página única com abas, mais os três módulos funcionando soltos.

| Arquivo | Tela | Responde |
|---|---|---|
| `calculadora.html` | as quatro abas juntas | é o arquivo para usar |
| `estimativa.html` | **Ideia de valor** | quanto vale, em dois cliques |
| `avaliacao.html` | **Comprar** | vale a pena comprar este studio? |
| `avaliacao-venda.html` | **Avaliar para vender** | PTAM com fundamentação |
| — | **Base de cálculo** | de onde vem cada número |

Publicada e navegável em: <https://claude.ai/code/artifact/02aff36d-9e45-4e84-b758-7c8b68a4b209>

> A versão publicada usa fonte de sistema no lugar da Poppins — o CSP da hospedagem bloqueia CDN de fonte. No repositório continua Poppins.

---

## 2. Ideia de valor — a via rápida

Para o telefone tocar e já haver número na mão.

**Entradas:** cidade → tipo → estado → porte → diferenciais.
**Saída:** faixa de conversa, mediana da cidade, aluguel esperado, renda bruta, valorização, vacância e **quantos bairros sustentam aquela mediana**.

Os diferenciais entram como prêmio sobre a mediana, com **teto somado de 15%**:

| Diferencial | Prêmio | | Diferencial | Prêmio |
|---|---|---|---|---|
| Ar-condicionado | +2% | | Edícula ou gourmet | +3% |
| Suíte | +3% | | Churrasqueira | +1% |
| Mais de uma suíte | +3% | | Energia solar | +3% |
| Móveis planejados | +2% | | Vaga coberta a mais | +2% |
| Piscina | +4% | | | |

O teto existe porque a mediana da cidade já embute o padrão local: sem ele, marcar tudo daria +23% e a estimativa perderia o pé. Quando o teto corta, a tela avisa.

**Leitura de valor** (sai em PDF com cabeçalho de cliente, data e CRECI):
- três preços — venda rápida, mercado e anúncio;
- curva de prazo, do preço pedido ao tempo até fechar.

**Confiança visível.** Cada mediana mostra o tamanho da amostra e muda de recado:

- São João da Boa Vista, casa 3 quartos → 20 bairros → *amostra forte*
- Itapira, 2 quartos → 1 bairro → *amostra fina*, com aviso para puxar três anúncios da rua antes de falar um número em voz alta

---

## 3. Comprar — a régua do investidor

Três respostas em vez de uma:

1. **Valor de mercado** — comparativo: R$/m² da região ajustado por 11 fatores.
2. **Valor pela renda** — capitalização do NOI no cap rate alvo.
3. **Teto de compra** — o preço máximo que ainda entrega a meta.

Duas travas, que existem porque a primeira versão errava sem elas:

- a avaliação não passa de **1,15× o comparativo** — na revenda vale o que o bairro paga, e a renda de temporada chegava a puxar o valor 50% acima do mercado;
- o **teto nunca supera a avaliação** — renda boa não é motivo para pagar acima do que o ativo vale. Sem essa trava, um pedido de R$ 600 mil num imóvel de R$ 383 mil recebia veredito de "comprar".

Botão **Carregar o motor do site** monta o cenário do studio benchmark e devolve os números do motor de produção, exatos.

---

## 4. Avaliar para vender — PTAM

Segue o checklist do Parecer Técnico de Avaliação Mercadológica que já existia no branch `claude/analise-imovel-sjbv-clys39`, pasta `ptam/`.

- **Homogeneização por comparável**, não da média — cada dado da amostra é trazido às características do avaliando por área, padrão, conservação e idade, e só então entra na estatística. Era o erro conceitual da primeira versão: com fatores diferentes por linha, os dois caminhos dão números diferentes.
- **Saneamento** com descarte do que se afasta do limite; o comparável descartado fica visível e riscado, para não sumir sem conferência.
- **Tratamento estatístico**: média saneada, desvio padrão, coeficiente de variação, intervalo de confiança de 80% por t de Student.
- **Grau de fundamentação** I, II ou III, por número de dados e amplitude do intervalo.
- **Depreciação Ross-Heidecke** — como manda o checklist.
- **Liquidação forçada** quando a finalidade é inventário, partilha, divórcio ou garantia.
- **Evolutivo como contraprova**, fora da ponderação: havendo amostra, o comparativo conclui sozinho, e divergência acima de 30% vira aviso em vez de virar média.

Teste com seis comparáveis do Jardim Amélia: média homogeneizada de R$ 3.702/m², desvio de R$ 72, CV de 1,9%, Grau II. Com um outlier de R$ 1,45 milhão jogado na amostra: descartado no saneamento, riscado na tela, e o valor final não se moveu.

---

## 5. O que foi encontrado no caminho

### O motor da calculadora publicada

Está no Drive, pasta da calculadora. Constantes de produção, marcadas como *não alterar*, validadas contra o PDF da unidade MOVI 2107:

```js
SELIC = 14,75%   IPCA = 4,5%   ITBI = 4,5%   MOBILIA = R$ 30.000
SP = { preço 350.000 · diária 191 · ocupação 88% · comissão 25% · fixos 800 · valorização 4,12% }
SAC = { juros 10,65% · prazo 420 meses · seguro 0,00056 }
Price = 0,9% a.m. · 360 meses
STUDIO_NOI    = 191 × 0,88 × 365/12 × 0,75 − 800  =  R$ 3.034/mês
STUDIO_AVISTA = 350.000 × 1,045 + 30.000          =  R$ 395.750
```

### O estudo de mercado do interior

78 registros de bairro, anúncios reais de março e abril de 2026 — FipeZAP, Quinto Andar, Chaves na Mão e imobiliárias locais — agregados por mediana em 16 cidades e três tipologias, com preço, aluguel, valorização e vacância por célula. Aguaí e Campos do Jordão ficaram fora por premissa.

Conferi as 32 células cruzando o preço da especificação contra o yield do código publicado: **nenhuma diverge**.

### Operações reais, dos e-mails

MOVI Campo Belo un. 2107 R$ 307.200 · HUB Alto da Boa Vista un. 2605 R$ 292.800 · Nurban Ibirapuera R2V 36 m² R$ 354.524 · juros dos empreendimentos 11,70% a.a. · ITBI e registro 5% pelo banco · sistema SAC · financiamento até 90% do valor avaliado.

---

## 6. Erros meus, corrigidos

Registro aberto, porque três deles mudaram números que eu já tinha te passado.

| # | Erro | Efeito | Correção |
|---|---|---|---|
| 1 | Parser de milhar brasileiro | `"13.800"` virava `13,8` | regex de milhar |
| 2 | Parser de decimal | `0.056` virava `56`, a parcela explodia | milhar passa a exigir inteiro sem zero à esquerda |
| 3 | Premissas reconstruídas pela landing page | disse 14,2% e fluxo de −R$ 688 | trocado pelas constantes do motor |
| 4 | Parcela SAC | média de 12 meses, juros efetivos, sem seguro → R$ 3.007 contra R$ 3.308 do motor | parcela do 1º mês, juros nominais ÷ 12, com seguro |
| 5 | Conta de pedir mais caro | a curva dizia "não vende no ciclo" a +30% e a tabela ao lado dizia que compensava | ganho ponderado por chance de fechar; depois removida junto com os custos |
| 6 | Deduplicação de CSS linha a linha | removia a abertura de `@media print` repetida entre módulos, e as regras de impressão vazavam para a tela escondendo botões | concatenação integral das folhas |

Sobre a linha "quem paga a parcela" eu errei duas vezes antes de acertar. O número validado contra o QA do próprio motor é: **sobra de −R$ 274 por mês e 92% de cobertura** no primeiro ano.

---

## 7. Divergências em aberto

### Landing page contra o motor, no mesmo site

| | Landing page | Motor |
|---|---|---|
| Capital total | R$ 423.476 | R$ 395.750 |
| Renda líquida | R$ 2.640 | R$ 3.034 |

São duas bases de mobília rodando no mesmo domínio: a página implica cerca de R$ 55 mil entre mobília e custos, o motor usa R$ 30.000 mais 4,5% de ITBI. Um visitante que ler as duas percebe.

### "O hóspede paga a parcela"

A calculadora do site conclui **"o studio quase se paga sozinho"**, com 92% de cobertura e R$ 274 por mês saindo do bolso no começo. A landing page afirma que **o hóspede paga a parcela**. A página é mais forte que a conta da casa no primeiro ano. Em SAC a parcela cai todo mês e a cobertura passa de 100% por volta do ano 8 — a nota da própria calculadora explica isso.

Não é erro de conta: é escolha de qual cenário virou manchete. A decisão é sua.

### Especificação contra código

A especificação do motor diz mobília de R$ 60.000; o código publicado diz R$ 30.000. Usei o código. Alguém precisa decidir qual está certo.

### Três decisões do motor seguem marcadas como abertas na própria especificação

contagem de unidades · manchete antes ou depois da parcela · ITBI no interior.

### A calculadora do site abre em branco

quando o visitante chega por `wisekey.co` sem o `www`. Registrado como problema aberto desde 11/07.

---

## 8. O que ainda é estimativa minha

Não usar em negociação sem trocar por dado.

- **Todos os R$/m² por bairro** — 23 regiões na aba de compra, 17 na de venda. O estudo real é por cidade e tipologia em preço mediano; converter num no outro exige a área mediana de cada célula, que a base não traz.
- **Terreno em R$/m² e CUB por padrão**, inclusive o Jardim Amélia, que acrescentei com número inventado.
- **Fatores de homogeneização** do PTAM — em faixas usuais de mercado, mas não calibrados na região.
- **Prêmios dos diferenciais** da tela rápida — os nove pesos e o teto de 15%.
- **Curva de prazo** — ancorada na vacância da cidade, sem dado real de tempo médio de venda. Por isso o campo de meses é editável.
- **Diária e ocupação por bairro** na aba de compra. Só o benchmark de São Paulo está confirmado: R$ 191 e 88%.

---

## 9. Decisões tomadas, para você confirmar ou desfazer

- **As telas de avaliação não têm custo embutido.** Corretagem, imposto sobre ganho, quitação, IPTU, condomínio e custo de capital parado saíram da leitura de valor e do PTAM. Avaliar é dizer quanto vale; o resto é a conversa seguinte.
- **A aba Comprar ficou intacta.** Ela analisa investimento, não avalia imóvel, e retorno sem custo não existe.
- **As páginas não estão linkadas no site** e estão com `noindex`. Se a ideia for usar como isca de captação, é um link no menu — mas aí eu esconderia o teto de compra, que é a sua régua de negociação.

---

## 10. O que falta buscar

- **Planilhas `Apartamentos`, `ABNB 706` e `Apto 706`** — anexos XLSX no e-mail, com diária, ocupação e receita reais.
- **`data.py` e `calculator.py`** — os 78 bairros individuais por trás das medianas.
- **Curadoria de Imóveis** e os cinco books dos empreendimentos.
- **Estudo do Reserva Boa Vista** — é o que fecha o cenário do lote da página, de R$ 1.025.533 para 250 m² de terreno mais 159 m² de obra. Não está no e-mail.
- **Fonte e data de coleta por comparável** — o checklist do PTAM exige, e a calculadora ainda não captura. São duas colunas a mais na amostra.
- **Histórico de tempo de anúncio e preço de fechamento** de vocês — transforma a curva de prazo de modelo em dado.

---

## 11. Commits

```
47406cf  Adiciona calculadora de avaliação de imóveis
1a75049  Adiciona calculadora de avaliação para o lado do vendedor
26ccda2  Corrige premissas de financiamento com os dados reais das operações
79f752c  Calibra a calculadora pela base de cálculo publicada no site
513edad  Refaz a avaliação do vendedor na metodologia do PTAM
9070440  Unifica as duas calculadoras e documenta a base em calculadora.html
863ecae  Substitui premissas inventadas pelas constantes do motor real
8b91b0b  Alinha a parcela SAC ao motor e corrige o parser de decimais
2e28718  Adiciona ideia de valor em dois cliques, com a mediana real de mercado
d6c77a2  Transforma a ideia de valor em estudo para apresentar ao proprietário
62ffc00  Tira os custos das telas de avaliação
0587805  Adiciona os diferenciais do imóvel à leitura de valor
```

---

## 12. Como regenerar a página única

`calculadora.html` é montado a partir dos três módulos. Ao editar qualquer um deles, remonte: os IDs em conflito do módulo de venda recebem prefixo `v-`, cada script roda em escopo próprio, e as folhas de estilo são concatenadas inteiras — **nunca deduplicadas linha a linha**, sob pena de quebrar os blocos `@media print`.

---

*Wisekey Estrategia e Assessoria Ltda · CNPJ 58.501.287/0001-13 · Responsável técnico: Raphael Piotto Cardoso · CRECI/SP 319841-F*
