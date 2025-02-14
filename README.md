![Release Version](https://img.shields.io/github/v/tag/cedbeu/svg-to-icons?label=version&style=flat-square)
![Python 3.9](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)
![Version](https://img.shields.io/badge/version-1.0-blue?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/status-active-brightgreen?style=flat-square)
![Click](https://img.shields.io/badge/Click-CLI-orange?style=flat-square)
![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-yellow?style=flat-square)
![CairoSVG](https://img.shields.io/badge/CairoSVG-SVG%20Rendering-purple?style=flat-square)

# README
Convert SVG to icons in the various format required for making applications for various OSes.

## Installation with venv/pip
`git clone https://github.com/cedbeu/svg-to-icons.git`

`cd svg-to-icons`

`python3 -m venv venv`

`source venv/bin/activate`

`pip install --upgrade pip`

`pip install -r requirements.txt`

## Input & Usage
Place your square SVG file(s) in the script directory (`svg-to-icons`) and run:

`python svg-to-icons.py`

## Output
Current version outputs the following formats:

```
svg-to-icons/
  └ output/
    └ {input_icon_name}/
      │─ icon.ico # windows 256x256
      │─ icon.icns # macOS various formats (regular & retina)
      │─ icon_16.png
      │─ icon_16@2x.png
      │─ icon_32.png
      │─ icon_32@2x.png
      │─ icon_48.png
      │─ icon_48@2x.png
      │─ icon_64.png
      │─ icon_64@2x.png
      │─ icon_128.png
      │─ icon_128@2x.png
      │─ icon_256.png
      │─ icon_256@2x.png
      │─ icon_512.png
      │─ icon_512@2x.png
      │─ icon_1024.png
      └─ icon_1024@2x.png
```
