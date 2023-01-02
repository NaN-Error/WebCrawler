import time # To get the execution time of the program.
Start_Program_Time = time.time()
import Modules.Find_Sites # Local module. Contains unclassified functions used by main.
import tkinter as tk

#rethink, why do I need tkinter for? 

# Create the main window
window = tk.Tk()
window.title("Radio Button Example")

# Set the size and position of the main window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = screen_width // 2
window_height = screen_height // 2
window_x = screen_width // 2 - window_width // 2
window_y = screen_height // 2 - window_height // 2

# Set the size and position of the new window
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Create a Tkinter variable to store the selected radiobutton
choice = tk.StringVar()

# Create the radiobuttons
radiobutton1 = tk.Radiobutton(window, text="1. Find webpages of a website using bf", variable=choice, value="radiobutton1")
radiobutton2 = tk.Radiobutton(window, text="2. Find all links of a website", variable=choice, value="radiobutton2")

# Pack the radiobuttons
radiobutton1.pack(side=tk.TOP, anchor=tk.CENTER)
radiobutton2.pack(side=tk.TOP, anchor=tk.CENTER)

# Create a button to store the selected radiobutton
def store_choice():
    selected_choice = choice.get()
    
    if selected_choice == "radiobutton1":
        
        # Create a new window to display the selected radiobutton and the output of the test function
        new_window = tk.Tk()
        new_window.title("Selection")

        # Set the size and position of the new window
        new_window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
        
        # Call the test function and display its output in a Text widget with a Scrollbar
        text = tk.Text(new_window)
        text.pack(side=tk.LEFT)
        scrollbar = tk.Scrollbar(new_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text.yview)
        
        # Call the test function and pass the Text widget as an argument
        Modules.Find_Sites.Brute_Force(text)
        
        # Bind the <Configure> event to a function that resizes the Text widget
        def resize(event):
            text.config(width=event.width, height=event.height)
        new_window.bind("<Configure>", resize)
            
    elif selected_choice == "radiobutton2":
        pass

button = tk.Button(window, text="Start", command=store_choice)
button.pack(side=tk.TOP, anchor=tk.CENTER)

# Run the main loop
window.mainloop()


End_Program_Time = time.time()
print("Time to compile:", round(End_Program_Time - Start_Program_Time, 4), "seconds.")




#_________________________________________________COMMENTS_________________________________________________

# brainstorm possible ways of reaching the end goal
# choose the most efficient, memory wise
# visualize the data flow, then describe it, then program it.

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