import time # To get the execution time of the program.
import tkinter as tk
import tkinter.messagebox as messagebox
from Modules import Brute_Force, textChange_alert

# For testing purposes - stores the time when the program starts - to check execution time. // TO DO - use at sub modules execution instead
Start_Program_Time = time.time()

# Creates the buttons to store the selected radiobutton
def select_option(window, choice):
    selected_choice = choice.get()
    window.destroy()
    if selected_choice == "radiobutton1":
        Brute_Force.gui()
    elif selected_choice == "radiobutton2":
        messagebox.showinfo("Alert", "This function is still in process.")
        main_window()
    elif selected_choice == "radiobutton3":
        textChange_alert.main()

def main_window():
    # Tkinter main window can be made a reusable function for main.py, textChage_alert.py, Brute_Force.py, etc for next ones.
    window = tk.Tk()
    window.title("Choose an option")

    # Sets the size and position of the main window
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = screen_width // 2
    window_height = screen_height // 2
    window_x = screen_width // 2 - window_width // 2
    window_y = screen_height // 2 - window_height // 2
    window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    # Create a Tkinter variable to store the selected radiobutton
    choice = tk.StringVar()

    # TO DO - make radiobuttons aligned left
    # Creating the radiobuttons and button
    radiobutton1 = tk.Radiobutton(window, text="1. Find webpages of a website using brute force.", variable=choice, value="radiobutton1")
    radiobutton2 = tk.Radiobutton(window, text="2. Find all links of a website.", variable=choice, value="radiobutton2")
    radiobutton3 = tk.Radiobutton(window, text="3. Lookup a keyword in a webpage and open it when the keyword appears.", variable=choice, value="radiobutton3")
    radiobutton1.pack(side=tk.TOP, anchor=tk.CENTER)
    radiobutton2.pack(side=tk.TOP, anchor=tk.CENTER)
    radiobutton3.pack(side=tk.TOP, anchor=tk.CENTER)

    # Define the Button with the name Start that when pressed, gets the selected option from select_option  the window and choice arguments
    button = tk.Button(window, text="Start", command=lambda: select_option(window, choice))
    button.pack(side=tk.TOP, anchor=tk.CENTER)
    
    # TO DO - add conditional messagebox thats displayed when the user press the Start button without selecting an option
    # or - disable start button at start and enable it when a radiobutton is selected - more fluent user experience
    
    # Keeps the tkinter window "window" open.
    window.mainloop()

# For testing purposes

#textChange_alert.main()
Brute_Force.gui()

# Substract the current time from the time when the program started to check execution time. // TO DO - use at sub modules execution instead
End_Program_Time = time.time()
print("Time to compile:", round(End_Program_Time - Start_Program_Time, 4), "seconds.")


exit()


#_________________________________________________COMMENTS_________________________________________________

# brainstorm possible ways of reaching the end goal
# choose the most efficient, memory wise
# visualize the data flow, then describe it, then program it.
# make it functional, then improve it.

# To do:

# [X]Comment code
# [X]Clean code
# [X]Create functions
# [X]Modulate
# []Make functions reusable for other purposes. 
    # [] Can create a module for reusable functions, 
    # [] one module for each program functionality e.x.
        # []Check_Sites.py module with all its non reusable functions calling all rehusable functions.
        # []Main_Funtions module can be all reusable functions. rename. Change all ocurrences(Main_Functions to Reusable_Functions).
# []Optimize efficiency
    # []Reevaluate processes used.
    # []Multithread (main function)
# []Expand program capabilities
    # []GUI
    # []Database. gui for link selection (calls db to get all links in a gui list.) this list could also give some extra information
    # []About the link.
    # []Second function could be website download as pdf. 
    # []Webcrawl to id every webpage a website has, going thru all its links related to the website.
        # []Can individually download each link as pdf or can also download every link.
    # []Could web crawl to id databases on website (webpage by webpage.) gets webpages, and databases it contains.
        # []Can download all databases/database contents.
        # []Could be all databases from a given webpage, or crawl all website and get all databases from all webpages.
    # []Main should give up a gui to ask user what function the program is going to execute. 
        # []Brute force find webpages of a website, find all webpages of a website. find databases of webpage/website.
    # []Maybe organize by a module that calls the functions it needs, a module for each big function
    
# If someone has enough time and will, they can do anything.
# ___________________________________________________________________________________________________ 