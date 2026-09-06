#!/usr/bin/env python3
"""
Generador de Portadas Editables para Redes Sociales — Tandil Labs
Permite combinar fondos fotográficos reales de las sierras de Tandil con el logotipo oficial
y textos editables (Título, Bajada, Detalles) para Facebook e Instagram.
"""

import os
import argparse
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "social")
OUTPUT_DIR = os.path.join(ASSETS_DIR, "exportadas")

FONT_BOLD_PATH = "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf"
FONT_REGULAR_PATH = "/usr/share/fonts/gnu-free/FreeSans.otf"
if not os.path.exists(FONT_REGULAR_PATH):
    FONT_REGULAR_PATH = "/usr/share/fonts/TTF/DejaVuSans.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def crear_portada(
    formato="facebook",
    fondo_path=None,
    logo_path=None,
    titulo="TANDIL LABS",
    subtitulo="Software & Automatización",
    detalle="Sistemas a Medida • Tandil, Buenos Aires",
    salida_path=None,
    alineacion="derecha",
    oscurecer=0.25
):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if formato == "facebook":
        target_size = (1920, 1080)
        default_fondo = os.path.join(ASSETS_DIR, "fondo-sierras-16-9.jpg")
        default_salida = os.path.join(OUTPUT_DIR, "portada_facebook_generada.jpg")
    else:
        target_size = (1080, 1080)
        default_fondo = os.path.join(ASSETS_DIR, "fondo-sierras-1-1.jpg")
        default_salida = os.path.join(OUTPUT_DIR, "portada_instagram_generada.jpg")
        alineacion = "centro"

    fondo_path = fondo_path or default_fondo
    logo_path = logo_path or os.path.join(ASSETS_DIR, "logo-transparent-hd.png")
    salida_path = salida_path or default_salida

    if os.path.exists(fondo_path):
        bg = Image.open(fondo_path).convert("RGBA")
        bg_ratio = bg.width / bg.height
        target_ratio = target_size[0] / target_size[1]
        if bg_ratio > target_ratio:
            new_height = target_size[1]
            new_width = int(new_height * bg_ratio)
        else:
            new_width = target_size[0]
            new_height = int(new_width / bg_ratio)
        bg = bg.resize((new_width, new_height), Image.Resampling.LANCZOS)
        left = (new_width - target_size[0]) // 2
        top = (new_height - target_size[1]) // 2
        bg = bg.crop((left, top, left + target_size[0], top + target_size[1]))
    else:
        bg = Image.new("RGBA", target_size, (10, 15, 25, 255))

    if oscurecer > 0:
        overlay = Image.new("RGBA", target_size, (0, 0, 0, 0))
        draw_ov = ImageDraw.Draw(overlay)
        if alineacion == "derecha":
            for x in range(target_size[0]):
                factor = max(0.0, (x - target_size[0] * 0.35) / (target_size[0] * 0.65))
                alpha = int(255 * oscurecer * (factor ** 1.3))
                draw_ov.line([(x, 0), (x, target_size[1])], fill=(5, 10, 18, alpha))
        else:
            for y in range(target_size[1]):
                dist = abs(y - target_size[1] * 0.35) / (target_size[1] * 0.5)
                alpha = int(255 * oscurecer * max(0.0, 1.0 - dist * 0.5))
                draw_ov.line([(0, y), (target_size[0], y)], fill=(5, 10, 18, alpha))
        bg = Image.alpha_composite(bg, overlay)

    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        if formato == "facebook":
            logo_w = 420
            logo_h = int(logo.height * (logo_w / logo.width))
            logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
            if alineacion == "derecha":
                logo_x = int(target_size[0] * 0.68 - logo_w // 2)
                logo_y = int(target_size[1] * 0.28)
            else:
                logo_x = (target_size[0] - logo_w) // 2
                logo_y = int(target_size[1] * 0.22)
        else:
            logo_w = 400
            logo_h = int(logo.height * (logo_w / logo.width))
            logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
            logo_x = (target_size[0] - logo_w) // 2
            logo_y = int(target_size[1] * 0.20)

        glow = Image.new("RGBA", target_size, (0, 0, 0, 0))
        glow_draw = ImageDraw.Draw(glow)
        glow_box = [logo_x - 30, logo_y - 30, logo_x + logo_w + 30, logo_y + logo_h + 30]
        glow_draw.ellipse(glow_box, fill=(0, 229, 255, 45))
        glow = glow.filter(ImageFilter.GaussianBlur(radius=35))
        bg = Image.alpha_composite(bg, glow)
        bg.paste(logo, (logo_x, logo_y), logo)

    draw = ImageDraw.Draw(bg)

    if formato == "facebook":
        font_sub = get_font(FONT_BOLD_PATH, 28)
        font_det = get_font(FONT_REGULAR_PATH, 20)

        center_x = logo_x + logo_w // 2 if alineacion == "derecha" else target_size[0] // 2
        base_y = logo_y + logo_h + 20

        if subtitulo:
            bbox_sub = draw.textbbox((0, 0), subtitulo, font=font_sub)
            w_sub = bbox_sub[2] - bbox_sub[0]
            draw.text((center_x - w_sub // 2, base_y), subtitulo, fill="#38bdf8", font=font_sub)
            base_y += 45

        if detalle:
            bbox_det = draw.textbbox((0, 0), detalle, font=font_det)
            w_det = bbox_det[2] - bbox_det[0]
            draw.text((center_x - w_det // 2, base_y), detalle, fill="#e2e8f0", font=font_det)

    else:
        font_sub = get_font(FONT_BOLD_PATH, 34)
        font_det = get_font(FONT_REGULAR_PATH, 24)

        center_x = target_size[0] // 2
        base_y = logo_y + logo_h + 25

        if subtitulo:
            bbox_sub = draw.textbbox((0, 0), subtitulo, font=font_sub)
            w_sub = bbox_sub[2] - bbox_sub[0]
            draw.text((center_x - w_sub // 2, base_y), subtitulo, fill="#38bdf8", font=font_sub)
            base_y += 50

        if detalle:
            bbox_det = draw.textbbox((0, 0), detalle, font=font_det)
            w_det = bbox_det[2] - bbox_det[0]
            draw.text((center_x - w_det // 2, base_y), detalle, fill="#cbd5e1", font=font_det)

    final_img = bg.convert("RGB")
    final_img.save(salida_path, "JPEG", quality=95, optimize=True)
    print(f"✓ Portada guardada exitosamente: {salida_path}")
    return salida_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generar portadas de redes sociales para Tandil Labs")
    parser.add_argument("--formato", choices=["facebook", "instagram", "todos"], default="todos", help="Formato de la portada")
    parser.add_argument("--fondo", type=str, default=None, help="Ruta a imagen de fondo personalizada")
    parser.add_argument("--subtitulo", type=str, default="Software & Automatización", help="Subtítulo / Bajada")
    parser.add_argument("--detalle", type=str, default="Sistemas a Medida • Tandil, Buenos Aires", help="Detalle inferior")
    parser.add_argument("--alineacion", choices=["derecha", "centro"], default="derecha", help="Alineación del bloque de marca")
    parser.add_argument("--salida", type=str, default=None, help="Ruta del archivo de salida")

    args = parser.parse_args()

    if args.formato == "todos":
        crear_portada(formato="facebook", subtitulo=args.subtitulo, detalle=args.detalle, alineacion="derecha")
        crear_portada(formato="instagram", subtitulo=args.subtitulo, detalle=args.detalle, alineacion="centro")
    else:
        crear_portada(
            formato=args.formato,
            fondo_path=args.fondo,
            subtitulo=args.subtitulo,
            detalle=args.detalle,
            salida_path=args.salida,
            alineacion=args.alineacion
        )
