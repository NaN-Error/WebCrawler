import string # To get the characters and numbers to create the URLs.
import time # To get the execution time of the program.
from Modules.Reusable_Modules import WebTest # Local module. To check each URL created, store the ones online, and store Web error messages, if any.
from Modules.Reusable_Modules import OS_Files_Manager # Local module. Deletes files created in previous runs.
import urllib.parse
import re
import threading
import tkinter as tk

#visualize it, describe it, code it.
#make it functional, then improve it.

#To do:
# insert an initial focus on text_widget
# checkboxes to ask for lists to use.
# needs a button to pause

# New functions to add after:

# if none of the url column is with lenght arraysofarray2d and with all its elements the last element of Unum
    # in the last run you were creating the list with which the test were going to be made. do you wish to continue?
        # no 
            # starts anew
        # yes 
            # gets previous data. needs data to be stored in hard drive. needs a function to store this data, and a function to clear this data.
# elif 
    # in the last run you were testing the webpages with the list created. do you wish to continue?
        # no 
            # do you want to create a new list?
                # no > close
                # yes > start anew
        # yes > gets db data from those rows who doesnt have data input in its tests rows.

# a button to continue from last test. (clear() function would have to be deleted. Store everything inside a db insead of txt)
# db used to id the last input. all url test are made, and columns should id if found, if not, if error etc. true false info?
# needs an intro gui to detect if theres data stored, if to continue last test or start over. start over deletes the db, continue gets last url.
# can multithreading be used to sort the database while the program is also inputing data on the database? or enter the data in the db in its place so its sorted?

# Check which functions can be reused, and move them to Reusable_Modules.Functions or similar, rethink when building new program functionality.
# most of gui can probably be reused. check tkinter options to do this.

