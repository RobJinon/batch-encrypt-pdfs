from os import listdir
from random import choice
import pikepdf
from pikepdf import Pdf
import tkinter as tk
from tkinter import filedialog
import pandas as pd

root = tk.Tk()
root.withdraw()

 
path = filedialog.askdirectory()
credentials = filedialog.askopenfile(filetypes = [('csv', '*.csv')], title="Select credentials file")

OutputFolder="Output"

pdfs=[ filename for filename in listdir(path) if filename.endswith(".pdf") ]


def read_password():
    data = pd.read_csv(credentials)
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

        filename = pdf.replace('.pdf', '')
        
        with Pdf.open(f"{path}/{pdf}", allow_overwriting_input=True) as pdffile:
            pdffile.save(f"{path}/{pdf}",encryption = pikepdf.Encryption(owner=password, user=password, R=4))

        counter += 1

    tk.messagebox.showinfo(title = "Success", message = "Files encrypted successfully")

except Exception as error:
    message = "Error: " + str(type(error).__name__)

    tk.messagebox.showwarning(title = "Error", message = message)
