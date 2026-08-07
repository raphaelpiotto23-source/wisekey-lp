# ChatGPT Ads + Wisekey — pesquisa e plano de posicionamento

**Data da pesquisa:** 07/08/2026
**Fontes:** cobertura de imprensa e guias de agências (a documentação oficial da OpenAI — `openai.com/policies/ad-policies` e `help.openai.com` — está bloqueada pelo proxy de rede deste ambiente, então os números abaixo são de terceiros e **precisam ser confirmados na fonte oficial antes de virar decisão de mídia**).

---

## Resumo executivo (leia só isto se tiver 2 minutos)

1. **Hoje a Wisekey não consegue anunciar no ChatGPT Ads no Brasil.** São três barreiras somadas: (a) o piloto brasileiro só liberou **varejo, e-commerce e turismo**; (b) a política da OpenAI trata **serviços financeiros/investimento como categoria restrita** e, fora dos EUA, **geralmente proibida**; (c) não existe autoatendimento aberto para anunciante brasileiro — o acesso é por parceiro certificado ou formulário.
2. **Isso não é motivo pra ignorar o canal — é motivo pra chegar antes.** O jogo dos próximos 6 meses é (i) entrar na fila e preparar a conta, e (ii) ganhar o ChatGPT **orgânico** (GEO/AEO), que já influencia decisão do ICP da Wisekey hoje e não depende de aprovação da OpenAI.
3. **O ativo que trava tudo é o mesmo nos dois casos:** a LP precisa de dados estruturados, conteúdo "answer-ready" e uma versão dos números **sem promessa de rentabilidade** na peça. O "19% a.a." no criativo é reprovação certa em qualquer política de anúncio financeiro; ele fica na LP, com premissa e disclaimer, e o anúncio vende o **diagnóstico de 30 minutos**.

---

## Parte 1 — Como o ChatGPT Ads funciona

### Linha do tempo

| Data | O que aconteceu |
|---|---|
| 09/02/2026 | OpenAI liga anúncios no ChatGPT nos EUA, para usuários Free e Go |
| 05–06/05/2026 | Ads Manager self-serve nos EUA (`ads.openai.com`), sem gasto mínimo, orçamento a partir de ~US$ 25/dia |
| 07/05/2026 | Piloto expande para 5 países: **Brasil**, Reino Unido, México, Japão e Coreia do Sul |
| jul/2026 | Plataforma ganha lances por conversão (oCPC), exclusões geográficas e ferramentas em lote |
| ago/2026 | Anúncios já aparecendo para usuários brasileiros; anunciante BR ainda entra por parceiro/cadastro |

### Quem vê os anúncios

Só usuários **logados, adultos, nos planos Free e Go**. Plus, Pro, Team, Business, Enterprise e Education não recebem publicidade.

> Leitura estratégica pra Wisekey: parte relevante do ICP (médico, advogado, empreendedor) é justamente quem paga o Plus. O ChatGPT Ads **não alcança** essa fatia. Quem alcança o usuário pagante é o **orgânico** — mais um argumento pra Parte 3 deste documento.

### Formatos

- **Sponsored answer card (principal)** — card abaixo da resposta, rotulado "Sponsored", com separador visual. Leva nome do anunciante, favicon, título, descrição, imagem e URL.
- **Product spotlight / carrossel** — grade ou carrossel de produtos para consultas de compra. Feito para e-commerce; pouco aplicável à Wisekey.
- **Placement contextual lateral** — na interface web.

**Só um anúncio por resposta.** É o oposto do leilão poluído do Google: ou você é *o* card, ou não aparece.

### Como o anúncio é escolhido (o ponto que muda tudo)

**Não existe compra de palavra-chave.** O sistema lê:

