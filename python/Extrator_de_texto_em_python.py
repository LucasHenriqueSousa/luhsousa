import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from pdf2image import convert_from_path

# Converte PDF em imagens
images = convert_from_path(r"")




# Itera sobre as imagens para realizar OCR
texto = ""
for i, img in enumerate(images):
    texto += pytesseract.image_to_string(img, lang='por') + "\n\n"

# Salva o texto extraído em um arquivo
with open("GerênciadeMemória_Virtual.txt", "w") as f:
    f.write(texto)