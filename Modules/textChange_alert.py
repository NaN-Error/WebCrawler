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


def main(): #change name or 
    
    Start_Program_Time = time.time()
    # Define a function to start the search
    def start():
        
        # Get the URL from the url_entry widget
        url = url_entry.get()
        # Check if the URL is valid
        if not check_url(url):
            # If the URL is invalid, show an error message and return
            text_widget.insert('end', f'ERROR: Invalid URL\n')
            return

        # Clear the textbox
        text_widget.delete("1.0", "end")

        # Disable the "Start" button
        start_button.config(state='disabled')

        # Enable the "Stop" button
        stop_button.config(state='normal')

        # Run the search() function in a separate thread, passing the url argument
        thread = threading.Thread(target=search, args=(url,))
        thread.start()

    # Define a function to stop the search
    def stop():
        # Use the after() method to schedule the enable_start_button() function to be run in the main thread
        window.after(0, enable_start_button)

        # Set the search_active flag to False
        global search_active
        search_active = False
        global stopped_by_user
        stopped_by_user = True
        
        # Use the after() method to schedule the insertion of the text in the text widget to be run in the main thread
        text_widget.after(0, text_widget.insert, 'end', 'Search canceled by user.')
        text_widget.see(tk.END)

    def enable_start_button():
        # Enable the "Start" button
        start_button.config(state='normal')

        # Disable the "Stop" button
        stop_button.config(state='disabled')
        
    # Define a function to check if every entry widget has some input
    def check_entry_inputs(event=None):
        # Check if every entry widget has some input
        if url_entry.get() and search_text_entry.get() and first_retry_entry.get() and last_retry_entry.get():
            # If every entry widget has some input, enable the "Start" button
            start_button.config(state='normal')
        else:
            # If any entry widget is empty, disable the "Start" button
            start_button.config(state='disabled')
    
    # Define a function to validate the input in the entry widgets
    def validate_input(new_input):
        # Return True if the new input is a number, False otherwise
        return bool(only_numbers_regex.match(new_input))
    
    # Define a function to check if the URL has a valid structure
    def check_url(url):
        try:
            result = urllib.parse.urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    # Create the main window
    window = tk.Tk()
    window.title("Search Webpage")

    # Set the pack_propagate option of the window widget to False
    window.pack_propagate(False)

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

    # Create a button to start the search
    start_button = tk.Button(window, text="Start", state='disabled', command=start)
    start_button.pack()

    # Create a button to stop the search
    stop_button = tk.Button(window, text="Stop", state='disabled', command=stop)
    stop_button.pack()


    # Create a Text widget and a Scrollbar widget
    text_widget = tk.Text(window)
    scrollbar = tk.Scrollbar(text_widget, orient='vertical', command=text_widget.yview)

    # Set the yscrollcommand of the Text widget to the set method of the Scrollbar widget
    text_widget['yscrollcommand'] = scrollbar.set

    # Pack the Scrollbar widget and the Text widget
    text_widget.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')
    
    # Define the search() function to append the search information to the Text widget
    def search(url):
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
                    End_Program_Time = time.time()
                    # If the search text is found, open the webpage in the default web browser
                    webbrowser.open(url)      
                    text_widget.delete(1.0, tk.END)
                    text_widget.insert('end', f'Search finished. \n\nText "{search_text}" found on {url}\n\n')
                    text_widget.insert('end', f'Time to complete search: {int(End_Program_Time - Start_Program_Time)} seconds.\nNumber of attempts: {attempt}\n')
                    
                    # Set the search_active flag to False to stop the search
                    search_active = False
                    
                    # Disable the "Start" button
                    start_button.config(state='normal')

                    # Enable the "Stop" button
                    stop_button.config(state='disabled')
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

        # Run the main loop of the Tkinter GUI
    
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


