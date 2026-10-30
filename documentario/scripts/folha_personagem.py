#!/usr/bin/env python3
"""Gera a folha de personagem no Nano Banana Pro (Replicate), em 4K.

Uso (no Mac):
  pip install replicate
  export REPLICATE_API_TOKEN=...   # nunca coloque o token no repo
  python3 documentario/scripts/folha_personagem.py foto1.jpg foto2.jpg foto3.jpg

Lê o prompt de documentario/personagens/dagoma/PROMPT_NANOBANANA.txt e salva em
documentario/personagens/dagoma/saida/. Os nomes dos campos são lidos do schema do modelo,
então o script se ajusta se o Replicate mudar a API.
"""
import argparse
import pathlib
import sys
import time

import replicate

BASE = pathlib.Path(__file__).resolve().parents[1] / "personagens" / "dagoma"


def campos_do_modelo(modelo):
    versao = replicate.models.get(modelo).latest_version
    return versao.openapi_schema["components"]["schemas"]["Input"]["properties"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fotos", nargs="+", help="fotos de referência do Dagoma com os cases")
    ap.add_argument("--modelo", default="google/nano-banana-pro")
    ap.add_argument("--resolucao", default="4K")
    ap.add_argument("--proporcao", default="16:9")
    ap.add_argument("--prompt", default=str(BASE / "PROMPT_NANOBANANA.txt"))
    args = ap.parse_args()

    campos = campos_do_modelo(args.modelo)
    entrada = {"prompt": pathlib.Path(args.prompt).read_text(encoding="utf-8")}

    chave_img = next((k for k in ("image_input", "images", "input_images", "image") if k in campos), None)
    if chave_img is None:
        sys.exit(f"Não achei o campo de imagem. Campos do modelo: {sorted(campos)}")
    arquivos = [open(f, "rb") for f in args.fotos]
    entrada[chave_img] = arquivos if campos[chave_img].get("type") == "array" else arquivos[0]

    chave_res = next((k for k in ("resolution", "image_size") if k in campos), None)
    if chave_res:
        entrada[chave_res] = args.resolucao
    if "aspect_ratio" in campos:
        entrada["aspect_ratio"] = args.proporcao
    if "output_format" in campos:
        entrada["output_format"] = "png"

    print(f"Gerando no {args.modelo} ({args.resolucao}, {args.proporcao}) com {len(arquivos)} foto(s)...")
    saida = replicate.run(args.modelo, input=entrada)
    itens = saida if isinstance(saida, list) else [saida]

    destino = BASE / "saida"
    destino.mkdir(parents=True, exist_ok=True)
    carimbo = time.strftime("%Y%m%d-%H%M%S")
    for i, item in enumerate(itens):
        arquivo = destino / f"folha_dagoma_{carimbo}_{i}.png"
        arquivo.write_bytes(item.read())
        print(f"Salvo: {arquivo}")


if __name__ == "__main__":
    main()
