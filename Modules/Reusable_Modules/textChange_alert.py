""""
This code defines a simple graphical user interface (GUI) using the tkinter library that allows the user to enter a URL and search text, 
and then searches the HTML of the webpage at the specified URL for the search text. If the search text is found, the webpage is opened in a new tab in the Chrome web browser. 

If the search text is not found, a popup message is displayed. The requests library is used to access the webpage at the specified URL, 
and the re (regular expression) library is used to search the HTML for the search text. 

The webbrowser library is used to open the webpage in a new tab in the Chrome web browser.
"""

import random
import time
import requests
import re
import tkinter.messagebox as messagebox
import tkinter as tk
import webbrowser
import urllib.parse
import threading


# Define a function to start the search
def start():
    # Disable the "Start" button
    start_button.config(state='disabled')

    # Enable the "Stop" button
    stop_button.config(state='normal')

    # Run the search() function in a separate thread
    thread = threading.Thread(target=search)
    thread.start()

# Define a function to stop the search
def stop():
    # Enable the "Start" button
    start_button.config(state='normal')

    # Disable the "Stop" button
    stop_button.config(state='disabled')

    # Set the search_active flag to False
    global search_active
    search_active = False
    
# Define a function to check if every entry widget has some input
def check_entry_inputs(event=None):
    # Check if every entry widget has some input
    if url_entry.get() and search_text_entry.get() and first_retry_entry.get() and last_retry_entry.get():
        # If every entry widget has some input, enable the "Start" button
        start_button.config(state='normal')
    else:
        # If any entry widget is empty, disable the "Start" button
        start_button.config(state='disabled')


# Create the main window
window = tk.Tk()
window.title("Search Webpage")

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window size to 50% of the screen size
window.geometry(f"{screen_width//2}x{screen_height//2}")

# Create a Label and an Entry widget to request the URL
url_label = tk.Label(window, text="Enter the URL:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

# Bind the <KeyRelease> event of the url_entry widget to the check_entry_inputs() function
url_entry.bind('<KeyRelease>', check_entry_inputs)

# Create a Label and an Entry widget to request the search text
search_text_label = tk.Label(window, text="Enter the search text:")
search_text_label.pack()
search_text_entry = tk.Entry(window)
search_text_entry.pack()

# Bind the <KeyRelease> event of the search_text_entry widget to the check_entry_inputs() function
search_text_entry.bind('<KeyRelease>', check_entry_inputs)

# Create a Label and two Entry widgets to request the retry intervals
retry_label = tk.Label(window, text="Enter the retry intervals (in seconds):")
retry_label.pack()

# Create a regular expression to match only digits
only_numbers_regex = re.compile(r'^\d+$')

# Define a function to validate the input in the entry widgets
def validate_input(new_input):
    # Return True if the new input is a number, False otherwise
    return bool(only_numbers_regex.match(new_input))

# Set the 'validate' and 'validatecommand' options of the entry widgets
first_retry_entry = tk.Entry(window, validate='key', validatecommand=(window.register(validate_input), '%P'))
last_retry_entry = tk.Entry(window, validate='key', validatecommand=(window.register(validate_input), '%P'))

# Pack the entry widgets
first_retry_entry.pack()
last_retry_entry.pack()

# Bind the <KeyRelease> event of the first_retry_entry widget to the check_entry_inputs() function
first_retry_entry.bind('<KeyRelease>', check_entry_inputs)

# Bind the <KeyRelease> event of the last_retry_entry widget to the check_entry_inputs() function
last_retry_entry.bind('<KeyRelease>', check_entry_inputs)

# Define a function to check if the URL has a valid structure
def check_url(url):
    try:
        result = urllib.parse.urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# Create a button to start the search
start_button = tk.Button(window, text="Start", state='disabled', command=start)
start_button.pack()

# Create a button to stop the search
stop_button = tk.Button(window, text="Stop", state='disabled', command=stop)
stop_button.pack()

# Define a flag variable to control the search loop
search_active = True

# Define a function to search the HTML for the search text
def search():
    global search_active
    # Get the URL, search text, and retry intervals from the Entry widgets
    url = url_entry.get()
    search_text = search_text_entry.get()
    first_retry = int(first_retry_entry.get())
    last_retry = int(last_retry_entry.get())

    # User agent string
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

    # Check if the URL has a valid structure
    if check_url(url):
        while search_active:
            # Send a GET request to the URL with the spoofed user agent string
            response = requests.get(url, headers=headers)

            # Check if the search text is found in the HTML
            if search_text in response.text:
                # If the search text is found, open the URL in a new tab in Chrome
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
                webbrowser.get('chrome').open_new_tab(url)

                # Stop the search
                search_active = False
            else:
                # If the search text is not found, wait for a random amount of time between the first and last retry intervals (in seconds) before trying again
                time.sleep(random.randint(first_retry, last_retry))
    else:
        # If the URL has an invalid structure, show an error message
        messagebox.showerror("Error", "The URL has an invalid structure")

# Run the main loop of the Tkinter GUI
window.mainloop()