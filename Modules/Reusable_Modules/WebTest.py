import urllib.request
from Modules.Reusable_Modules.OS_Files_Manager import Store_Results


def Check_URL(url):
    # Checks if site can be normally accessed, and if its not empty, and stores it in online.txt
    # If site cannot be normally accessed, stores it in unhandledcodes.txt
    # If there's a URL access error or website not found error, inform the client, but dont store it.
    # If its any other type of error, stores it in unhandlederrors.txt
    try:
        r = urllib.request.urlopen(url)
        getcode_url = urllib.request.urlopen(url).getcode()
        if getcode_url == 200: # Checks if site exist, and saves the URL and info on txt.
            print('Web page exists.')
            Site_Length = len(r.read())
            print("Site length =", Site_Length)
            print("Site length type =", type(Site_Length))
            if Site_Length > 1: # Filters out placeholder sites with no info. #36539 Y, 31872 & 32064 N
                print("Contains relevant information.")
                Results = "Online"
                Store_Results(Results, url, 0, 0)
        else:
            print("Unhandled code, see UnhandledCodes.txt for more information.")
            Results = "UnhandledCodes" 
            Store_Results(Results, url, getcode_url, 0)
    except urllib.error.URLError as e:  # Checks for errors in url access.
        print(e)
    except urllib.error.HTTPError as e:  # Checks for error 404, webpage not found.
        print(e)
    else:
        print("Unhandled error, see UnhandledErrors.txt for more information.")
        Results = "UnhandledErrors"
        e = urllib.error
        Store_Results(Results, url, 0, urllib.error)

# # Define a function to be called when the button is clicked
# import tkinter as tk
# def get_url():
#     global url
#     url = textbox.get()

# # Create the main window
# window = tk.Tk()

# # Create a textbox and a button
# textbox = tk.Entry(window)
# button = tk.Button(window, text="Get URL")

# # Set the command of the button to the get_url function
# button["command"] = get_url

# # Pack the widgets (arrange them in the window)
# textbox.pack()
# button.pack()

# # Start the event loop
# window.mainloop()