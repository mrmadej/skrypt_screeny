from fpdf import FPDF
import pytesseract
from PIL import Image
import os

# Ścieżka do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\marci\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Folder zrzutów ekranu
input_folder = r"D:\Egzamin_inzynierski\skrypt_screeny\screeny"
# Wyjściowy plik PDF
output_pdf_path = r"D:\Egzamin_inzynierski\skrypt_screeny\output.pdf"

# Klasa PDF z obsługą Unicode
class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        # Dodanie czcionki obsługującej Unicode
        self.add_font('DejaVu', '', r'D:\Egzamin_inzynierski\skrypt_screeny\DejaVuSans.ttf', uni=True)
        self.set_font('DejaVu', '', 12)  # Ustawienie standardowej czcionki DejaVu

# Utwórz obiekt PDF
pdf = PDF()

# Przetwarzanie obrazów
for filename in sorted(os.listdir(input_folder)):
    if filename.endswith(".png"):
        image_path = os.path.join(input_folder, filename)
        print(f"Przetwarzanie: {image_path}")
        try:
            # Odczytanie tekstu z obrazu
            image = Image.open(image_path)
            extracted_text = pytesseract.image_to_string(image, lang="pol")
            # Dodanie tekstu do PDF
            pdf.multi_cell(0, 10, extracted_text)
        except Exception as e:
            print(f"Błąd przetwarzania {filename}: {e}")

# Zapisz PDF
pdf.output(output_pdf_path)
print(f"Plik PDF zapisano w: {output_pdf_path}")