#add a gui to input 
def gui():
    # Defining objects of the gui
    Start_Program_Time = time.time()
    # Starts the search
    def start():
        # Gets the URL from the url_entry widget
        url = url_entry.get()
        # Checks if the URL is invalid. if so, shows an error message and returns
        if not check_url(url):
            text_widget.insert('end', f'ERROR: Invalid URL\n')
            return

        # If the URL is valid, the program does the following:
        
        Arrays_Of_Array2D = int(search_text_entry.get())
        # Clears the textbox
        text_widget.delete("1.0", "end")
        # Disables the Start button and enables the Stop button.
        disable_start_button()
        # Runs the search() function in a separate thread (to avoid the gui get stuck in a loop and freeze) and passes the url argument
        thread = threading.Thread(target=main, args=(Arrays_Of_Array2D, url))
        thread.start()

    # Stops the search
    def stop():
        enable_start_button()

        # Set the search_active flag to False
        global search_active
        search_active = False
        global stopped_by_user
        stopped_by_user = True
        
        # Use the after() method to schedule the insertion of the text in the text widget to be run in the main thread
        text_widget.insert('end', "\n____________________________________________END____________________________________________________\n")
        text_widget.insert('end', "\n\n----SEARCH CANCELED BY USER----.\n\n")
        text_widget.insert('end', "____________________________________________END____________________________________________________\n")
        text_widget.see(tk.END)

    # Enables the "Start" button and disables the "Stop" button. Used when the "Stop" button is pressed.
    def enable_start_button():
        start_button.config(state='normal')
        stop_button.config(state='disabled')
        
        url_entry.config(state='normal')
        search_text_entry.config(state='normal')
    
    
    def disable_start_button():
        start_button.config(state='disabled')
        stop_button.config(state='normal')
        
        url_entry.config(state='disabled')
        search_text_entry.config(state='disabled')
    
    # Define a function to check if every entry widget has some input
    def check_entry_inputs(event=None):
        # Check if every entry widget has some input
        if url_entry.get() and search_text_entry.get():
            # If every entry widget has some input, enable the "Start" button
            start_button.config(state='normal')
        else:
            # If any entry widget is empty, disable the "Start" button
            start_button.config(state='disabled')
    
    # Define a function to validate the input in the entry widgets
    def validate_input(new_input):
        # Return True if the new input is a number, False otherwise
        if new_input == "":
            return True
        return bool(only_numbers_regex.match(new_input))
    
    # Define a function to check if the URL has a valid structure
    def check_url(url):
        try:
            result = urllib.parse.urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
    
    
    def main(Arrays_Of_Array2D, domain_name):# 1. - Checks which webpages exist, using brute force.
        # gui  
        # continue? if data stored, if yes, continue, if not, clear_files(), else #works with both url maker and url lookup.
        # calls websiteurlinput() # asks website url. look at the end of code.
        # checklist make urls, lookup urls. 
        # checklist store urls that exist, store url that doesnt exist (db should specify on column "exist" as boolean true false.), store errors founds on urls.
        
        
        # Removes the txt files that contains all the URL's info. 
        OS_Files_Manager.Clear_Files() 
        # After every run, the txt files needs to be kept for evaluation, so they need to be removed at the beginning of the rerun of the program.

        text_widget.insert('end', "_____________________________________Initializing_Arrays___________________________________________\n")

        # Assign all the elements of all the lists selected in E_Ploribus_Unum() into Unum_List.
        Unum_List = E_Ploribus_Unum()

        # Initialize Array2D with the amount of arrays specified(Arrays_Of_Array2D), and the elements of every array.
        Arrays_Of_Array2D, Array2D, URL_Subdirectory_Test = Initializing_Arrays(Unum_List, Arrays_Of_Array2D)

        text_widget.insert('end', "___________________________________________START___________________________________________________\n")

        
        # Evaluates every combination of selected characters.
        Start_URL_Tests(Unum_List, Arrays_Of_Array2D, Array2D, URL_Subdirectory_Test, domain_name)
        


    def Initializing_Arrays(Unum_List, Arrays_Of_Array2D): # 1.2 - Initializes Array2D and URL_Subdirectory_Test(Array1D)
        # This can be a single user input, maybe in a textbox to define lenght of test.
        

        # Initializes the dimensions of the multidimensional array using Arrays_Of_Array2D as the amount of arrays
        # And with Unum_List as the elements every array in the multidimensional array will contain.
        Array2D = [[0 for i in range(len(Unum_List))] for i in range(Arrays_Of_Array2D)]
        # Array2D doesnt change or store anything, its only purpose is to scroll thru its elements.

        text_widget.insert('end', "___________________________________________________________________________________________________\n")
        text_widget.insert('end', "Dimensions of Array2D initialized.\n\n")
        text_widget.insert('end', f"Count of items inside Array2D 0: {len(Array2D[0])}\n")
        text_widget.insert('end', "The items inside each Array2D are initialized to 0\n")
        text_widget.insert('end', f"Count of arrays inside Array2D: {len(Array2D)}\n")
        text_widget.insert('end', "___________________________________________________________________________________________________\n")

        # Adds the elements of Unum_List to every array of Array2D.
        for i in range(Arrays_Of_Array2D):
            for j in range(len(Unum_List)):
                Array2D[i][j] = Unum_List[j]

        text_widget.insert('end', "___________________________________________________________________________________________________\n")
        text_widget.insert('end', "Items of Array2D initialized.\n\n")
        text_widget.insert('end', f"Count of items inside Array2D 0: {len(Array2D[0])}\n")
        text_widget.insert('end', "The items inside each Array2D are initialized to contain a-z, A-Z, and 0-9\n")
        text_widget.insert('end', f"Count of arrays inside Array2D: {len(Array2D)}\n")
        text_widget.insert('end', "___________________________________________________________________________________________________\n")
        
        # Creates a 1 dimension array and makes it as long as the amount of arrays in Array2D, and makes every element to be empty "".
        URL_Subdirectory_Test = [""] * Arrays_Of_Array2D   
        
        return Arrays_Of_Array2D, Array2D, URL_Subdirectory_Test


    def Start_URL_Tests(Unum_List, Arrays_Of_Array2D, Array2D, URL_Subdirectory_Test, domain_name): # 1.3 - Evaluates every combination of selected characters.
        # Set the search_active flag to True
        global search_active
        search_active = True
        global stopped_by_user
        stopped_by_user = False
        #optimize - remove the following while search active and remove the else break from i < arrays from arrays2d...?
        
        while search_active:#this might keep the loop running without ending after completion.
            
            text_widget.see(tk.END)
            
            # For testing purposes.
            Iteration_Count = 0 

            # To id when the program should go back to array 1(index 0).
            IsZero = True 
            i = 0 

            # While instead of a for. The for didn't allowed to modify i when it was inside another loop and if. # Testing while as a for.
            while i < Arrays_Of_Array2D: 
                
                text_widget.see(tk.END)
                
                if stopped_by_user == True:
                    break
                i += 1
                
                if IsZero == True:
                    i = 0
                IsZero = False
                text_widget.insert('end', "___________________________________________________________________________________________________\n")
                text_widget.insert('end', f"From i = 0 to i = {Arrays_Of_Array2D - 1}|  {i} = i\n")
                text_widget.insert('end', "___________________________________________________________________________________________________\n")
                
                for j in range(len(Unum_List)):
                    
                    text_widget.see(tk.END)
                    
                    if stopped_by_user == True:
                        break
                    Iteration_Count += 1
                    
                    # Clears the contents of the string URL_Subdirectory before using it.
                    URL_Subdirectory = ""
                    # Every time URL_Subdirectory_Test is modified, its more efficient and simpler to use a string than an array.
                    
                    text_widget.insert('end', '\n')
                    text_widget.insert('end', f"Iteration # {Iteration_Count}\n")
                    text_widget.insert('end', f"From j = 0 to j = {len(Unum_List)} - 1 | i = {i} & j = {j}\n")
                    text_widget.insert('end', "________\n")
                    text_widget.insert('end', '\n')
                    
                    # Most important line in this program. 
                    URL_Subdirectory_Test[i] = Array2D[i][j]  
                    # As Array2D changes positioning thru its elements, they are stored on the 1d array. 
                    # URL_Subdirectory_Test is like an overlay of Array2D that will save the elements Array2D is going thru.
                    
                    # Stores all the elements of the list URL_Subdirectory_Test on the string variable URL_Subdirectory
                    text_widget.insert('end', "URL_Subdirectory_Test = ")
                    for k in range(len(URL_Subdirectory_Test)): 
                        text_widget.insert('end', URL_Subdirectory_Test[k])
                        URL_Subdirectory = URL_Subdirectory + str(URL_Subdirectory_Test[k])
                    text_widget.insert('end', '\n')
                    
                    # Creates the complete url to test
                    #url can be input variable, and 2nd subdirectory can be added as input variable too
                    url = domain_name + URL_Subdirectory #+ "=" .
                    text_widget.insert('end', f'URL = {url}\n')
                    
