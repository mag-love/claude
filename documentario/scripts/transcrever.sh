#!/usr/bin/env bash
# Transcreve no Mac (Apple Silicon) todos os vídeos/áudios de uma pasta, sem gastar crédito.
# Uso: documentario/scripts/transcrever.sh "/Volumes/Magnesio/ENTREVISTAS"
# Saída: documentario/transcricoes/<nome do arquivo>.{srt,json,txt}
# Requer: brew install ffmpeg && pip install mlx-whisper
set -euo pipefail

ORIGEM="${1:?Informe a pasta das entrevistas, ex.: /Volumes/Magnesio/ENTREVISTAS}"
DESTINO="$(cd "$(dirname "$0")/.." && pwd)/transcricoes"
MODELO="mlx-community/whisper-large-v3-turbo"
mkdir -p "$DESTINO"

find "$ORIGEM" -type f \( -iname '*.mov' -o -iname '*.mp4' -o -iname '*.mxf' -o -iname '*.wav' -o -iname '*.mp3' -o -iname '*.m4a' \) \
  ! -name '._*' -print0 |
while IFS= read -r -d '' arquivo; do
  nome="$(basename "${arquivo%.*}")"
  if [[ -f "$DESTINO/$nome.json" ]]; then
    echo "pula (já transcrito): $nome"
    continue
  fi
  echo "transcrevendo: $arquivo"
  mlx_whisper "$arquivo" --model "$MODELO" --language pt \
    --output-format all --output-dir "$DESTINO" --output-name "$nome"
done

echo "Pronto. Transcrições em $DESTINO"
