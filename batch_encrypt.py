from os import listdir
import pikepdf
from pikepdf import Pdf
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os

# Reads filenames from the credentials file (csv)
def read_filename(credentials):

    try: 
        data = pd.read_csv(credentials.name)
        filenames = data['Filename'].astype(str).tolist()

        return filenames
    
    except:
        data = pd.read_excel(credentials.name, dtype='object')
        filenames = data['Filename'].astype(str).tolist()

        return filenames

def read_password(credentials):

    try: 
        data = pd.read_csv(credentials.name)
        filenames = data['Birthdate'].astype(str).tolist()

        return filenames
    
    except:
        data = pd.read_excel(credentials.name, dtype='object')
        filenames = data['Birthdate'].astype(str).tolist()

        return filenames
    
# Changes the format of the date from DDMMYYYY to MMDDYYYY
def format_date(date):

    day = date[:2]
    month = date[2:4]
    year = date[4:]

    return month+day+year

def encrypt_pdf(pdfs, filenames, birthdays, path):
    counter = 0 # counts the number of files encrypted

    # initalize backup credentials data
    data = []
    data.append("Filename, Birthdate")

    try:
        for pdf in pdfs:
            filename = pdf.replace('.pdf', '')  #removes the '.pdf' extension in the filename
            
            # check if filename exists in the credentials file
            try:
                index = filenames.index(filename)
            except:
                continue

            password = birthdays[index]

            # print('Filename' + str(counter) + ": " + str(filename) + "\nPassword" + str(counter) + ": " + str(password))
            
            if filename in filenames:
                try:
                    # this is where the ecryption proces happens
                    with Pdf.open(f"{path}/{pdf}", allow_overwriting_input=True) as pdffile:
                        pdffile.save(f"{path}/{pdf}",encryption = pikepdf.Encryption(owner=password, user=password, R=4))
                    counter += 1

                    data.append(f"'{filename}, '{password}")
                except:
                    continue

        if counter > 0:
            tk.messagebox.showinfo(title = "Success", message = "Files encrypted successfully. " + str(counter) + " files encrypted.")
        else:
            tk.messagebox.showinfo(title = "Success", message = "No files encrypted.")

        open(os.path.join(path , "credentials_backup.csv"), "w").writelines(s + '\n' for s in data)

    except Exception as error:
        message = "Error: " + str(type(error).__name__)
        message = "Error: " + str(error)
    
        tk.messagebox.showwarning(title = "Error", message = message)

def main():

    root = tk.Tk()  # Initializes Tkinter module
    root.withdraw() # Hide root window
 
    # opens a dialog input to select a directory and credentials
    path = filedialog.askdirectory()
    credentials = filedialog.askopenfile(filetypes = [('All files', '*'),('.csv', '*.csv'), ('.xlsx', '*.xlsx')], title="Select credentials file")

    # Returns a list of filenames (ex: ["FILENAME0.pdf", "FILENAME01.pdf"]) based on the files in the directory
    pdfs = [filename for filename in listdir(path) if filename.endswith(".pdf")]

    # Returns a list of filenames (ex: ["FILENAME", "FILENAME"]) based on the credentials file (csv)
    filenames = read_filename(credentials)

    # Returns a list of birthdays (string) which will serve as the password
    birthdays = read_password(credentials)

    encrypt_pdf(pdfs, filenames, birthdays, path)

main()