"""This code defines two functions for managing text files and storing results in them.

The Clear_Files function removes three files (Online.txt, UnhandledCodes.txt, and UnhandledErrors.txt) from the Databases/ directory if they exist.

The Store_Results function takes three arguments: Results, url, and Unhandled_Error. 
It opens one of three text files (depending on the value of Results) in the Databases/ directory, and writes a message to the file containing the value of url and Unhandled_Error. 
If Results is "Online", the message written to the file is "Webpage: URL", where URL is the value of url. 
If Results is "UnhandledCodes", the message written to the file is "Unhandled Code: CODE - Webpage: URL", where CODE is the value of getcode_url and URL is the value of url. 
If Results is "UnhandledErrors", the message written to the file is "Unhandled Error: ERROR - Webpage: URL", where ERROR is the value of Unhandled_Error and URL is the value of url.
"""


from pathlib import Path 
import os 
#import mysql.connector

# To do: change txt for db. db should have url(str), found(bool), unhandled_code(str), unhandled_error(str)

#Path to the directory where the program stores its files.
Databases_Path = Path("Databases/")

def Clear_Files(): 
    # Checks if the file exists, and remove it if it does. Executed at the beginning of each run to clear the previous stored info.
    if os.path.isfile(Databases_Path / 'Online.txt'):
        os.remove(Databases_Path / 'Online.txt')
    if os.path.isfile(Databases_Path / 'UnhandledCodes.txt'):
        os.remove(Databases_Path / 'UnhandledCodes.txt')
    if os.path.isfile(Databases_Path / 'UnhandledErrors.txt'):
        os.remove(Databases_Path / 'UnhandledErrors.txt')

    
def Store_Results(Results, url, getcode_url, Unhandled_Error):
    """
Stores the URL check results.
Results: String - The result of the URL check.
url: String - The URL that was checked.
getcode_url: String - The HTTP status code received when checking the URL.
Unhandled_Error: Object - An unhandled error that occurred while checking the URL.
"""
    # Checks the result of the URL check, and store it in the corresponding file.
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