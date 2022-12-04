import time # To get the execution time of the program.
Start_Program_Time = time.time()
import Modules.Main_Functions # Local module. Contains unclassified functions used by main.
from Modules.OS_Files_Manager import Clear_Files # Local module. Deletes files created in previous runs.


def Brute_Force_Check_Sites():# Purpose of this program: Check which webpages exist, using brute force. All of this below makes up one functionality of the program.
    
    # Removes the txt files that contains all the URL's info. 
    Clear_Files() 
    # After every run, the txt files needs to be kept for evaluation, so they need to be removed at the beginning of the rerun of the program.

    print("_____________________________________Initializing_Arrays___________________________________________\n")

    # Assign all the elements of all the lists selected in E_Ploribus_Unum() into Unum_List.
    Unum_List = Modules.Main_Functions.E_Ploribus_Unum()

    # Initialize Array2D with the amount of arrays specified(Arrays_Of_Array2D), and the elements of every array.
    Arrays_Of_Array2D, Array2D, URL_Subdirectory_Test = Modules.Main_Functions.Initializing_Arrays(Unum_List)

    print("___________________________________________START___________________________________________________")

    # Evaluates every combination of selected characters.
    Modules.Main_Functions.Start_URL_Tests(Unum_List, Arrays_Of_Array2D, Array2D, URL_Subdirectory_Test)

    print("____________________________________________END____________________________________________________")

    # Shows an end message with the time the program took to run.
    Modules.Main_Functions.End_URL_Tests(Array2D, Start_Program_Time)  

    print("____________________________________________END____________________________________________________")


choice = 1 # Will be an input. Will make a gui with options where 1 is Brute Force check for webpages in a website.
if choice == 1:
    Brute_Force_Check_Sites()


#_________________________________________________COMMENTS_________________________________________________

# brainstorm possible ways of reaching the end goal
# choose the most efficient, memory wise
# visualize the data flow, then describe it, then program it.

# To do:

# [X]Comment code
# [X]Clean code
# [X]Create functions
# [X]Modulate
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
# []Optimize efficiency
    # []Reevaluate processes used.
    # []Multithread (main function)
    
# ___________________________________________________________________________________________________