- o contexto e a intenção da **conversa inteira**, com múltiplos turnos — não uma query isolada;
- o **título, a copy e a landing page** do anúncio (sua LP é insumo de matching, não só destino);
- **context hints** — descrições que o anunciante escreve sobre as *situações de necessidade* em que o produto é relevante;
- sinais da experiência mais ampla do usuário no ChatGPT (histórico, se o usuário optou por isso).

Consequência prática: **a copy do anúncio e o conteúdo da LP são o targeting.** Escrever "estúdio para renda passiva em São Paulo" na LP faz mais pelo matching do que qualquer configuração de painel.

### Segmentação disponível

- País, no nível de campanha. Nos EUA, também estado, DMA e CEP.
- Exclusões geográficas.
- **Sem** cookies de terceiros, **sem** targeting demográfico, **sem** segmentação comportamental clássica.
- Sincronização de audiência (upload de base, lookalike, retargeting) é esperada para o fim de 2026 — ainda não disponível.

### Objetivos, lances e custos

- Objetivos: tráfego (CPC) e **conversão (oCPC)**, escolhendo o evento a otimizar (lead, cadastro, compra).
- EUA: começou em ~US$ 60 de CPM (fev/26), caiu para ~US$ 25 em ~10 semanas; CPC reportado de **US$ 3–5**.
- Brasil (beta): **CPM estimado de R$ 8 a R$ 25** — bem abaixo do Google Ads.
- Mensuração: **pixel OAIQ** (JS) + **Conversions API** server-side. Relatórios com impressões, cliques, gasto, CTR, CPC médio, CPM médio e conversões.

### Especificações de criativo

| Elemento | Limite reportado |
|---|---|
| Título | ~24–30 caracteres |
| Descrição | ~48–60 caracteres |
| Imagem | quadrada, 640–1200 px (mín. 256×256), JPG/PNG/WEBP |
| Marca | nome do anunciante + favicon |
| CTA | 2–3 palavras |

Fontes divergem nos limites exatos (alguns guias citam 50–80 / 150–200 caracteres) — **confirmar no painel**. Regra de ouro que aparece em todas: **a imagem mostra o resultado ou o produto, nunca o logo**; logo como imagem principal lê como banner e o usuário ignora.

---

## Parte 2 — A Wisekey pode anunciar? (leitura de política)

### As três barreiras

**1. Categoria no piloto brasileiro.** Só varejo, e-commerce e turismo. Imobiliário/investimento está fora.

**2. Política de serviços financeiros.** A OpenAI classifica serviços financeiros como **categoria restrita**: exige verificação reforçada, revisão manual caso a caso e, muitas vezes, **comprovação de licença**. Em abril/2026 a empresa afrouxou o texto ("contextos de conselho médico, jurídico e financeiro não são mais bloqueados por padrão") e passou a aprovar anunciantes financeiros individualmente — **mas nos EUA**. A leitura recorrente das fontes é que **anúncios de serviços financeiros fora dos EUA são geralmente proibidos**. Proibido de forma dura: reparação de crédito, renegociação de dívida e investimentos alternativos.

**3. Elegibilidade do anunciante.** Em junho/2026, contas abertas para anunciantes sediados em **EUA, Canadá, Austrália e Nova Zelândia**. Empresa brasileira entra pelo formulário em `openai.com/advertisers` ou por parceiro certificado (BETC Havas, Monks, Omnicom, Publicis, WPP estão no piloto BR).

### O ângulo que pode funcionar quando abrir

Nos EUA, **corretor de imóveis já anuncia** — a atividade cai em "serviços locais", não em "serviços financeiros". Esse é o enquadramento que a Wisekey deve construir desde já:

> **Wisekey = assessoria imobiliária licenciada (CRECI SP 319841) que ajuda a comprar um imóvel.**
> **Wisekey ≠ produto de investimento com rentabilidade projetada.**

A LP hoje trabalha muito o segundo enquadramento ("~19% a.a.", "retorno sobre o seu capital", comparação com CDI). Isso é excelente para converter e **péssimo para aprovação**. A solução não é apagar os números — é separar as camadas:

