# Photo Converter 📸

A Python command-line (CLI) utility for batch converting image files from one format to another with high quality preservation and smart transparency handling.

## 🚀 Features
- **Batch Processing**: Convert all images of a chosen format within a folder in a single run.
- **Progress Bar**: Smooth progress bar powered by `tqdm`.
- **Smart Transparency Handling**: When converting from formats with alpha channel (PNG, WebP) to formats without it (JPG, JPEG), transparent backgrounds are automatically filled with clean white.
- **High Quality Output**: Lossy formats (JPG, WebP) are saved with maximum quality settings (`quality=95`, `subsampling=0`).

## 📁 Supported Formats
`bmp`, `ico`, `jpeg`, `jpg`, `pbm`, `pgm`, `png`, `ppm`, `tif`, `tiff`, `tga`, `webp`

## 🛠️ Installation & Setup

1. **Navigate to project directory**:
   ```bash
   cd "Convertor photo"
   ```

2. **Create & activate virtual environment**:
   - **Windows (PowerShell)**:
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - **Linux / macOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run**:
   ```bash
   python convertor_photo.py
   ```

## 📝 Usage Example
When launched, the script will prompt for:
1. Source folder path containing images (e.g. `C:\Photos\Input`).
2. Destination folder path (e.g. `C:\Photos\Output`).
3. Input file format (e.g. `png`).
4. Target output file format (e.g. `jpg`).
