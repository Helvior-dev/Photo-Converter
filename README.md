# Photo Converter

A small interactive Python CLI for batch-converting images between common file formats with Pillow.

## Features

- Converts matching files in one folder from a selected source format to a selected output format.
- Displays conversion progress with `tqdm`.
- Uses a white background when exporting `RGBA` or `LA` images to JPEG.
- Applies Pillow quality settings when saving JPEG and WebP files.

## Supported formats

`bmp`, `ico`, `jpeg`, `jpg`, `pbm`, `pgm`, `png`, `ppm`, `tif`, `tiff`, `tga`, `webp`

## Requirements

- Python 3.8 or newer
- Packages listed in `requirements.txt`

## Setup

Clone the repository and enter its directory:

```bash
git clone https://github.com/Helvior-dev/Photo-Converter.git
cd Photo-Converter
```

Create and activate a virtual environment, then install the dependencies:

- Windows PowerShell:

  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  ```

- Linux or macOS:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

## Usage

Run the converter:

```bash
python convertor_photo.py
```

Enter the source folder, destination folder, source format, and output format when prompted. Enter format names without the leading dot, for example `png` and `jpg`.

The converter scans only the selected folder, not subfolders. Existing output files with the same names are overwritten. Use a separate destination folder and keep a backup of important images.