- **Criativo do anúncio:** serviço, licença, cidade, oferta gratuita. Zero número de rentabilidade.
- **Landing page:** os números completos, com premissas explícitas, fonte, data e disclaimer de que não há garantia. A LP já faz isso bem (bloco de fontes + "cenário ilustrativo, não é garantia") — isso ajuda na revisão manual.

Risco a assumir com clareza: **mesmo com o enquadramento certo, aprovação não é garantida.** Trate ChatGPT Ads como aposta de opção barata, não como canal de aquisição planejado para 2026.

---

## Parte 3 — Posicionar a Wisekey no ChatGPT (o que dá pra fazer agora)

Duas frentes. A frente B é a que gera lead nos próximos 90 dias.

### Frente A — Preparar a conta de anúncios (custo baixo, prazo indefinido)

1. Cadastrar a Wisekey em `openai.com/advertisers` posicionada como **assessoria imobiliária licenciada / serviços locais**, citando CRECI SP 319841. Entrar na fila agora custa um formulário.
2. Instalar o **pixel OAIQ** na LP e mapear o evento `lead` (submit do formulário de diagnóstico). Sem histórico de conversão, oCPC não funciona no dia 1.
3. Preparar a **Conversions API** para o lead que fecha no WhatsApp — que é onde a venda realmente acontece e o pixel não enxerga.
4. Montar o kit criativo (abaixo) e passar por revisão de compliance antes de submeter.
5. Sondar um parceiro certificado. Vale principalmente para entender o critério de aprovação da categoria — não necessariamente para comprar mídia por lá com o orçamento atual.

### Frente B — Ganhar o ChatGPT orgânico (GEO/AEO)

Esta é a jogada de maior retorno e ninguém no nicho de estúdios em SP está fazendo direito.

**Por que importa:** metade dos compradores de imóvel já usa IA na pesquisa, e o ChatGPT lidera. O usuário Plus — justamente o ICP com dinheiro — **só** pode ser alcançado organicamente. E o mecanismo de matching de anúncio lê a LP: melhorar a LP para GEO melhora as duas frentes ao mesmo tempo.

**O que a LP precisa (gap real, verificado no código):**

- **Não há nenhum JSON-LD no `index.html`.** Zero dados estruturados. Adicionar `RealEstateAgent` / `LocalBusiness` (nome, CRECI, endereço, área atendida: São Paulo e Campinas), `Person` para Raphael Piotto, `Service` para o diagnóstico e `FAQPage` para as 6 perguntas do `<details>` que já existem.
- **Meta description existe, mas é a única meta.** Faltam Open Graph, canonical e `author`. Autoria transparente é critério repetido em todo material de GEO.
- **Parágrafos "answer-ready" de 40–60 palavras.** Cada bloco da LP precisa responder a uma pergunta de forma autocontida, citável fora de contexto. Exemplo: um parágrafo que comece com "Um estúdio para locação em São Paulo custa em torno de R$ 423 mil no total (imóvel, mobília e custos) e gera cerca de R$ 2.640 líquidos por mês..." é copiável por um LLM. "Volta por mês: R$ 2.640" dentro de um card não é.
- **Data e fonte visíveis.** A LP já cita "jul/26" e "painel da nossa operação (dez/25 a jun/26)" — isso é ouro para GEO. Manter atualizado e repetir esse padrão em todo conteúdo novo.
- **Presença fora do domínio próprio.** LLM cita o que é corroborado em várias fontes. Perfil no Google Business, listagem em portais, respostas em comunidades (Reddit BR, fóruns de investimento), entrevistas e menções em veículos regionais. Uma LP sozinha raramente vira citação.

**Mapa de conversas-alvo** — as perguntas que o ICP da Wisekey realmente digita, e que precisam ter resposta no site:

