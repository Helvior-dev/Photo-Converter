import os
from PIL import Image
from tqdm import tqdm

SUPPORTED_FORMATS = {
    "jpg",
    "jpeg",
    "png",
    "webp",
    "bmp",
    "tiff",
    "tif",
    "ico",
    "ppm",
    "pgm",
    "pbm",
    "tga",
}
LOSSY_FORMATS = {"jpg", "jpeg", "webp"}
NO_ALPHA_FORMATS = {"jpg", "jpeg"}
input_dir = input("Folder where to get photos: ").strip()
output_dir = input("Where to save photos folder: ").strip()
input_ext = (
    input(
        f"Format of source files "
        f"(supported: {', '.join(sorted(SUPPORTED_FORMATS))}): "
    )
    .strip()
    .lower()
    .lstrip(".")
)
output_ext = (
    input(
        f"Output file format " f"(supported: {', '.join(sorted(SUPPORTED_FORMATS))}): "
    )
    .strip()
    .lower()
    .lstrip(".")
)
if input_ext not in SUPPORTED_FORMATS:
    raise ValueError(f"Unsupported input format: {input_ext}")
if output_ext not in SUPPORTED_FORMATS:
    raise ValueError(f"Unsupported output format: {output_ext}")
if not os.path.isdir(input_dir):
    raise FileNotFoundError(f"Folder not found: {input_dir}")
os.makedirs(output_dir, exist_ok=True)
files = [f for f in os.listdir(input_dir) if f.lower().endswith("." + input_ext)]
if not files:
    print("No files found for conversion")
    exit()
print(f"\nFiles found: {len(files)}")
print(f"Conversion: {input_ext.upper()} -> {output_ext.upper()}\n")
for filename in tqdm(files, desc="Conversion", unit="file", ascii=True):
    input_path = os.path.join(input_dir, filename)
    output_name = os.path.splitext(filename)[0] + "." + output_ext
    output_path = os.path.join(output_dir, output_name)
    try:
        with Image.open(input_path) as img:
            if output_ext in NO_ALPHA_FORMATS and img.mode in ("RGBA", "LA"):
                bg = Image.new("RGB", img.size, (255, 255, 255))
                bg.paste(img, mask=img.split()[-1])
                img = bg
            else:
                if output_ext in NO_ALPHA_FORMATS:
                    img = img.convert("RGB")
            save_kwargs = {}
            if output_ext in LOSSY_FORMATS:
                save_kwargs["quality"] = 95
                save_kwargs["subsampling"] = 0
            img.save(output_path, **save_kwargs)
    except Exception as e:
        print(f"\nError with file {filename}: {e}")
print("\nDone! All images have been processed.")
