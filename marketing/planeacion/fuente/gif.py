"""Arma un GIF por video recomendado a partir de los PNG que guarda print.cjs.
Uso: python3 gif.py <carpeta_frames>  -> ../animaciones/<id>.gif"""
import sys
from pathlib import Path
from PIL import Image
import gen

src = Path(sys.argv[1])
out = Path(__file__).parent.parent / "animaciones"
out.mkdir(exist_ok=True)
DUR = [1600, 1600, 1600, 1800]
for s in gen.STARS:
    frames = [Image.open(src / f"{s['id']}-{i}.png").convert("RGB") for i in range(len(s["frames"]))]
    w = 360
    frames = [f.resize((w, round(f.height * w / f.width)), Image.LANCZOS) for f in frames]
    seq, dur = [], []
    for i, f in enumerate(frames):
        seq.append(f); dur.append(DUR[i])
        if i < len(frames) - 1:  # fundido corto entre tomas
            for t in (0.33, 0.66):
                seq.append(Image.blend(f, frames[i + 1], t)); dur.append(70)
    pal = [im.quantize(colors=128, method=Image.MEDIANCUT) for im in seq]
    pal[0].save(out / f"{s['id']}.gif", save_all=True, append_images=pal[1:], duration=dur, loop=0, optimize=True)
    print(s["id"], (out / f"{s['id']}.gif").stat().st_size // 1024, "KB")