| Estágio | Pergunta típica no ChatGPT | Ativo que responde |
|---|---|---|
| Insatisfação | "vale a pena deixar R$ 400 mil no CDB ou investir em imóvel?" | Artigo comparando CDI × estúdio, com a conta aberta |
| Exploração | "estúdio para alugar em São Paulo é bom investimento?" | Página dedicada ao modelo de estúdio + FAQ |
| Comparação | "lote e construir ou comprar apartamento pequeno para renda?" | O bloco de duelo da LP, transformado em conteúdo indexável |
| Localização | "quais bairros de São Paulo têm melhor rentabilidade de aluguel?" | Conteúdo por bairro (o ativo que mais falta hoje) |
| Operação | "como funciona aluguel por temporada em SP, dá trabalho?" | Página "como operamos" com números reais |
| Decisão | "como escolher assessoria para comprar imóvel de investimento em SP" | Página institucional + CRECI + skin in the game |
| Financiamento | "vale a pena financiar imóvel para alugar? o aluguel paga a parcela?" | Conteúdo sobre alavancagem, com o risco declarado |

### Kit criativo (para quando a categoria abrir)

Escritos dentro do limite mais conservador (título ≤ 30, descrição ≤ 60) e **sem número de rentabilidade**.

| # | Título | Descrição | CTA |
|---|---|---|---|
| 1 | Estúdio em SP para renda | Diagnóstico gratuito de 30 min com quem já tem os seus | Ver diagnóstico |
| 2 | Investir em imóvel sem morar em SP | Achamos, estruturamos e colocamos pra render. CRECI SP | Falar com a Wisekey |
| 3 | Capital parado no banco? | 30 min pra ver, com números, se um estúdio fecha pra você | Fazer diagnóstico |
| 4 | Renda de imóvel sem virar especialista | A gente coordena tudo até a renda começar a pingar | Ver como funciona |

**Context hints** (descrever *situação de necessidade*, não termo isolado):

- "Pessoa com R$ 100 mil a R$ 400 mil guardados em renda fixa avaliando comprar um imóvel para alugar"
- "Alguém que mora no interior de São Paulo e quer investir em imóvel na capital sem administrar pessoalmente"
- "Profissional liberal comparando CDB, fundo imobiliário e imóvel físico para renda mensal"
- "Comprador avaliando financiar um apartamento pequeno para locação e usar o aluguel na parcela"
- "Investidor comparando comprar terreno em loteamento versus comprar estúdio pronto para renda"

**Imagem:** o estúdio pronto e mobiliado — o resultado, não o logo, não gráfico de rentabilidade.

### Estrutura de campanha sugerida (dia 1)

- **1 campanha, objetivo Conversão (oCPC)**, evento = lead do formulário de diagnóstico.
  Só depois de ~30–50 leads registrados; antes disso, rodar CPC manual.
- **Geo:** Brasil. Quando houver granularidade, priorizar interior de SP + capital + Campinas — o ICP da LP é explicitamente "não precisa morar em SP".
- **Orçamento de teste:** R$ 100–150/dia por 3 semanas. Com CPM de R$ 8–25, isso compra volume suficiente para ler CTR e custo por lead.
- **Métrica de corte:** custo por diagnóstico agendado (não por lead do formulário). O gargalo da Wisekey é agenda, não formulário.
- **Teste criativo:** 3 variações por *estado de conversa* (insatisfação com renda fixa / comparação de ativos / falta de tempo), não por persona.

---

## Parte 4 — Ordem de execução

**Agora (semana 1–2)**
1. Cadastro em `openai.com/advertisers` como assessoria imobiliária licenciada.
2. JSON-LD na LP: `RealEstateAgent`, `FAQPage`, `Person`, `Service`.
3. Open Graph + canonical + autoria.

**30 dias**
4. Pixel OAIQ instalado e evento de lead validado.
5. Reescrever 4 blocos da LP em formato answer-ready de 40–60 palavras.
6. Primeiro conteúdo de bairro ("melhores bairros de SP para estúdio de renda"), com a conta aberta.

