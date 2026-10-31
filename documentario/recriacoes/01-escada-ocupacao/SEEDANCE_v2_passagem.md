# Recriação 01 v2: a escada como passagem de tempo

Cada corte é um salto de 10 anos. Mesma subida, mesmo case, ele mais velho e com outra roupa. O Dagoma tem 1,85 m, é grande e quadrado; o boneco já está nessa escala.

- Animatic: `animatic_escada_v2.mp4` (10 s, 3 planos). Plano extra: `animatic_v2_plano04.mp4`.
- Cores do boneco: **azul = 2006 (22 anos)**, **verde = 2016 (32 anos)**, **magenta = hoje (42 anos)**. Ponto amarelo = rosto. Caixa laranja = case.

## Referências (ordem de upload)

- **video 1** = `animatic_escada_v2.mp4`
- **image 1** = frame real da escada (o do vão até o térreo)
- **image 2** = `folha_2006_22anos.jpg`
- **image 3** = folha de 2016 (32 anos). Se ainda não existir, use de novo a de 2006 e troque "at 32, 2016" por "at 22, 2006".
- **image 4** = `folha_2026_42anos.jpg` (refeita com a altura certa)
- **image 5** = `ref3_cases_detalhe.jpg`

## No Dreamina

1. AI Video → Seedance 2.5 (ou 2.0) → **Omni reference**.
2. No **+**, suba o animatic e as 5 imagens nesta ordem. O 2.0 aceita até 12 referências, o 2.5 até 50.
3. Cole o prompt abaixo e troque "video 1" e "image 1…5" pelas tags @ que o Dreamina mostrar para cada arquivo.
4. 16:9, 10 s, na menor resolução disponível. Uma geração só, para conferir.
5. O Dreamina restringe rosto de pessoa real nas referências. Se recusar alguma imagem: no frame da escada, corte as pessoas da borda esquerda; nas folhas, o visual pintado tende a passar.

## Prompt (colar no Seedance)

```
Follow video 1 shot for shot: keep its camera positions, camera moves, cuts and timing. The colored figures are placeholders for one man, DAGOMA, at three ages; replace them with the real person and do not copy their stiff body mechanics. He is tall and heavily built, about 1.85 m, broad and square.

Image 1 is the location: the stairwell of an occupied building in downtown São Paulo, open rectangular well, rounded white concrete parapets, worn grey steps, peeling teal walls, warm window light on the lower floors.

Blue figure = DAGOMA at 22, in 2006, exactly as in image 2. Green figure = DAGOMA at 32, in 2016, exactly as in image 3. Magenta figure = DAGOMA at 42, today, exactly as in image 4. The orange box is his DJ turntable flight case from image 5; in every shot he carries it against his chest with both arms.

Shot 1 (0.0–3.0 s), 2006: ground floor, low frontal camera; he climbs the first flight toward the lens.
Shot 2 (3.0–7.0 s), 2016: several floors higher; handheld camera follows from behind as he turns at the landing and keeps climbing.
Shot 3 (7.0–10.0 s), today: straight top-down view from the top of the stairwell; he climbs the last flight, the endless well below him.

Each cut jumps ten years: the same climb, the same case, an older man in different clothes. Heavy breathing, effort, steady pace.

Style: painted look matching the character sheets, visible brushwork, warm earthy palette, documentary camera behavior. No music. Sound: footsteps on concrete, breathing, distant voices and a radio from other floors. No text, no logos.
```

Se não adotarmos o look pintado, troque a linha Style por: `Style: observational documentary, natural available light, subtle film grain.`

## Plano 4 (câmera desce e cruza com ele), versão hoje

Use `animatic_v2_plano04.mp4` como video 1 e a folha de 2026 como image 2. O prompt é o do plano 4 em `SEEDANCE.md`; acrescente: "He is tall and heavily built, about 1.85 m, broad and square."
