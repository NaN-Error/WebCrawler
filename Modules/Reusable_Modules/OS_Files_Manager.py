# Module dedicated to local file management. This module can have more functions to expand program capabilities.
from pathlib import Path # For Windows/Mac path compatibility
import os # To check, create, and remove files from OS directories.
import mysql.connector

Databases_Path = Path("Databases/")


def Clear_Files(): # Removes the txt files that contains all the URL's info. 
    if os.path.isfile(Databases_Path / 'Online.txt'):
        os.remove(Databases_Path / 'Online.txt')
    if os.path.isfile(Databases_Path / 'UnhandledCodes.txt'):
        os.remove(Databases_Path / 'UnhandledCodes.txt')
    if os.path.isfile(Databases_Path / 'UnhandledErrors.txt'):
        os.remove(Databases_Path / 'UnhandledErrors.txt')

    
def Store_Results(Results, url, getcode_url, Unhandled_Error): # Stores the URL check results.
    if Results == "Online":
        with open(Databases_Path / 'Online.txt', 'a') as f:
            f.write("Webpage: ")
            f.write(url)
            f.write('\n')
            f.close()
    elif Results == "UnhandledCodes":
        with open(Databases_Path / 'UnhandledCodes.txt', 'a') as f:
            f.write("Unhandled Code: ")
            f.write(getcode_url)
            f.write("- Webpage:")
            f.write(url)
            f.write('\n')
            f.close()
    elif Results == "UnhandledErrors":
        with open(Databases_Path / 'UnhandledErrors.txt', 'a') as f:
            f.write("Unhandled Error: ")
            f.write(str(Unhandled_Error))
            f.write("- Webpage:")
            f.write(url)
            f.write('\n')
            f.close()