# README
Convert SVG to icons in the various format required for making applications for various OSes.

## Installation with venv/pip:
`git clone https://github.com/cedbeu/svg-to-icons.git`

`cd svg-to-icons`

`python -m venv venv`

`pip install -r requirements.txt`

## Input:
Place your square SVG file(s) in the script directory (`svg-to-icons`)

## Usage
`source venv/bin/activate`

`python svg-to-icons.py`

## Output
Current version outputs the following formats:

```
svg-to-icons/
  └ output/
    └ input_icon_name/
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
