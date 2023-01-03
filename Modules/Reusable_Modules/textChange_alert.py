import requests
import re
import tkinter.messagebox as tk
import tkinter as tk
import webbrowser


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

# Create a Label and an Entry widget to request the search text
search_text_label = tk.Label(window, text="Enter the search text:")
search_text_label.pack()
search_text_entry = tk.Entry(window)
search_text_entry.pack()


# Define a function to search the HTML for the search text
def search(event=None):
    # Get the URL and the search text from the Entry widgets
    url = url_entry.get()
    search_text = search_text_entry.get()
    
    # Access the URL
    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
    except requests.exceptions.RequestException as e:
        # If there is an error accessing the URL, show a popup message
        root = tk.Tk()
        root.withdraw()
        tk.messagebox.showerror("Error", e)
        exit()

    # Search the HTML for the search text
    if re.search(search_text, html, re.IGNORECASE):
        # If the search text is found, open the URL in a new tab in Chrome
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
        webbrowser.get('chrome').open_new_tab(url)
    else:
        # If the search text is not found, show a popup message
        root = tk.Tk()
        root.withdraw()
        tk.messagebox.showinfo("Result", "Not found")

#"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# Create a Button to search the HTML
button = tk.Button(window, text="Search", command=search)
button.pack()

# Bind the <Return> event to the search function
url_entry.bind("<Return>", search)

# Bind the <Return> event to the search function
search_text_entry.bind("<Return>", search)

button.focus_set()

# Run the main loop
window.mainloop()