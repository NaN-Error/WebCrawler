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
import tkinter as tk
import webbrowser
import urllib.parse
import threading

# comments update following from line 48
# To do: add a check for captcha. when url in text or captcha in text, open window. captcha id is variable, might require a list with possible ids to evaluate. Research.

# The main function holds the gui that calls the rest of the functions. If the gui needs to be in an independent function, it would need to pass the arguments to all the other
# functions. The gui doesnt need to be on an independent fuction, so everything can be put inside a main function that contains both the gui and the other functions so no arguments
# needs to be passed. The program works either way, but the code is cleaner if gui is put in an independent function.

def main():
    # Starts the search
    def start():
        # Gets the URL from the url_entry widget
        url = url_entry.get()
        # Checks if the URL is invalid. if so, shows an error message and goes back to main to wait for user action.
        if not check_url(url):
            text_widget.insert('end', f'ERROR: Invalid URL\n')
            return

        # If the URL is valid, the program does the following:
        # Clears the "terminal" textbox(text_widget)
        text_widget.delete("1.0", "end")
        # Disables the Start button and enables the Stop button.
        disable_start_button()
        # Runs the search() function in a separate thread (to avoid the gui get stuck in a loop and freeze) and passes the url argument
        thread = threading.Thread(target=search, args=(url,))
        thread.start()

    # Stops the search
    def stop():
        enable_start_button()

        # Sets the search_active flag to False - TO DO: reevaluate for redundancies.
        global search_active
        search_active = False
        global stopped_by_user
        stopped_by_user = True
        
        # Shows a "Search Canceled by user" message in the text widget when the Stop button is pressed.
        text_widget.insert('end', "\n____________________________________________END____________________________________________________\n")
        text_widget.insert('end', "\n\n----SEARCH CANCELED BY USER----.\n\n")
        text_widget.insert('end', "____________________________________________END____________________________________________________\n")
        text_widget.see(tk.END)

    # Enables the "Start" button and text fields, and disables the "Stop" button when the "Stop" button is pressed and when the program ends.
    def enable_start_button():
        # Enables Start button/Disables Stop button
        start_button.config(state='normal')
        stop_button.config(state='disabled')
        # Enables text fields.
        url_entry.config(state='normal')
        search_text_entry.config(state='normal')
        first_retry_entry.config(state='normal')
        last_retry_entry.config(state='normal')
    
    # Disables the "Start" button and text fields, and enables the "Stop" button when the "Start" button is pressed.
    def disable_start_button():
        # Disables Start button/Enables Stop button.
        start_button.config(state='disabled')
        stop_button.config(state='normal')
        # Disables text fields.
        url_entry.config(state='disabled')
        search_text_entry.config(state='disabled')
        first_retry_entry.config(state='disabled')
        last_retry_entry.config(state='disabled')
    
    # Function to actively check if every text widget has some input; Start button is enabled if it does and disabled if it doesn't. 
    # Used by the Bind function to actively check whenever an input is made in the text fields.
    def check_entry_inputs(event=None):
        # Check if every entry widget has some input.
        if url_entry.get() and search_text_entry.get() and first_retry_entry.get() and last_retry_entry.get():
            # If every entry widget has some input, enable the "Start" button.
            start_button.config(state='normal')
        else:
            # If any entry widget is empty, disable the "Start" button
            start_button.config(state='disabled')
    
    # Validate the input for numbers only in the first retry entry and last retry entry textboxes
    def validate_input(new_input):
        # Return True if the new input is blank (to allow deleting all the numbers if wanted), and checks if the new input matches the regex. If matches, returns true, else false.
        # When True, it allows the input in the textbox, when false, no input is allowed into the textbox.
        if new_input == "":
            return True
        return bool(only_numbers_regex.match(new_input))
    
    # Check if the URL has a valid structure
    def check_url(url):
        try:
            result = urllib.parse.urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
    
    # Define the search() function to append the search information to the Text widget
    def search(url):
        # For testing purposes - stores the time when the program starts - to check execution time. // TO DO - use at sub modules execution instead
        Start_Program_Time = time.time()
        
        # Initialize the search attempt counter
        attempt = 1

        # Get the search text and retry intervals from the entry widgets
        search_text = search_text_entry.get()
        first_retry = int(first_retry_entry.get())
        last_retry = int(last_retry_entry.get())

        # Set the search_active flag to True
        global search_active
        search_active = True
        
        global stopped_by_user
        stopped_by_user = False
        
        while search_active:
            # Generate a random interval of time within the retry intervals
            retry_interval = random.randint(first_retry, last_retry)

            # Append the search information to the Text widget
            text_widget.insert('end', f'Attempt {attempt}: Searching for "{search_text}" in {url[:25]}...{url[-20:]}\n')
            
            lines = text_widget.get(1.0, tk.END).strip("\n")
            
            #save everything from the text_widget, then create a loop, 
            time_left = retry_interval
            
            while time_left >= 0 and stopped_by_user == False:
                text_widget.delete(1.0, tk.END)
                text_widget.insert('end', f'{lines}\n')
                text_widget.insert('end', f'Waiting for {time_left} seconds\n')#instead of retry_interval, make it timeretry
                text_widget.see(tk.END)
                time_left -= 1
                # Wait for the random interval of time
                time.sleep(1.0) #make it 1 second insted of retry_interval
                #needs to be interrupted by the stop button
                    #can be done using flag or checking the last text in the text widget and compare it in the while... or
            
            # Send a GET request to the URL
            try:
                response = requests.get(url)
                    # Search the content of the webpage for the search text
                if search_text in response.text:
                    # If the search text is found, open the webpage in the default web browser
                    webbrowser.open(url)      
                    text_widget.delete(1.0, tk.END)
                    text_widget.insert('end', f'Search finished. \n\nText "{search_text}" found on {url}\n\n')
                    End_Program_Time = time.time()
                    text_widget.insert('end', f'Number of attempts: {attempt}\nTime to complete search: {int(End_Program_Time - Start_Program_Time)} seconds.\n')
                    
                    # Set the search_active flag to False to stop the search
                    search_active = False
                    
                    disable_start_button()
                else:
                    if stopped_by_user == False:
                        text_widget.delete(1.0, tk.END)
                        text_widget.insert('end', f'{lines}\n')
                        text_widget.insert('end', f'Text "{search_text}" not found on {url[:25]}...{url[-20:]}\n')#instead of retry_interval, make it timeretry
                        text_widget.insert('end', f'Retrying...\n\n')#instead of retry_interval, make it timeretry
                        text_widget.see(tk.END)
            except Exception as e:
                # If the request fails, display an error message and continue with the next attempt
                text_widget.insert('end', f'ERROR: {e}\n')
            
            # Increment the attempt counter
            attempt += 1
    
    # Create the main window
    window = tk.Tk()
    window.title("Search Webpage - Text Change Alert")

    # Sets the pack_propagate of the window to False in order for it to be able to change its own size
    window.pack_propagate(False)

    # Sets the size and position of the main window
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = screen_width // 2
    window_height = screen_height // 2
    window_x = screen_width // 2 - window_width // 2
    window_y = screen_height // 2 - window_height // 2
    window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    # Creates a Label and a text widget to request the URL
    url_label = tk.Label(window, text="Enter the URL:")
    url_label.pack()
    url_entry = tk.Entry(window)
    url_entry.pack()

    # Creates a Label and a text widget to request the text to search.
    search_text_label = tk.Label(window, text="Enter the search text:")
    search_text_label.pack()
    search_text_entry = tk.Entry(window)
    search_text_entry.pack()
    
    # To do: make first and last be side by side, smaller, total size of both same as one button.
    # Creates a Label and two text widgets to request the retry intervals
    retry_label = tk.Label(window, text="Enter the retry intervals (in seconds):")
    retry_label.pack()
    first_retry_entry = tk.Entry(window, validate='key', validatecommand=(window.register(validate_input), '%P'))
    last_retry_entry = tk.Entry(window, validate='key', validatecommand=(window.register(validate_input), '%P'))
    first_retry_entry.pack()
    last_retry_entry.pack()
    
    # Button to start the search
    start_button = tk.Button(window, text="Start", state='disabled', command=start)
    start_button.pack()

    # Button to stop the search
    stop_button = tk.Button(window, text="Stop", state='disabled', command=stop)
    stop_button.pack()

    # Creates a Text widget and a Scrollbar widget
    text_widget = tk.Text(window)
    
    # Sets a scrollbar in the text_widget to scroll thru all the test text
    scrollbar = tk.Scrollbar(text_widget, orient='vertical', command=text_widget.yview)
    text_widget['yscrollcommand'] = scrollbar.set
    text_widget.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')
    
    # Create a regular expression to match only digits
    only_numbers_regex = re.compile(r'^\d+$')
    
    # Checks for inputs in the textboxes url_entry, search_text_entry, first_retry_entry and last_retry_entry 
    url_entry.bind('<KeyRelease>', check_entry_inputs)
    search_text_entry.bind('<KeyRelease>', check_entry_inputs)
    first_retry_entry.bind('<KeyRelease>', check_entry_inputs)
    last_retry_entry.bind('<KeyRelease>', check_entry_inputs)
    
    # Binds the Enter key to the Start button so Enter can be pressed to start the program when all the texboxes has some text.
    window.bind('<Return>', lambda event: start_button.invoke())
    
    window.mainloop()
    

# import requests
# from bs4 import BeautifulSoup

# # Access the webpage
# response = requests.get(url)
# html = response.text

# # Parse the HTML
# soup = BeautifulSoup(html, 'html.parser')

# # Search for the CAPTCHA element
# captcha_element = soup.find(id='captcha-form')

# if captcha_element:
#     # CAPTCHA element was found
#     print("CAPTCHA found")
# else:
#     # CAPTCHA element was not found
#     print("CAPTCHA not found")
# This code will search the HTML for an element with the id captcha-form and print "CAPTCHA found" if the element is found, or "CAPTCHA not found" if it is not found. You can modify the code to search for other elements or classes that may indicate the presence of a CAPTCHA.

# Keep in mind that this approach may not always be reliable, as the webpage may use a CAPTCHA that is not detected by this method or may use other methods to block automated access to the webpage.

# captcha
# g-recaptcha
# captcha-form
# captcha-input
# captcha-image


