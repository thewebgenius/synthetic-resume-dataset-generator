import subprocess
from pathlib import Path

PDF_DIR = Path("output/pdf")
IMAGE_DIR = Path("output/images")

PDFTOPPM = r"C:\poppler-25.12.0\Library\bin\pdftoppm.exe"

def convert_pdf_to_images():
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    pdf_files = list(PDF_DIR.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found.")
        return

    for pdf in pdf_files:
        output_prefix = IMAGE_DIR / pdf.stem

        command = [
            PDFTOPPM,
            "-png",
            "-r", "300",
            str(pdf.resolve()),
            str(output_prefix.resolve())
        ]

        print("Running:", " ".join(command))

        try:
            subprocess.run(command, check=True)
            print(f"✅ Converted: {pdf.name}")
        except Exception as e:
            print(f"❌ Failed: {pdf.name} → {e}")

if __name__ == "__main__":
    convert_pdf_to_images()
