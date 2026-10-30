# Recriação com previz (Blender → Seedance)

Quando usar: só onde o montador marcou FALTA COBERTURA e não existe imagem real nem arquivo (infância, venda de bala no trem, a escada da ocupação). Material real sempre vem primeiro.

## Regras de documentário

- Recriação nunca se passa por arquivo. Ela tem um look próprio, definido pelo diretor de arte, e o espectador percebe que é recriação.
- Rosto ou corpo de pessoa real só com aprovação dela (Dagoma, família). Registre a aprovação nas Notas da entrega.

## Etapas

1. **Plano da cena (motion).** A fala que a cena cobre, duração exata (timecode do montador), no máximo 3 a 4 planos por geração.
2. **Referências.**
   - Ambiente: foto real do lugar quando existir; senão, imagem gerada (Firefly ou Dreamina). Sem pessoas e sem texto pequeno.
   - Personagens: foto de referência aprovada ou folha de personagem.
3. **Blocking no Blender** (Claude + conector oficial do Blender no Mac, ou Blender na nuvem do Higgsfield 3D Jutsu, sem crédito), colando `documentario/blender/PROMPT_BLOCKING.md`.
   - Personagens como blocos: cubo de corpo + esfera de cabeça, uma cor por personagem, frente da cabeça marcada. Nada de boneco com rig: quanto mais detalhado, mais o Seedance copia o movimento robótico.
   - Câmeras e cortes com a regra dos 180°. Animatic 720p em MP4 com a duração da fala.
   - **No Mac, use o starter kit da Curious Refuge** (`cr_blender_starterkit.blend`, fica fora do Git). Cole o PROMPT_TEMPLATE que vem dentro dele. O kit tem manequim com passada real (`kit.walk()`), prende o case na mão (`kit.attach_prop()`), renderiza (`kit.render_animatic()`) e escreve o prompt (`kit.seedance_prompt()`).
   - **Conflito em aberto:** o kit diz que o Seedance copia o movimento do manequim 1:1 (nunca deslizar o personagem); os comentários do vídeo dizem que blocos soltam a atuação. Na primeira cena, gere os dois no rascunho e fique com o melhor.
   - **Regras do kit:** no máximo 15 s e 3 planos por geração; cada plano com 2 s ou mais; câmera andando no máximo ~8% da largura do quadro por segundo; prompt com até 2000 caracteres.
4. **Gate: o Fern aprova o animatic.** Até aqui, nenhum crédito gasto.
5. **Geração no Seedance.** Dreamina primeiro (créditos); Replicate ou Segmind se o modelo estiver disponível lá. Na primeira cena, teste as duas rotas e adote a melhor:
   - **Rota A, vídeo como guia:** animatic como vídeo 1 + imagens de referência. O prompt diz para usar o vídeo só como guia de câmera e cortes, e que os blocos são marcadores de posição.
   - **Rota B, storyboard:** frames-chave do animatic pintados com o modelo de imagem (mesmo enquadramento, referências aplicadas) e animados sem vídeo de referência.
   - Sempre primeiro em rascunho ou baixa resolução, quando a plataforma oferecer. Alta resolução só depois de aprovado.
6. **Finalização.** Upscale (Replicate) se preciso, cor e grão no look da recriação, entra na timeline no timecode marcado.
7. **Registro.** Cronograma (versões, aprovação, consentimento) e Créditos IA (gasto).
