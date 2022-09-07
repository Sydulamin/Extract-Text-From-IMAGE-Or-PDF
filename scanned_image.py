import pytesseract
import glob
from pdf2image import convert_from_path


# images = glob.glob(r"images\*.png")
# for img in images:
#     image_text = pytesseract.image_to_string(img)
#     with open(f'{img}.txt','w') as the_file:
#         the_file.write(image_text)

pdfs = glob.glob(r"pdf\*.pdf")
for pdf_path in pdfs:
    pages = convert_from_path(pdf_path,500)
    for pageNum,imgBlob in enumerate(pages):
        text = pytesseract.image_to_string(imgBlob,lang='eng')
        with open(f'{pdf_path[:-4]}_page_{pageNum}.txt','w') as the_file:
            the_file.write(text)