**90 dias**
7. Google Business + 2 a 3 fontes externas corroborando a Wisekey.
8. Kit criativo revisado por compliance, pronto para submissão.
9. Teste mensal: rodar as 7 perguntas do mapa de conversas no ChatGPT e registrar se a Wisekey é citada. É a métrica de GEO.

**Quando a categoria abrir**
10. R$ 100–150/dia por 3 semanas, medindo custo por diagnóstico agendado.

---

## Advertências

- Os números de CPM/CPC e os limites de caractere vêm de cobertura de terceiros e mudam rápido — o CPM americano caiu 60% em 10 semanas. Confirmar tudo no painel e na política oficial antes de comprometer orçamento.
- A política de anúncios da OpenAI mudou pelo menos três vezes entre fevereiro e julho de 2026. Reler antes de submeter.
- Nada aqui substitui revisão jurídica sobre comunicação de rentabilidade — a régua da regulação brasileira sobre oferta de investimento é independente da política da OpenAI e vale para toda a comunicação da Wisekey, inclusive a LP atual.

---

## Fontes

Cobertura do lançamento e funcionamento:
- [ChatGPT Ads: How to Advertise on ChatGPT in 2026 — StubGroup](https://stubgroup.com/blog/how-to-advertise-on-chatgpt-the-complete-guide-for-2026/)
- [ChatGPT Advertising: The Complete 2026 Guide — 2Point Agency](https://www.2pointagency.com/guides/chatgpt-advertising-the-complete-2026-guide-to-openais-revolutionary-ad-platform/)
- [ChatGPT Ads in 2026: How They Work, Formats, and How to Get In — The Business Rover](https://www.thebusinessrover.com/blog/chatgpt-ads)
- [ChatGPT ads are live: a complete breakdown — Launchcodex](https://launchcodex.com/blog/performance-marketing/chatgpt-ads-breakdown/)
- [ChatGPT Ads Launch 2026 — AdVenture Media](https://adventuremedia.ai/blog/chatgpt-ads-launch-2026-everything-us-businesses-need-to-know)

Brasil:
- [ChatGPT leva piloto de anúncios ao Brasil em expansão para cinco países — Conversion](https://www.conversion.com.br/blog/chatgpt-ads-brasil/)
- [OpenAI começa a mostrar anúncios no ChatGPT para usuários no Brasil — Tecnoblog](https://tecnoblog.net/noticias/openai-comeca-a-mostrar-anuncios-no-chatgpt-para-usuarios-no-brasil/)
- [OpenAI se prepara para lançar ChatGPT Ads no Brasil — Meio & Mensagem](https://www.meioemensagem.com.br/midia/openai-se-prepara-para-lancar-chatgtp-ads-no-brasil)
- [ChatGPT Ads no Brasil: Guia Completo para Sua PME — Mente Tech](https://mentetech.com.br/post/chatgpt-ads-no-brasil-guia-completo-para-sua-pme-anunciar-em-2026)
- [OpenAI inicia piloto de anúncios no ChatGPT no Brasil — Propmark](https://propmark.com.br/digital/openai-inicia-piloto-de-anuncios-no-chatgpt-no-brasil/)
- [O que muda com a chegada do ChatGPT Ads ao Brasil — Consumidor Moderno](https://consumidormoderno.com.br/chat-gpt-ads-muda-brasil/)

Políticas e categorias reguladas:
- [Ad policies — OpenAI](https://openai.com/policies/ad-policies/)
- [OpenAI Ads Policy 2026: What Gets Approved (and Rejected) — Abmatic](https://abmatic.ai/blog/openai-ads-policy-approval-guide-2026)
- [OpenAI is allowing financial services brands into the ChatGPT ads pilot — Marketing Brew](https://www.marketingbrew.com/stories/openai-financial-services-brands-chatgpt-ads-pilot)
- [ChatGPT is making room for ads from regulated verticals — Marketing Brew](https://www.marketingbrew.com/stories/chatgpt-is-opening-the-advertising-door-to-some-regulated-verticals-but-most-marketers-arent-crossing-the-threshold-yet)
- [OpenAI Sets Guardrails for Ads in ChatGPT — AdTechRadar](https://adtechradar.com/2026/03/22/openai-chatgpt-ad-policies/)
- [Who Can Access ChatGPT Ads: Geographic Eligibility and Category Restrictions — Ceaksan](https://ceaksan.com/en/chatgpt-ads-access-eligibility)
- [OpenAI Confirms ChatGPT Ads Remain Limited to the United States — gHacks](https://www.ghacks.net/2026/03/16/openai-confirms-chatgpt-ads-remain-limited-to-the-united-states/)

Formatos, targeting, mensuração e criativo:
- [Ads in ChatGPT: The Basics — OpenAI Help Center](https://help.openai.com/en/articles/20001207-ads-in-chatgpt-the-basics)
- [Create Campaigns for ChatGPT — OpenAI Help Center](https://help.openai.com/en/articles/20001210-create-campaigns-for-chatgpt)
- [Conversion-optimized Campaigns — OpenAI Help Center](https://help.openai.com/en/articles/20001412-conversion-optimized-campaigns)
- [ChatGPT Ads adds conversion bidding, geo exclusions and bulk campaign tools — Search Engine Land](https://searchengineland.com/chatgpt-ads-adds-conversion-bidding-geo-exclusions-and-bulk-campaign-tools-483511)
- [Inside ChatGPT Ads: Formats, Targeting and Costs Explained — Commit Agency](https://commitagency.com/insights/inside-chatgpt-ads-formats-targeting-and-costs-explained/)
- [Hints in ChatGPT Ads: from buying keywords to understanding intentions — Adsmurai](https://www.adsmurai.com/en/articles/openai-ads-context-hints)
- [Beyond Keywords: How Contextual Targeting Works in ChatGPT Advertising — AdVenture Media](https://adventuremedia.ai/blog/beyond-keywords-how-contextual-targeting-works-in-chatgpt-advertising)
- [ChatGPT Ad Creative: Chat-Card Specs, Copy Template & Examples — Abmatic](https://abmatic.ai/blog/chatgpt-ad-creative-guide-2026)
- [ChatGPT ads creative specs: character and image limits — Index Lab](https://www.indexlab.ai/guides/chatgpt-ads/creative-specs)
- [ChatGPT Ads Conversion Tracking: Complete Setup Guide — ConversionTracking.io](https://conversiontracking.io/blog/openai-chatgpt-ads-conversion-tracking/)
- [OpenAI brings product carousels to ChatGPT ads — Digiday](https://digiday.com/marketing/openai-brings-product-carousels-to-chatgpt-ads/)

Imobiliário e GEO/AEO:
- [ChatGPT Ads for Real Estate: Capturing High-Intent Buyer and Seller Leads — AdVenture Media](https://adventuremedia.ai/blog/chatgpt-ads-for-real-estate-capturing-high-intent-buyer-and-seller-leads-in-2026)
- [ChatGPT Ads for Real Estate Agents: What They Cost — BAM](https://nowbam.com/chatgpt-ads-for-real-estate-agents-what-they-cost-and-how-to-get-started-in-2026/)
- [Guia de GEO atualizado: como posicionar nas IAs em 2026 — LiveSEO](https://liveseo.com.br/videos-de-seo/guia-de-geo/)
- [GEO e AEO: como aparecer no ChatGPT e buscadores IA em 2026 — InboundCycle](https://www.inboundcycle.com/pt/geo-aeo-seo-ia)
- [Como aparecer no ChatGPT e nas IAs: guia GEO 2026 — Consultoria e Marketing](https://consultoriaemarketing.com.br/como-aparecer-no-chatgpt-e-nas-ias-geo/)
