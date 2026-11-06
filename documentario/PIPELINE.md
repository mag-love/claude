# Doc Dagoma — pipeline de agentes

Contexto comum. Todo agente lê este arquivo e `documentario/MEMORIA.md` antes de agir. Nada de repetir pesquisa ou transcrição que já está registrada na memória.

## Norte criativo (prioridade agora)

1. **Narrativa bem amarrada.** Cada cena precisa de um porquê e levar à próxima. Se sai e o filme não sente falta, corta.
2. **Entrevistas boas de assistir e de ouvir.** Falas fortes, ritmo vivo, áudio limpo. Entrevista que cansa perde o espectador.
3. **Imagem de cobertura conta a história.** Todo B-roll ilustra o que está sendo dito naquele momento. Imagem bonita que não conversa com a fala sai.

As demais regras vão sendo definidas durante o processo.

## Onde as coisas vivem

- Central no Notion (norte, bíblia, regras): https://app.notion.com/p/40932fc5888a81a3b68ac3d5fac98fa2
- Relatório do produtor (página reescrita a cada checagem): https://app.notion.com/p/40932fc5888a81088777f4a8723dc066
- Banco **Cronograma & Entregas**: `collection://70b014df-66f2-47f6-bb33-85ac4c800bca`
  - Campos: Entrega, Agente, Status (A fazer / Em produção / Aguardando aprovação / Aprovado), Prazo, Ferramenta, Link, Notas
- Banco **Créditos IA**: `collection://b35d4aa7-44f1-4316-b8dd-827899cefd72`
  - Campos: Ferramenta, Uso no doc, Saldo, Unidade, Expira/renova em, Status (Ativo / Zerado / Bloqueado)
- Material bruto: Google Drive da conta docdagoma, pasta DOCS (PRODUÇÃO, GRAVAÇÃO, ROTEIRO, MAPA NETFLIX)

## Regras atuais

1. Gate humano: nada vai para "Aprovado" sem o Fern aprovar. O agente para em "Aguardando aprovação".
2. Créditos: gaste primeiro o que expira antes. Ferramentas ativas: Firefly, Flow, ElevenLabs, Dreamina, Segmind, Replicate.
3. Higgsfield: liberado só para o Blender na nuvem (3D Jutsu: montar cena e renderizar animatic, sem crédito). Geração paga (vídeo, imagem) continua bloqueada até os créditos das outras zerarem e o Fern aprovar a assinatura.
4. Editor: Adobe Premiere Pro num Mac M4 Max. O Premiere MCP só roda no Windows, então a timeline vai por XML importado no Premiere.
5. Toda entrega vira linha no Cronograma. Todo uso de crédito atualiza o Saldo em Créditos IA.
6. Não envie e-mail, Slack nem convite de agenda sem o Fern pedir.
7. O Dagoma só é acionado quando o corte estiver mais fechado (autorização de imagem, tema do orfanato). Nenhum agente entra em contato com ele antes.
8. Produtora: Fernando Magnata Produções Artísticas (ME).

## Como cada ferramenta é usada

- **Firefly, Flow, Dreamina:** sem geração pelo conector. O agente entrega o prompt pronto para colar, o Fern gera e informa o gasto. O conector Adobe serve para expandir quadro (generative expand), ajustes de imagem, melhorar fala, fontes e boards.
- **ElevenLabs, Segmind, Replicate:** têm API. Rodam no Mac com a chave em variável de ambiente (`ELEVENLABS_API_KEY`, `SEGMIND_API_KEY`, `REPLICATE_API_TOKEN`). Nunca cole a chave no chat nem no repo.
- **Local no Mac (grátis, sem crédito):** transcrição com `mlx-whisper` (large-v3-turbo), identificação de quem fala com `pyannote`, QC com `ffmpeg`/`ffprobe`. Use o local antes de gastar crédito.

## Recriação de cenas

Cenas sem imagem real seguem `documentario/fluxo-recriacao.md` (blocking no Blender → animatic aprovado → Seedance).

## Ferramentas por agente

| Agente | Usa |
|---|---|
| produtor | Notion, Google Calendar, Drive |
| diretor-arte | Firefly e Dreamina (prompt), conector Adobe (fontes, ajustes, expandir quadro, boards), Figma |
| motion | Flow, Firefly e Dreamina (prompt), Replicate/Segmind (API), Blender (conector oficial, no Mac), scripts After Effects |
| montador | Transcrição local, Drive, XML para o Premiere, ElevenLabs (narração guia) |
| finalizador | ffmpeg local, conector Adobe (melhorar fala), ElevenLabs (Voice Isolator), Replicate (upscale e restauração de arquivo) |
