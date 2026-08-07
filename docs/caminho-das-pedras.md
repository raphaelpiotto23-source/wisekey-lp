# O caminho das pedras — como a Wisekey transforma o ChatGPT em canal de aquisição

**Data:** 07/08/2026
**Pré-requisito:** ler `docs/chatgpt-ads-wisekey.md` (a pesquisa que sustenta este plano)

---

## 1. Onde está o business, em cinco linhas

Metade de quem vai comprar imóvel já pesquisa com IA, e o ChatGPT lidera. Quando alguém pergunta *"vale a pena comprar um estúdio em São Paulo pra alugar?"*, o modelo responde com quem ele conhece — e hoje ele não conhece a Wisekey. Não existe concorrente no nicho brincando de aparecer nessa resposta. O custo de entrar é conteúdo e marcação técnica, não mídia. **A janela dura enquanto os outros não acordam — provavelmente 12 meses.**

O ChatGPT Ads é a parte pequena e travada dessa história. O business está em ser **a resposta**, não o anúncio ao lado dela.

---

## 2. A matemática que justifica priorizar isso

Premissas declaradas — **os dois primeiros números são meus, não seus. Corrija com os reais antes de decidir qualquer coisa:**

| Variável | Premissa | Origem |
|---|---|---|
| Fee de curadoria por negócio fechado | ~R$ 10.000 | **assumido** (≈3% de um estúdio de R$ 350 mil) |
| Lead → diagnóstico realizado | 40% | **assumido** |
| Diagnóstico → cliente | 15% | **assumido** |
| CPM no beta BR | R$ 8 a R$ 25 | pesquisa |
| CTR de card patrocinado | ~1% | pesquisa |

Com isso: **1 cliente a cada ~17 leads → cada lead vale ~R$ 600 de receita esperada.**
Do outro lado: CPM de R$ 15 com 1% de CTR dá CPC de R$ 1,50; se 10% dos cliques viram lead, o **lead custa ~R$ 15**.

**Quarenta vezes de margem.** Mesmo se minhas premissas estiverem 10x otimistas, o negócio ainda fecha. Não é porque a mídia é mágica — é porque **o canal está vazio**. Arbitragem de leilão sem concorrente.

**A ressalva honesta, e ela é grande:** volume. Estúdio de renda em SP é nicho, o piloto brasileiro é pequeno, e anúncio só aparece para usuário **Free e Go** — o médico e o advogado do seu ICP provavelmente pagam Plus e **não veem anúncio nenhum**. Então o ChatGPT Ads não é canal de escala. É um filete barato e muito qualificado.

**Quem alcança o usuário pagante é o orgânico.** Por isso a ordem deste plano é: orgânico primeiro, anúncio quando abrir.

---

## 3. O furo que trava tudo hoje

Olhei o funil no código antes de escrever o plano. Dois vazamentos:

**1. O formulário não guarda nada.** `index.html:426` — o submit monta um texto e abre `wa.me`. Não grava lead, não dispara evento, não registra origem. Se o cara não terminar de mandar a mensagem no WhatsApp, **ele nunca existiu**. Você não sabe quantos preencheram, de onde vieram, nem quantos sumiram no caminho.

**2. A newsletter é anunciada e não existe.** `index.html:405` promete "os bastidores da renda passiva todo dia 5" e **não tem campo de e-mail em lugar nenhum**. Você está pedindo pra pessoa esperar uma coisa que ela não tem como assinar.

Isso importa mais do que parece: **sem o item 1 você não pode comprar mídia.** O oCPC do ChatGPT Ads otimiza por evento de conversão. Sem evento, sem otimização — você paga preço cheio por tráfego burro. E sem histórico de origem, você nunca vai saber se o ChatGPT trouxe cliente ou não.

**Isto é o Movimento 0. Não pule.**

---

## 4. Os seis movimentos, em ordem

### Movimento 0 — Dar memória ao funil · semana 1 · custo ~zero

