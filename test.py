from os import listdir
from random import choice
import pikepdf
from pikepdf import Pdf


Data=[]
path="./"
OutputFolder="Output"
pdfs=[ filename for filename in listdir(path) if filename.endswith(".pdf") ]

def generate_password(filename):
    return ''.join(i for i in filename if i.isdigit())


for pdf in pdfs:
    password = generate_password(pdf)

    print("Password: " + str(password))

    with Pdf.open(f"{path}/{pdf}") as pdffile:
        pdffile.save(f"{OutputFolder}/{pdf[:-4]}.pdf",encryption=pikepdf.Encryption(owner=password, user=password, R=4))

    filename = pdf.replace('.pdf', '')

    Data.append(f"{filename},{password}")

open("credentials.csv","a").writelines(s + '\n' for s in Data)