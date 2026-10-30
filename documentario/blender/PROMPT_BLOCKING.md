# Prompt de blocking (colar no Claude com o Blender conectado)

Troque tudo que está entre colchetes. Anexe a imagem de ambiente na mesma mensagem.

```
Você controla o Blender pelo conector. Monte o blocking de uma cena de recriação do Doc Dagoma.

Referências que vou usar no gerador de vídeo (você não precisa abri-las):
- IMAGEM 1 = ambiente: [descrição]
- IMAGEM 2 = [PERSONAGEM A]
- IMAGEM 3 = [PERSONAGEM B]

A imagem de ambiente está anexada.

Fala que esta cena cobre: "[trecho da entrevista]". Duração: [x] segundos.

Ação: [quem faz o quê, onde, em que ordem]

Planos (máximo 4):
1. [ex.: plano aberto da escada da ocupação]
2. [...]

Regras:
- Cenário: bloqueie a partir da imagem, só volumes simples, escala real.
- Personagens: cubo de corpo + esfera de cabeça, sem braços e sem rig. Uma cor sólida por personagem ([A] = azul, [B] = magenta). Marque a frente da cabeça com um círculo de outra cor.
- Câmera: lentes e movimentos que um operador real faria (tripé, ombro, dolly). Respeite a regra dos 180°.
- Timeline: 24 fps, duração igual à fala, um marker em cada corte.
- Confira o enquadramento contra a imagem de ambiente pelo menos duas vezes.
- Salve o .blend antes de rodar código.
- Render: Workbench ou EEVEE, 1280x720, MP4, em [pasta].

No fim, me entregue:
1. O caminho do MP4 e uma linha por plano com tempo de início e fim.
2. O prompt para o Seedance, em inglês: referências numeradas (video 1, image 1, image 2...), cada corte com tempo de início e fim, ação, câmera, luz e som, e a frase: "Use video 1 only as a guide for camera position, camera moves and cuts. The colored blocks are placeholders; do not copy their poses or body mechanics."
3. De 3 a 5 frames-chave (número do frame) para a rota storyboard.
```