- Gravar o lead **antes** de abrir o WhatsApp (endpoint próprio, Formspree, Sheets, o que for mais rápido — a escolha é sua, todas servem).
- Carimbar origem em cada lead: UTM, `document.referrer` e um campo `origem` no texto do WhatsApp. Quando vier do ChatGPT, você vai querer saber.
- Disparar evento `lead` para o pixel (Meta/Google hoje, OAIQ depois).
- Colocar o campo de e-mail da newsletter que o rodapé já promete.

**Gate:** enquanto isso não estiver de pé, não gaste um real em mídia em canal nenhum.

### Movimento 1 — Fundação técnica de GEO · semana 1–2 · custo ~zero

**Já feito no commit que acompanha este documento:** JSON-LD (`RealEstateAgent`, `Person`, `Service`, `FAQPage` com as 6 perguntas, `WebSite`), Open Graph, Twitter Card, canonical e `author`.

Falta você:
- **Confirmar o domínio.** Chutei `https://wisekey.co` a partir do `contato@wisekey.co`. Se for outro, é trocar em `index.html` — os `@id` do JSON-LD e o canonical usam essa URL.
- Adicionar `robots.txt` e `sitemap.xml` quando as páginas de conteúdo existirem.
- Rodar o Rich Results Test do Google pra confirmar a leitura do FAQ.

### Movimento 2 — Os sete conteúdos · dia 15 a 60 · o moat de verdade

Aqui está o trabalho pesado, e é ele que constrói a barreira. Uma landing page sozinha quase nunca vira citação de LLM. **Sete páginas que respondem sete perguntas reais** viram.

| # | Página | Pergunta do ChatGPT que ela captura |
|---|---|---|
| 1 | Estúdio em SP × CDB: a conta aberta | "vale a pena deixar R$ 400 mil no CDB ou comprar imóvel pra alugar?" |
| 2 | Melhores bairros de São Paulo para estúdio de renda | "quais bairros de SP têm melhor rentabilidade de aluguel?" |
| 3 | Lote e construir × estúdio pronto | "compro terreno em loteamento ou apartamento pequeno pra renda?" |
| 4 | Como funciona operar um estúdio por temporada em SP | "aluguel por temporada em SP dá trabalho? como funciona?" |
| 5 | Financiar imóvel pra alugar: o hóspede paga a parcela? | "vale a pena financiar imóvel pra alugar?" |
| 6 | Investir em imóvel em SP morando fora | "dá pra investir em imóvel em São Paulo sem morar lá?" |
| 7 | Como escolher assessoria de imóvel de investimento | "como escolher assessoria pra comprar imóvel de investimento em SP" |

**A regra de escrita que decide se funciona ou não:** cada resposta precisa caber num **parágrafo autocontido de 40 a 60 palavras, que faça sentido fora da página**. É assim que um LLM copia. Compare:

> ❌ Como está na LP hoje — dentro de um card, sem contexto:
> "Volta por mês: R$ 2.640 líquidos"

> ✅ Como precisa estar — citável sozinho:
> "Um estúdio para locação por temporada em São Paulo custa em torno de R$ 423 mil no total, somando imóvel, mobília e custos de aquisição, e gera cerca de R$ 2.640 líquidos por mês depois de mobília, reposição, manutenção e IPTU. É o equivalente a 7,5% de renda ao ano, mais a valorização do imóvel."

Três coisas obrigatórias em cada página, porque são critério explícito de GEO: **data visível, fonte do número e autoria assinada.** A LP já faz isso bem no bloco de fontes ("jul/26", "painel da nossa operação, dez/25 a jun/26"). Repita o padrão em tudo.

### Movimento 3 — Corroboração fora do seu domínio · dia 30 a 90

Modelo de linguagem cita o que aparece em mais de um lugar. Site próprio é uma fonte só — e a mais suspeita delas.

