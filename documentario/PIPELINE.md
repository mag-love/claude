# Doc Dagoma — pipeline de agentes

Contexto comum. Todo agente lê este arquivo antes de agir.

## Onde as coisas vivem

- Central no Notion (bíblia + regras): https://app.notion.com/p/40932fc5888a81a3b68ac3d5fac98fa2
- Banco **Cronograma & Entregas**: `collection://70b014df-66f2-47f6-bb33-85ac4c800bca`
  - Campos: Entrega, Agente, Status (A fazer / Em produção / Aguardando aprovação / Aprovado), Prazo, Ferramenta, Link, Notas
- Banco **Créditos IA**: `collection://b35d4aa7-44f1-4316-b8dd-827899cefd72`
  - Campos: Ferramenta, Uso no doc, Saldo, Unidade, Expira/renova em, Status (Ativo / Zerado / Bloqueado)
- Material bruto: Google Drive da conta docdagoma, pasta DOCS (PRODUÇÃO, GRAVAÇÃO, ROTEIRO, MAPA NETFLIX)

## Regras

1. Gate humano: nada vai para "Aprovado" sem o Fern aprovar. O agente para em "Aguardando aprovação".
2. Créditos: gaste primeiro o que expira antes. Ordem atual: Firefly → Flow → ElevenLabs → Dreamina.
3. Higgsfield bloqueado até os quatro acima zerarem e o Fern aprovar a assinatura. Mesmo com a ferramenta conectada, não use.
4. Editor: Adobe Premiere Pro.
5. Toda entrega vira linha no Cronograma. Todo uso de crédito atualiza o Saldo em Créditos IA.
6. Ferramenta sem conector (Flow, Dreamina, ElevenLabs): o agente entrega o prompt pronto para colar, e o Fern roda. Registre o gasto quando o Fern informar.
7. Não envie e-mail, Slack nem convite de agenda sem o Fern pedir.

## Ferramentas por função

| Agente | Com conector | Manual (prompt pronto) |
|---|---|---|
| produtor | Notion, Google Calendar, Drive | — |
| diretor-arte | Adobe (Firefly, fontes), Figma, Canva | Dreamina (Seedream) |
| motion | Adobe (Firefly) | Flow (Veo), Dreamina (Seedance), scripts After Effects |
| montador | Drive, Premiere MCP (só Windows) | XML para importar no Premiere, ElevenLabs (narração guia) |
| finalizador | Adobe (melhorar fala), ffmpeg/ffprobe local | ElevenLabs (Voice Isolator) |
