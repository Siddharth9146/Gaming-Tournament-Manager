"""Regenerate the QR code that points to the deployed site.

Usage:
    python generate_qr.py [url]

If no URL is given, defaults to the GitHub Pages URL below.
Outputs: qr.png (the QR), qr-card.png (a pretty pink card around the QR).
"""

import sys
from pathlib import Path

import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw, ImageFont

DEFAULT_URL = "https://siddharth9146.github.io/Gaming-Tournament-Manager/"

PINK_DARK = (227, 80, 137)
PINK_MID = (255, 143, 184)
PINK_SOFT = (255, 230, 239)
CREAM = (255, 251, 246)
INK = (74, 34, 51)


def make_qr(url: str, out_path: Path) -> Image.Image:
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        box_size=20,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=PINK_DARK, back_color=CREAM).convert("RGB")
    img.save(out_path)
    return img


def _try_font(size: int) -> ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def make_card(qr_img: Image.Image, out_path: Path) -> None:
    W, H = 1200, 1500
    card = Image.new("RGB", (W, H), PINK_SOFT)
    draw = ImageDraw.Draw(card)

    # soft gradient backdrop
    for y in range(H):
        t = y / H
        r = int(PINK_SOFT[0] * (1 - t) + CREAM[0] * t)
        g = int(PINK_SOFT[1] * (1 - t) + CREAM[1] * t)
        b = int(PINK_SOFT[2] * (1 - t) + CREAM[2] * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # inner rounded card
    margin = 60
    card_box = (margin, margin, W - margin, H - margin)
    draw.rounded_rectangle(card_box, radius=40, fill=CREAM, outline=PINK_MID, width=3)

    title_font = _try_font(72)
    sub_font = _try_font(36)
    foot_font = _try_font(30)

    title = "For Vanshita"
    sub = "scan with love"
    foot = "made just for you"

    # title
    tw = draw.textlength(title, font=title_font)
    draw.text(((W - tw) / 2, 130), title, font=title_font, fill=PINK_DARK)
    sw = draw.textlength(sub, font=sub_font)
    draw.text(((W - sw) / 2, 235), sub, font=sub_font, fill=INK)

    # QR
    qr_size = 800
    qr_resized = qr_img.resize((qr_size, qr_size), Image.NEAREST)
    qr_x = (W - qr_size) // 2
    qr_y = 330
    # subtle drop shadow
    shadow = Image.new("RGBA", (qr_size + 40, qr_size + 40), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((0, 0, qr_size + 40, qr_size + 40), radius=30,
                         fill=(227, 80, 137, 60))
    card.paste(shadow, (qr_x - 20, qr_y - 10), shadow)
    card.paste(qr_resized, (qr_x, qr_y))

    # heart + footer
    heart = "with love"
    hw = draw.textlength(heart, font=sub_font)
    draw.text(((W - hw) / 2, qr_y + qr_size + 60), heart,
              font=sub_font, fill=PINK_DARK)
    fw = draw.textlength(foot, font=foot_font)
    draw.text(((W - fw) / 2, qr_y + qr_size + 120), foot,
              font=foot_font, fill=INK)

    card.save(out_path)


def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    out_dir = Path(__file__).parent
    qr_path = out_dir / "qr.png"
    card_path = out_dir / "qr-card.png"
    qr_img = make_qr(url, qr_path)
    make_card(qr_img, card_path)
    print(f"URL: {url}")
    print(f"Wrote: {qr_path}")
    print(f"Wrote: {card_path}")


if __name__ == "__main__":
    main()