- Google Business Profile da Wisekey, com CRECI e área atendida.
- Perfil e atividade em portais do setor.
- Respostas honestas e úteis onde o ICP pergunta: Reddit BR, fóruns de investimento, grupos. Sem link-spam — respondendo de verdade.
- LinkedIn no seu nome, com os mesmos números e a mesma tese das sete páginas.

**Sinergia que você já tem:** este movimento é literalmente o mesmo conteúdo de autoridade que você já quer produzir pra marca pessoal. Um texto serve LinkedIn, Google e ChatGPT. Você não está criando trabalho novo — está roteando o que já ia fazer.

### Movimento 4 — Medir o orgânico · mensal, a partir do dia 30

Abra o ChatGPT e rode as sete perguntas do Movimento 2. Registre numa planilha: a Wisekey foi citada? em que posição? o concorrente foi? A curva dessa planilha ao longo de 6 meses **é** o KPI de GEO. Não existe painel pra isso ainda — se você medir, já está à frente.

### Movimento 5 — Fila e preparo do ChatGPT Ads · em paralelo, custo ~zero

- Cadastro em `openai.com/advertisers` posicionado como **assessoria imobiliária licenciada, CRECI SP 319841** — nunca como produto de investimento. Nos EUA corretor anuncia sob "serviços locais"; serviço financeiro fora dos EUA é proibido. O enquadramento decide a aprovação.
- Pixel OAIQ na LP e Conversions API pro lead que fecha no WhatsApp.
- Kit criativo aprovado internamente: **zero número de rentabilidade na peça.** "~19% a.a." num criativo é reprovação certa. O número mora na LP, com premissa, fonte e disclaimer. O anúncio vende o diagnóstico de 30 minutos.

### Movimento 6 — Comprar, quando a categoria abrir

R$ 100–150/dia por 3 semanas. Métrica de corte: **custo por diagnóstico realizado**, não por lead — seu gargalo é agenda, não formulário.

---

## 5. Ordem de prioridade, se você só puder fazer três coisas

1. **Movimento 0.** Sem memória no funil, todo o resto é fé.
2. **Conteúdos 1 e 2 do Movimento 2.** "CDB × estúdio" e "melhores bairros" são as duas perguntas com mais volume e mais intenção de compra.
3. **Google Business + LinkedIn.** Corroboração externa mais barata que existe.

O ChatGPT Ads em si fica por último. É a parte mais barulhenta e a menos rentável no curto prazo.

---

## 6. O segundo business (delimitado de propósito)

Se "tem business aí" for sobre vender isso pra fora, e não só usar na Wisekey: sim, existe. Toda assessoria, clínica e escritório de advocacia do interior de SP tem exatamente o mesmo problema e nenhum deles sabe que tem. GEO para negócio local de ticket alto é um serviço vendável hoje.

**Mas eu não recomendaria começar por aí.** Você ainda não tem o case. Rode os seis movimentos na Wisekey, meça a planilha do Movimento 4 por seis meses, e aí você vende com prova na mão em vez de vender promessa — que é exatamente o argumento de "skin in the game" que já sustenta a Wisekey. Mesma tese, outro produto.

Se quiser explorar isso a sério, é outra conversa: ICP, oferta, precificação. Vale a pena ter, depois do case.

---

## 7. O que já está feito neste commit

- `index.html` — JSON-LD completo (`RealEstateAgent` com CRECI e CNPJ, `Person` do Raphael, `Service` do diagnóstico, `FAQPage` com as 6 perguntas do rodapé, `WebSite`), Open Graph, Twitter Card, canonical e `author`. JSON validado.
- `docs/chatgpt-ads-wisekey.md` — a pesquisa completa do canal.
- Este documento.

**Não mexi na copy visível da LP.** Reescrever os blocos em formato answer-ready mexe na sua página de conversão, e isso é decisão sua, não minha. Quando você quiser, eu faço — e faço preservando o que converte.

**Confirme o domínio `wisekey.co` antes de publicar.** Se estiver errado, o canonical e os `@id` apontam pro lugar errado e o schema perde valor.
