import time # To get the execution time of the program.
Start_Program_Time = time.time()
import Main_Modules.Brute_Force # Local module. Contains unclassified functions used by main.


choice = 1 # Will be an input. Will make a gui with options where 1 is Brute Force check for webpages in a website.
if choice == 1:
    Main_Modules.Brute_Force.Check_Sites(Start_Program_Time)


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