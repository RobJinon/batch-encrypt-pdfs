# Batch File Encrypter

## 📝 General
Developers: Robien Jinon, Limuelle Alamil <br />
Description: This is a Python program that encrypts batch of files using `pikepdf` module.

## ❔ How to use (Users)
1. Download the repository (https://github.com/RobJinon/batch-encrypt-pdfs). If you can't access, ask for permission to be added as collaborator.
2. Download the executable (EXE) file `batch_encrypt.exe`.
3. Before starting, make sure that you have 1) the <ins> files to be encrypted </ins> and 2) the <ins> CSV/XLSX file </ins> that contains the list of filenames and birthdate ready. Take note of their location in your File Manager as well to easily find them later. <br />
⚠️ NOTE: Make sure that the list of filenames in the CSV/XLSX file is coherent with the filenames of the actual files to be encrypted in the directory. <br />
⚠️ NOTE: Make sure that the files to be encrypted are all in the same directory. The CSV/XLSX file can be stored anywhere.
4. Double click the EXE file to start the program.
5. A file dialog asking to select a directory will appear. Select the directory where the files to be encrypted is located.
6. Another file dialog asking to select a CSV/XLSX file will appear. This CSV/XLSX file is where the filenames and birthdate data are stored.

## ❓ How to use (Developers)
1. Clone the repository (https://github.com/RobJinon/batch-encrypt-pdfs) to your local device. If you can't access, ask for permission to be added as collaborator.
2. The repository contains several files: <br />
   `.gitignore` - This file contains the files and directories that is not included when pushing changes to the repo.<br />
   `README.md` - This file contains documentation.<br />
   `batch_encrypt.py` - This Python file contains the source code for the program. Changes are made in this file.<br />
   `batch_encrypt.exe` - This file is the source code as an executable file.
3. If not yet installed, install the following modules first:<br />
   `pikepdf` - PDF encryption<br />
   `pandas` - CSV/XLSX file handling
4. To start making changes, open the repo and create a new branch by running `git branch <branch_name>` in the bash terminal (e.g., `git branch lim-bug-fixes`). This way, you are not directly making modification in the working source code.
5. Once done with your changes, commit your changes and push your branch to the repository. If your branch has no merge conflicts with the `dev` branch (development branch), proceed to merge. <br />
⚠️ Note: Don't merge with the `main` branch unless you are absolutely sure that your branch works properly and error-free.
   
