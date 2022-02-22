from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import font
from tkinter import *
from tkinter import messagebox
import mysql.connector
from hashlib import sha256

# each password can only be decrypted with the same key it is encrypted with
# generates new key each time
# key MUST be saved in db with the rest of the acc details
# key = Fernet.generate_key()
# creates object to encrypt/decrypt
# crypter = Fernet(key)
# pw = crypter.encrypt(b'password1')
# decryptString = crypter.decrypt(pw)

#connecting to SQL database#
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database="passwordManager"
)

mycursor = db.cursor()


def show_frame(frame):
    frame.tkraise()


window = tk.Tk()
window.state('zoomed')

# ================ LOGIN FRAME CODE ================#
loginFrame = tk.Frame(window, bg='black')

loginLabel = tk.Label(loginFrame, text='LOG1N TO PWMAN', fg='green', bg='black', font=('OCR A Extended', 24))
loginLabel.place(relx=0.375, rely=0.3, relwidth=0.25)

masterPasswordEntry = tk.Entry(loginFrame)
masterPasswordEntry.place(relx=0.425, rely=0.35, relwidth=0.15)


# == login function when button clicked == #
def login():
    passwordEntered = masterPasswordEntry.get()

    #SQL CODE
    mycursor.execute("SELECT hashedPassword FROM login WHERE userID='1'")

    hashedPasswordDB1 = mycursor.fetchone()
    hashedPasswordDB2 = str(hashedPasswordDB1)
    hashedPasswordDB = hashedPasswordDB2.split("'")


    #print(hashedPasswordDB[1])
    #print(hashedPasswordDB1)
    #print(hashedPasswordDB2)
    hashedPasswordEntered = sha256(passwordEntered.encode('utf-8')).hexdigest()
    #print(hashedPasswordEntered)

    if hashedPasswordDB[1] == hashedPasswordEntered:
        show_frame(homeFrame)
    else:
        messagebox.showinfo("Error", "Incorrect Password")


loginButton = tk.Button(loginFrame, text='Login', command=login, font=('OCR A Extended', 12), bg='black', fg='green')
loginButton.place(relx=0.45, rely=0.38, relwidth=0.1)

# ================ HOME FRAME CODE ================#
homeFrame = tk.Frame(window, bg='black')

homeLabel = tk.Label(homeFrame, text='HOM3', fg='green', bg='black', font=('OCR A Extended', 24))
homeLabel.place(relx=0.375, rely=0.1, relwidth=0.25)

# button to take user to enter a brand new entry
newEntryButton = tk.Button(homeFrame, text='Add new account', font=('OCR A Extended', 12),
                           command=lambda: show_frame(brandNewEntryFrame), bg='black', fg='green')
newEntryButton.place(relwidth=0.15, relx=0.425, rely=0.2)

# button to take user to new existing account
existingAccButton = tk.Button(homeFrame, text='Add existing account', font=('OCR A Extended', 12),
                              command=lambda: show_frame(newExistingAccountFrame), bg='black', fg='green')
existingAccButton.place(relwidth=0.15, relx=0.425, rely=0.3)

# button to take user to edit entry
editEntryButton = tk.Button(homeFrame, text='Edit an existing entry', font=('OCR A Extended', 12),
                            command=lambda: show_frame(editEntryFrame), bg='black', fg='green')
editEntryButton.place(relwidth=0.15, relx=0.425, rely=0.4)

# button to take user to view entries
viewEntriesButton = tk.Button(homeFrame, text='View all entries', font=('OCR A Extended', 12),
                              command=lambda: show_frame(viewEntriesFrame), bg='black', fg='green')
viewEntriesButton.place(relwidth=0.15, relx=0.425, rely=0.5)

# ================ BRAND NEW ENTRY FRAME CODE ================#
brandNewEntryFrame = tk.Frame(window, bg='black')

# back to home button
backBrandButton = tk.Button(brandNewEntryFrame, text='Back', fg='green', bg='black', font=('OCR A Extended', 12),
                            command=lambda: show_frame(homeFrame))
backBrandButton.place(relx=0.1, rely=0.1, relwidth=0.05)

# page title
brandLabel = tk.Label(brandNewEntryFrame, text='BR4ND N3W 3NTRY', fg='green', bg='black', font=('OCR A Extended', 24))
brandLabel.place(relx=0.375, rely=0.1, relwidth=0.25)

# label for siteBrandEntry text input
siteBrandLabel = tk.Label(brandNewEntryFrame, text='Enter site or app name here:', fg='green', bg='black',
                          font=('OCR A Extended', 10))
siteBrandLabel.place(relx=0.44, rely=0.166, relwidth=0.12, relheight=0.05)

# text input for site/app name
siteBrandEntry = tk.Entry(brandNewEntryFrame)
siteBrandEntry.place(relx=0.425, rely=0.2, relwidth=0.15)

# label for siteBrandEntry text input
usernameBrandLabel = tk.Label(brandNewEntryFrame, text='Enter username here:', fg='green', bg='black',
                              font=('OCR A Extended', 10))
usernameBrandLabel.place(relx=0.44, rely=0.266, relwidth=0.12, relheight=0.05)

# text input for username/email
usernameBrandEntry = tk.Entry(brandNewEntryFrame)
usernameBrandEntry.place(relx=0.425, rely=0.3, relwidth=0.15)

