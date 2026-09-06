# Portadas para Redes Sociales — Tandil Labs

Archivos de imagen, plantillas vectoriales y herramientas de edición para portadas y publicaciones de **Facebook** e **Instagram**, utilizando las sierras reales de Tandil (formaciones graníticas del Sistema de Tandilia) combinadas con el logotipo y la identidad de Tandil Labs.

---

## 1. Imágenes Listas para Usar (Alta Resolución)

- **`portada-facebook.jpg`** (1920 x 1080 px):
  - Portada panorámica 16:9 con atardecer dorado en las sierras de Tandil.
  - Logotipo y textos ubicados en la mitad derecha para evitar ser tapados por la foto de perfil circular de Facebook (tanto en computadoras como en celulares).
- **`portada-instagram.jpg`** (1080 x 1080 px):
  - Formato cuadrado 1:1 para feed, post fijado o portada de perfil de Instagram.
- **`portada-facebook-crepusculo.jpg`** (1920 x 1080 px):
  - Variante crepuscular en tonos azules y pampa nocturna.

---

## 2. Fondos Fotográficos Limpios (Sin texto)

- **`fondo-sierras-16-9.jpg`**: Fotografía paisajística pura de las sierras de Tandil en 16:9.
- **`fondo-sierras-1-1.jpg`**: Fotografía paisajística pura de las sierras de Tandil en 1:1 cuadrado.

---

## 3. Plantillas Editables

### A. Editor Visual Web (La forma más fácil y rápida)
Abra el archivo **`editor-portadas.html`** en su navegador (o en `assets/social/editor.html`).
- Permite cambiar en tiempo real los textos, teléfonos, sitios web o eslóganes.
- Cambia entre formatos (Facebook 16:9, Instagram 1:1, Historias/Reels 9:16).
- Mueve el logo de posición y ajusta tamaño y oscurecimiento de fondo.
- Descarga la imagen terminada en **PNG** o **JPG** con un solo clic.

### B. Plantillas Vectoriales SVG (Para Figma, Illustrator o Inkscape)
- **`portada-facebook.svg`**
- **`portada-instagram.svg`**
Abra estos archivos en cualquier software de diseño o editor de código. Las capas de texto (`<text>`) y los logotipos son independientes y 100% editables.

### C. Generador por Consola (Python)
Script en Python con Pillow para renderizar imágenes en masa o automatizadas:
```bash
# Generar ambas portadas por defecto
python3 scripts/generar_portadas.py

# Personalizar textos desde la terminal
python3 scripts/generar_portadas.py --formato facebook --subtitulo "DESARROLLO DE SOFTWARE" --detalle "Automatización de Procesos • Tandil"
```
