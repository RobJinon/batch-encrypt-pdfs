from os import listdir
from random import choice
import pikepdf
from pikepdf import Pdf
import tkinter as tk
from tkinter import filedialog
import pandas as pd

root = tk.Tk()
root.withdraw()

Data = []
 
path = filedialog.askdirectory()

OutputFolder="Output"

pdfs=[ filename for filename in listdir(path) if filename.endswith(".pdf") ]

# def generate_password(filename):
#     strippedFilename = ''.join(i for i in filename if i.isdigit())

#     if strippedFilename.isdigit():
#         return strippedFilename
    
#     # sets default password if filename is not numeric  
#     return ''.join([choice('0123456789') for i in range(8)])

def read_password():
    data = pd.read_csv("credentials.csv")
    birthdays = data['Birthdate'].astype(str).tolist()
    return birthdays

birthdays = read_password()

# Changes the format of the date from DDMMYYYY to MMDDYYYY
def format_date(date):

    day = date[:2]
    month = date[2:4]
    year = date[4:]

    return month+day+year

try:
    counter = 0
    for pdf in pdfs:
        password = birthdays[counter]

        with Pdf.open(f"{path}/{pdf}", allow_overwriting_input=True) as pdffile:
            pdffile.save(f"{path}/{pdf}",encryption = pikepdf.Encryption(owner=password, user=password, R=4))

        filename = pdf.replace('.pdf', '')
        Data.append(f"{filename},{password}")

        # open("credentials.csv","a").writelines(s + '\n' for s in Data)

        filename = pdf.replace('.pdf', '')
        Data.append(f"{filename},{password}")
        
        counter += 1

# open("credentials.csv","a").writelines(s + '\n' for s in Data)
    tk.messagebox.showinfo(title = "Success", message = "Files encrypted successfully")
    
except Exception as error:
    message = "Error (" + str(type(error).__name__) + "): Files already encrypted."

    tk.messagebox.showwarning(title = "Error", message = message)