#insert a focus on end of text_widget
                    
                    
                    
                    # If website exist, saves the URL on txt.
                    
                    line = WebTest.Check_URL(url)
                    if stopped_by_user != True:
                        text_widget.insert('end', f"{line}")
                        text_widget.insert('end', "___________________________________________________________________________________________________\n")
                        
                        #si todos los elementos de urlsubdir son el ultimo valor de array2d, end.
                        
                        # first option: on while increasing i to get to the next array, if all arrays has the last value, then end.
                        # second option: on array declaration function, create a variable initialized with the value of the last URL_Subdirectory_Test. e.x. 99999 if its 5 arrays.
                        
                        
                        #if URL_Subdirectory_Test[] or URL_Subdirectory == Arrays_Of_Array2D-1:
                            #text_widget.insert('end', "end")
                            #pass #has to end program if i has reached its end. also make 1d and 2d arrays empty again.
                        #either here or inside while increasing.
                        if j == len(Unum_List)-1: #si llega al final, va al proximo array, si es 9 va al proximo array etc etc y si no es 9, aumenta 1 e i-- j =0 so on hasta que i =0
                            IsZero, i = Increase_To_Next_Option(i, j, Arrays_Of_Array2D, URL_Subdirectory_Test, Array2D, Unum_List)
                        #put this inside the run to only execute after it gets out of the while of i < arrayofarrays2d else:
            else:
                text_widget.insert('end', "____________________________________________END____________________________________________________\n")
                text_widget.insert('end', '\n')
                text_widget.insert('end', f"Count of items inside Array2D[0]: {len(Array2D[0])}\n")
                text_widget.insert('end', f"Count of arrays inside Array2D: {len(Array2D)}\n")
                text_widget.insert('end', "\nCompleted.\n")
                text_widget.insert('end', '\n')  
                text_widget.insert('end', "____________________________________________END____________________________________________________\n")
                enable_start_button()
                text_widget.see(tk.END)
                break
                


    def Increase_To_Next_Option(i, j, Arrays_Of_Array2D, URL_Subdirectory_Test, Array2D, Unum_List): # 1.4 - Increases to the next combination after reaching last character of array.
        text_widget.insert('end', f"j is equal to {j}\n")  
        text_widget.insert('end', f"i is equal to {i}\n")    
        while URL_Subdirectory_Test[i] == Unum_List[len(Unum_List) - 1]: #cant be 9, has to be end of biglist. #[i] is actually just the position of URL_Subdirectory_Test[i] and see if contents of that index == 9
            if i < Arrays_Of_Array2D:
                i += 1 #im using i somewhere that is causing the loop to end at 47, at i end.
                text_widget.insert('end', f"i is now equal to {i}\n") 
                text_widget.insert('end', f"Arrays_Of_Array2D equals to {Arrays_Of_Array2D}\n")
            if i == Arrays_Of_Array2D:
                text_widget.insert('end', "end\n")
                break #its going to the while's else? or looping in the for.
                #return True, 0
            #add a hasbeenincreased var to do an if yes then ReinitializeArrto0 to avoid execution of function every time.
            #if i == Arrays_Of_Array2D-1:
                #text_widget.insert('end', "end")
                #break #has to end program if i has reached its end. also make 1d and 2d arrays empty again.
        else:
            text_widget.insert('end', "Program not concluded.\n")
            if URL_Subdirectory_Test[i] == "":
                URL_Subdirectory_Test[i] = Array2D[i][0]
                #this can be put outside of the for to optimize efficiency but needs initialize previous arrays to 0 function instead
                # of the break.
                #call function (inizialize previous arrays to 0)
                Reinitialize_Arrays_To_Zero(URL_Subdirectory_Test, Array2D, i, j)
                #changed to b, didnt ran thru a first. move this to if inside for.    
            #look up Array2D[i][j] #if not 9, use a 
            else:
                for l in range(len(Unum_List)): #compares#to compare contents of Array2D[i][j] with URL_Subdirectory_Test[i] and if same, then increases Array2D[i][l+1] and stores it in URL_Subdirectory_Test[i])
                    if URL_Subdirectory_Test[i] == Array2D[i][l]: #compare contents of Array2D[i][j] with URL_Subdirectory_Test[i] and if same, then 
                        URL_Subdirectory_Test[i] = Array2D[i][l+1]#issue here is that WURLTSTS is initialized with "" so it doesnt have anything to compare with.
                        #inside of for, but can be an if, instead of elif. needs == "" if to be changed as recommended.
                        
                        text_widget.insert('end', "Character to add: ")
                        text_widget.insert('end', f'{URL_Subdirectory_Test[i]}\n')
                        
                        text_widget.insert('end', "Entire string: ")    
                        for k in range(len(URL_Subdirectory_Test)):
                            text_widget.insert('end', URL_Subdirectory_Test[k])
                        break
                Reinitialize_Arrays_To_Zero(URL_Subdirectory_Test, Array2D, i, j)
        text_widget.see(tk.END)
        return True, i


    def Reinitialize_Arrays_To_Zero(URL_Subdirectory_Test, Array2D, i, j): # 1.5 - Reusable - Inizialize previous arrays to 0
        while i != 0: # Goes from the index before the one modified, to the first index(index 0)
            i -= 1
            URL_Subdirectory_Test[i] = Array2D[i][0] # Substitutes current index value with index 0 value("a if a is the first index of the list")
            text_widget.insert('end', f'\nValue of i: {URL_Subdirectory_Test[i]}\n')
            text_widget.insert('end', 'New string: ')
            for k in range(len(URL_Subdirectory_Test)):
                text_widget.insert('end', URL_Subdirectory_Test[k])
            text_widget.insert('end', f'\ni now equals : {i}\n')
            text_widget.insert('end', f'j now equals : {j}\n')
        text_widget.see(tk.END)


    def E_Ploribus_Unum(): # Reusable(1.1) - Returns a list with lower, upper, number and special characters, as selected.
        # Can be checkbox input for user to select which ones to include in tests.
        
        Alphabet_Lowercase = list(string.ascii_lowercase)
        text_widget.insert('end', f"Lowercase List: {Alphabet_Lowercase}")
        text_widget.insert('end', '\n')

        Alphabet_Uppercase = list(string.ascii_uppercase)
        text_widget.insert('end', f"Uppercase List: {Alphabet_Uppercase}")
        text_widget.insert('end', '\n')

        Numbers_List = list(string.digits)
        text_widget.insert('end', f"Number's List: {Numbers_List}")
        text_widget.insert('end', '\n')

        Special_Characters = list(string.punctuation)
        text_widget.insert('end', f"Special Characters List: {Special_Characters}")
        text_widget.insert('end', '\n')

        # Test url lookup with special_characters, see which ones are allowed in url.
        #return Alphabet_Lowercase + Alphabet_Uppercase + Numbers_List + Special_Characters # The elements that each Array2D of the multidimensiona Array2D will have.

        return Numbers_List  #+ Special_Characters # Temp return for testing purposes.


    # Define the search() function to append the search information to the Text widget
    def search(Arrays_Of_Array2D, url):

        # Set the search_active flag to True
        global search_active
        search_active = True
        
        global stopped_by_user
        stopped_by_user = False
        
        while search_active:
            main(Arrays_Of_Array2D, url)
            # # Append the search information to the Text widget
            # text_widget.insert('end', f'Attempt {attempt}: Searching for "{search_text}" in {url[:25]}...{url[-20:]}\n')
            
            # lines = text_widget.get(1.0, tk.END).strip("\n")
            
            # # Send a GET request to the URL
            # try:
            #     response = requests.get(url)
            #         # Search the content of the webpage for the search text
            #     if search_text in response.text:
            #         # If the search text is found, open the webpage in the default web browser
            #         webbrowser.open(url)      
            #         text_widget.delete(1.0, tk.END)
            #         text_widget.insert('end', f'Search finished. \n\nText "{search_text}" found on {url}\n\n')
            #         End_Program_Time = time.time()
            #         text_widget.insert('end', f'Time to complete search: {int(End_Program_Time - Start_Program_Time)} seconds.\nNumber of attempts: {attempt}\n')
                    
            #         # Set the search_active flag to False to stop the search
            #         search_active = False
                    
            #         disable_start_button()
            #     else:
            #         if stopped_by_user == False:
            #             text_widget.delete(1.0, tk.END)
            #             text_widget.insert('end', f'{lines}\n')
            #             text_widget.insert('end', f'Text "{search_text}" not found on {url[:25]}...{url[-20:]}\n')#instead of retry_interval, make it timeretry
            #             text_widget.insert('end', f'Retrying...\n\n')#instead of retry_interval, make it timeretry
            #             text_widget.see(tk.END)
            # except Exception as e:
            #     # If the request fails, display an error message and continue with the next attempt
            #     text_widget.insert('end', f'ERROR: {e}\n')
            
            # # Increment the attempt counter
            # attempt += 1
    
    # Create the main window
    window = tk.Tk()
    window.title("Search Webpage")

    # Set the pack_propagate option of the window widget to False
    window.pack_propagate(False)

    # Set the size and position of the main window
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = screen_width // 2
    window_height = screen_height // 2
    window_x = screen_width // 2 - window_width // 2
    window_y = screen_height // 2 - window_height // 2

    # Set the size and position of the new window
    window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    # Create a Label and an Entry widget to request the URL
    url_label = tk.Label(window, text="Enter the URL:")
    url_label.pack()
    url_entry = tk.Entry(window)
    url_entry.pack()

    # Create a Label and an Entry widget to request the search text
    search_text_label = tk.Label(window, text="Enter the lenght to test:")
    search_text_label.pack()
    search_text_entry = tk.Entry(window, validate='key', validatecommand=(window.register(validate_input), '%P'))
    search_text_entry.pack()

    #fix not allowing to erase inputs and new inputs slides to the right.
    #make first and last be side by side, smaller, same as buttons.
    # Create a regular expression to match only digits
    only_numbers_regex = re.compile(r'^\d+$')

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
    
    # Checks for inputs in the textboxes url_entry, search_text_entry, first_retry_entry and last_retry_entry 
    url_entry.bind('<KeyRelease>', check_entry_inputs)
    search_text_entry.bind('<KeyRelease>', check_entry_inputs)
    
    # Binds the Enter key to the Start button so Enter can be pressed to start the program.
    window.bind('<Return>', lambda event: start_button.invoke())
    
    window.mainloop()
    
    



#def websiteurlinput (): gui to request website url, checks if url has / at the end if not, adds it, returns url to functions that needs this input(bruteforce, linkfinder, brokenlinks) - Reusable