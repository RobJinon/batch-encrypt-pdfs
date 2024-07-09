from os import listdir
import pikepdf
from pikepdf import Pdf
import tkinter as tk
from tkinter import filedialog
import pandas as pd


root = tk.Tk()  # Initializes Tkinter module
root.withdraw() # Hide root window

 
# opens a dialog input to select a directory and credentials
path = filedialog.askdirectory()
credentials = filedialog.askopenfile(filetypes = [('All files', '*'),('.csv', '*.csv'), ('.xlsx', '*.xlsx')], title="Select credentials file")


# Returns a list of filenames (ex: ["FILENAME0.pdf", "FILENAME01.pdf"]) based on the files in the directory
pdfs = [filename for filename in listdir(path) if filename.endswith(".pdf")]


# Reads filenames from the credentials file (csv)
def read_filename():
    try: 
        data = pd.read_csv(credentials.name)
        filenames = data['Filename'].astype(str).tolist()
        return filenames
    except:
        data = pd.read_excel(credentials.name)
        data.to_csv("./credentials.csv")
        filenames = data['Filename'].astype(str).tolist()
        print(filenames)
        return filenames

# Returns a list of filenames (ex: ["FILENAME", "FILENAME"]) based on the credentials file (csv)
filenames = read_filename()

def read_password():
    try: 
        data = pd.read_csv(credentials.name)
        filenames = data['Birthdate'].astype(str).tolist()
        return filenames
    except:
        data = pd.read_excel(credentials.name)
        data.to_csv("./credentials.csv")
        filenames = data['Birthdate'].astype(str).tolist()
        print(filenames)
        return filenames

# Returns a list of birthdays (string) which will serve as the password
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
        
        try:
            index = filenames.index(filename)
        except:
            continue

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
    message = "Error: " + str(error)
    

    tk.messagebox.showwarning(title = "Error", message = message)
