#!/usr/bin/env python
# coding: utf-8

###############################################################################
# Imports
###############################################################################
# standard library
import os
import shutil
import struct
from pathlib import Path

# third-party dependencies
from dotenv import load_dotenv
import click
from cairosvg import svg2png
from PIL import Image

###############################################################################
# Constants
###############################################################################
load_dotenv()
DEBUG = os.getenv("DEBUG")
APP_ENV = os.getenv("APP_ENV")
ICON_SIZES = {16, 32, 48, 64, 128, 256, 512, 1024}
MESSAGES = {"CLI_INPUT": "Press Enter to continue..."}

###############################################################################
# Processing functions
###############################################################################
def convert_svg_to_png(
    input_svg: Path, output_dir: Path, icon_sizes=ICON_SIZES, dpi=144
):
    """Generate PNGs from SVG with consistent DPI."""
    png_files = []
    for size in icon_sizes:
        for suffix in ["", "@2x"]:
            output_file = output_dir / f"icon_{size}{suffix}.png"
            factor = 2 if suffix else 1
            svg2png(
                url=str(input_svg),
                write_to=str(output_file),
                output_width=size * factor,
                output_height=size * factor,
                dpi=dpi,
            )
            png_files.append(output_file)
    return png_files

def convert_png_to_ico(
    png_files: list, output_dir: Path, icon_sizes=ICON_SIZES
):
    """Generate an ICO file from PNG."""
    sizes = tuple((s, s) for s in icon_sizes)
    ico_file = output_dir / "icon.ico"

    # Find largest PNG by file size
    largest_img_path = max(png_files, key=lambda x: x.stat().st_size)

    img = Image.open(largest_img_path)
    img.save(str(ico_file), format="ICO", sizes=sizes)
    
    return ico_file

def convert_png_to_icns(png_files: list, output_dir: Path):
    """Generate ICNS file for macOS from PNGs."""
    # Mapping of pixel sizes to macOS icon types
    ICON_TYPES = {
        (16, 16): b"is32",  # 16x16@1x
        (32, 32): b"is32",  # 16x16@2x (32x32)
        (64, 64): b"ih32",  # 32x32@2x (64x64)
        (128, 128): b"it32",  # 128x128@1x
        (256, 256): b"ic08",  # 256x256@1x
        (512, 512): b"ic09",  # 256x256@2x (512x512)
        (1024, 1024): b"ic10",  # 512x512@2x (1024x1024)
    }

    icon_data = []

    for png_path in png_files:
        with Image.open(png_path) as img:
            width, height = img.size

        icon_type = ICON_TYPES.get((width, height))
        if not icon_type:
            # print(
            #     f"Unsupported size: {width}x{height}. Skipping: {png_path}"
            # )
            continue

        with open(png_path, "rb") as f:
            icon_data.append((icon_type, f.read()))

    icns_file = output_dir / "icon.icns"
    with open(icns_file, "wb") as f:
        f.write(b"icns")
        f.write(struct.pack(">I", 0))  # File size placeholder

        for icon_type, png_bytes in icon_data:
            f.write(icon_type)
            f.write(
                struct.pack(">I", len(png_bytes) + 8)
            )  # Header + data length
            f.write(png_bytes)

        # Update final file size
        f.seek(4)
        f.write(struct.pack(">I", f.tell()))

    return icns_file

###############################################################################
# CLI Setup
###############################################################################
@click.command()
@click.option(
    "--output-dir",
    "-O",
    default="output",
    type=click.Path(file_okay=False),
    help="Output directory (default: 'output')",
)
def main(output_dir: Path):
    """Convert SVG files to PNG, ICO, and ICNS formats."""
    n_svgs = len(list(Path.cwd().glob("*.svg")))
    output_dir = Path(output_dir)
    
    if output_dir.exists() and output_dir.is_dir():
        response = input(
            f"'{output_dir}' exists. It will be deleted. Continue? (y/N): "
        ).strip().lower() or "n"

        if response == "y":
            shutil.rmtree(output_dir)
            print(f"Directory '{output_dir}' has been deleted.")
        else:
            print("Operation canceled.")
            exit(0)
    
    if n_svgs:
        print(f"{n_svgs} SVGs files found. Creating {output_dir}...")
        output_dir.mkdir(parents=True)
        
        for input_svg in Path.cwd().glob("*.svg"):
            print(f"\nProcessing {input_svg}...")
            
            icon_output_dir = output_dir / input_svg.stem
            icon_output_dir.mkdir(parents=True)

            png_files = convert_svg_to_png(input_svg, icon_output_dir)
            print(f"Created '{icon_output_dir}' (PNGs)")
            
            ico_file = convert_png_to_ico(png_files, icon_output_dir)
            print(f"Created '{ico_file}' (Windows)")
            
            icns_file = convert_png_to_icns(png_files, icon_output_dir)
            print(f"Created '{icns_file}' (macOS)")
    else:
        print("No SVG files found")

    input(MESSAGES["CLI_INPUT"])

###############################################################################
# Entry point
###############################################################################
if __name__ == "__main__":
    if bool(DEBUG): 
        print("Debug mode:", DEBUG)
        print("App environment:", APP_ENV)
    main()
