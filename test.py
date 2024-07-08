from os import listdir
from random import choice
import pikepdf
from pikepdf import Pdf


Data=[]
path="./"
OutputFolder="Output"
pdfs=[ filename for filename in listdir(path) if filename.endswith(".pdf") ]

def generate_password(filename):
    strippedFilename = ''.join(i for i in filename if i.isdigit())

    if strippedFilename.isdigit():
        return strippedFilename
    
    return ''.join([choice('0123456789') for i in range(8)])


for pdf in pdfs:
    password = generate_password(pdf)

    print("Password: " + str(password))

    with Pdf.open(f"{path}/{pdf}") as pdffile:
        pdffile.save(f"{OutputFolder}/{pdf[:-4]}.pdf",encryption=pikepdf.Encryption(owner=password, user=password, R=4))

    filename = pdf.replace('.pdf', '')

    Data.append(f"{filename},{password}")

open("credentials.csv","a").writelines(s + '\n' for s in Data)