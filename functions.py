"""
Python Docx
  pip install python-docx
  https://python-docx.readthedocs.io/en/latest/

Python PYPDF2
  pip install PyPDF2
  https://pypi.org/project/docx2pdf/

DOCX2PDF
  pip install docx2pdf
  https://pypi.org/project/docx2pdf/

rut:
, C.I. N° 
, con nota final 
"""

import re 
from docx import Document
from docx2pdf import convert
from PyPDF2 import PdfWriter, PdfReader

def getFromDocx(doc, regex):
    """
    Busca parrafo por parrafo un string en base a una expresion regular.
    retorna una lista con todas la coicidencias y un numero que indica la pagina en la que fue encontrada
    """
    names = []
    i = 0
    for para in doc.paragraphs:
        text = para.text
        if not len(text):
            continue

        results = re.search(regex, text)
        if results:
            name = results.group(1).strip()
            names.append([i, name])
            i += 1
    return names

def splitPdf(reader, names, destDir):
    """
    Recibe el documento pdf, la lista con los nombres y el directorio de destino.
    Divide el pdf y le asigna el nombre correspondiente a la pagina
    """
    length = len(names)
    for index, name in names:
        try:
            page = reader.pages[index]
            pdfOutDir = f'{destDir}/{name}.pdf'
            pdfOut = open(pdfOutDir, 'wb') 
            
            writer = PdfWriter()
            writer.add_page(page)
            writer.write(pdfOut)
            print(f"{name}.pdf creado correctamente.")
        except:
            print(f"\n{name}.pdf no ha podido ser creado.\n")

def wordToPdf(options):
    print(f"""
    Archivo Original: {options["docDir"]}
    Destino: {options["destDir"]}
    Frase de inicio: {options["start"].get()}
    Frase de fin: {options["stop"].get()}\n""")
    #Generacion de la expresion regular
    start = options["start"].get()
    stop = options["stop"].get()
    regex = re.escape(start) + r'(.*?)' + re.escape(stop) 
    
    # Crear un pdf en base al docx
    docDir = options["docDir"]
    destDir = options["destDir"]
    pdfDir = destDir + "/" + docDir.replace('.docx', '').split("/")[-1] + ".pdf"
    convert(docDir, pdfDir)

    doc = Document(docDir)
    names = getFromDocx(doc, regex)
    
    reader = PdfReader(pdfDir)
    splitPdf(reader, names, destDir)