# label for siteBrandEntry text input
passwordBrandLabel = tk.Label(brandNewEntryFrame, text='Enter password here:', fg='green', bg='black',
                              font=('OCR A Extended', 10))
passwordBrandLabel.place(relx=0.44, rely=0.366, relwidth=0.12, relheight=0.05)

# text input for password
pwBrandEntry = tk.Entry(brandNewEntryFrame)
pwBrandEntry.place(relx=0.425, rely=0.4, relwidth=0.15)

# button to create password for user and put it in textbox
createPasswordBrandButton = tk.Button(brandNewEntryFrame, text='Create Password', font=('OCR A Extended', 7),
                                      bg='black', fg='green')
createPasswordBrandButton.place(relwidth=0.05, relx=0.425, rely=0.42)

# button to copy contents of textbox to clipboard (same as CTRL+C)
clipboardBrandButton = tk.Button(brandNewEntryFrame, text='Copy to Clipboard', font=('OCR A Extended', 7),
                                 bg='black', fg='green')
clipboardBrandButton.place(relwidth=0.05, relx=0.525, rely=0.42)

# submit button
submitBrandButton = tk.Button(brandNewEntryFrame, text='Submit', font=('OCR A Extended', 12),
                              bg='black', fg='green')
submitBrandButton.place(relx=0.475, rely=0.5, relwidth=0.05)

# ================ NEW EXISTING ACCOUNT FRAME CODE ================#
newExistingAccountFrame = tk.Frame(window, bg='black')

existingLabel = tk.Label(newExistingAccountFrame, text='4DD 3X1ST1NG 4CCOUNT', fg='green', bg='black',
                         font=('OCR A Extended', 24))
existingLabel.place(relx=0.375, rely=0.1, relwidth=0.25)

# back to home button
backExistingButton = tk.Button(newExistingAccountFrame, text='Back', fg='green', bg='black',
                               font=('OCR A Extended', 12), command=lambda: show_frame(homeFrame))
backExistingButton.place(relx=0.1, rely=0.1, relwidth=0.05)

# label for siteBrandEntry text input
siteExistingLabel = tk.Label(newExistingAccountFrame, text='Enter site or app name here:', fg='green', bg='black',
                             font=('OCR A Extended', 10))
siteExistingLabel.place(relx=0.44, rely=0.166, relwidth=0.12, relheight=0.05)

# text input for site/app name
siteExistingEntry = tk.Entry(newExistingAccountFrame)
siteExistingEntry.place(relx=0.425, rely=0.2, relwidth=0.15)

# label for siteBrandEntry text input
usernameExistingLabel = tk.Label(newExistingAccountFrame, text='Enter username here:', fg='green', bg='black',
                                 font=('OCR A Extended', 10))
usernameExistingLabel.place(relx=0.44, rely=0.266, relwidth=0.12, relheight=0.05)

# text input for username/email
usernameExistingEntry = tk.Entry(newExistingAccountFrame)
usernameExistingEntry.place(relx=0.425, rely=0.3, relwidth=0.15)

# label for siteBrandEntry text input
passwordExistingLabel = tk.Label(newExistingAccountFrame, text='Enter password here:', fg='green', bg='black',
                                 font=('OCR A Extended', 10))
passwordExistingLabel.place(relx=0.44, rely=0.366, relwidth=0.12, relheight=0.05)

# text input for password
pwExistingEntry = tk.Entry(newExistingAccountFrame)
pwExistingEntry.place(relx=0.425, rely=0.4, relwidth=0.15)

# submit button
submitExistingButton = tk.Button(newExistingAccountFrame, text='Submit', font=('OCR A Extended', 12),
                                 bg='black', fg='green')
submitExistingButton.place(relx=0.475, rely=0.45, relwidth=0.05)

# ================ EDIT ENTRY FRAME CODE ================#
editEntryFrame = tk.Frame(window, bg='black')

editEditLabel = tk.Label(editEntryFrame, text='Edit Entry', fg='green', bg='black', font=('OCR A Extended', 24))
editEditLabel.place(relx=0.375, rely=0.1, relwidth=0.25)

# back to home button
backButton = tk.Button(editEntryFrame, text='Back', fg='green', bg='black', font=('OCR A Extended', 12),
                       command=lambda: show_frame(homeFrame))
backButton.place(relx=0.1, rely=0.1, relwidth=0.05)

# ================ VIEW ENTRIES FRAME CODE ================#
viewEntriesFrame = tk.Frame(window, bg='black')

viewLabel = tk.Label(viewEntriesFrame, text='HOM3', fg='green', bg='black', font=('OCR A Extended', 24))
viewLabel.place(relx=0.375, rely=0.1, relwidth=0.25)

# back to home button
backViewButton = tk.Button(viewEntriesFrame, text='Back', fg='green', bg='black', font=('OCR A Extended', 12),
                           command=lambda: show_frame(homeFrame))
backViewButton.place(relx=0.1, rely=0.1, relwidth=0.05)

# ================ VIEW SINGLE ENTRY FRAME CODE ================#
viewSingleEntryFrame = tk.Frame(window, bg='black')

for frame in (loginFrame, homeFrame, brandNewEntryFrame, newExistingAccountFrame, editEntryFrame, viewEntriesFrame,
              viewSingleEntryFrame):
    frame.place(relwidth=1, relheight=1)

show_frame(loginFrame)
window.mainloop()
