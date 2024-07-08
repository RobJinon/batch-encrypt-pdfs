from os import listdir
from random import choice
import pikepdf
from pikepdf import Pdf
import tkinter as tk
from tkinter import filedialog
import pandas as pd

root = tk.Tk()
root.withdraw()

def read_filename():
    data = pd.read_csv("credentials.csv")
    filenames = data['Filename'].astype(str).tolist()
    return filenames
 
path = filedialog.askdirectory()
credentials = filedialog.askopenfile(filetypes = [('csv', '*.csv')], title="Select credentials file")

OutputFolder="Output"

# Returns a list of filenames (ex: ["FILENAME0.pdf", "FILENAME01.pdf"])
pdfs=[ filename for filename in listdir(path) if filename.endswith(".pdf") ]
filenames = read_filename()


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

counter = 0

try:
    for pdf in pdfs:
        filename = pdf.replace('.pdf', '')
        index = filenames.index(filename)

        password = birthdays[index]
        
        if filename in filenames:
            try:
                with Pdf.open(f"{path}/{pdf}", allow_overwriting_input=True) as pdffile:
                    pdffile.save(f"{path}/{pdf}",encryption = pikepdf.Encryption(owner=password, user=password, R=4))
                counter += 1
            except:
                continue

    if counter > 0:
        tk.messagebox.showinfo(title = "Success", message = "Files encrypted successfully.")
    else:
        tk.messagebox.showinfo(title = "Success", message = "No files encrypted.")

except Exception as error:
    message = "Error: " + str(type(error).__name__)

    tk.messagebox.showwarning(title = "Error", message = message)
