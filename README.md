# Batch File Encrypter

## 📝 General
Developers: Robien Jinon, Limuelle Alamil <br />
Description: This is a Python program that encrypts batch of files using `pikepdf` module. It asks for two inputs: 1) directory of files to be encrypted and 2) spreadsheet containing the data which will be used to encrypt the files.

[Download Batch File Encrypter v1](https://github.com/RobJinon/batch-encrypt-pdfs/blob/main/dist/batch_encrypt.exe)

## ❔ How to use (Users)
1. Download the repository (https://github.com/RobJinon/batch-encrypt-pdfs). If you can't access, ask for permission to be added as collaborator.<br /><br />
![image](https://github.com/RobJinon/batch-encrypt-pdfs/assets/98687205/81c6e276-25d1-4d5c-a76c-de34c6e48bce)

2. Extract the compressed repository and find the file `batch_encrypt.exe` inside the `dist` folder.<br /><br />
![image](https://github.com/RobJinon/batch-encrypt-pdfs/assets/98687205/5a0e7780-b01f-4a79-95d1-9ed0e89f57b9)

3. Before starting, make sure that you have 1) the <ins> files to be encrypted </ins> and 2) the <ins> CSV/XLSX file </ins> that contains the list of filenames and birthdate ready. Take note of their location in your File Manager as well to easily find them later. <br /><br />
![image](https://github.com/RobJinon/batch-encrypt-pdfs/assets/98687205/19f3bdd5-2410-4ba8-b895-63079da82861)
![image](https://github.com/RobJinon/batch-encrypt-pdfs/assets/98687205/9525b5b2-7a10-499b-8f82-140562ee8f97)

⚠️ NOTE: Make sure that the list of filenames in the CSV/XLSX file is coherent with the filenames of the actual files to be encrypted in the directory. <br />
⚠️ NOTE: Make sure that the files to be encrypted are all in the same directory. The CSV/XLSX file can be stored anywhere.<br />

4. Double click the EXE file to start the program.<br />
5. A file dialog asking to select a directory will appear. Select the directory where the files to be encrypted is located.<br /><br />
![image](https://github.com/RobJinon/batch-encrypt-pdfs/assets/98687205/e9d8cd6e-a89b-450a-896b-92f08f667f26)

6. Another file dialog asking to select a CSV/XLSX file will appear. This CSV/XLSX file is where the filenames and birthdate data are stored.<br /><br />
![image](https://github.com/RobJinon/batch-encrypt-pdfs/assets/98687205/c6aff41e-af17-47cc-a8a4-883039375f6e)

7. If the encryption is successful, a toast like the one below will appear. Click OK.<br /><br />
![image](https://github.com/RobJinon/batch-encrypt-pdfs/assets/98687205/4f454920-66ec-4aa2-9f46-c22a4f9ededf)


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
   
