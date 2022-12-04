# Purpose of this program: Check which webpages exist, using brute force.
import time # To get the execution time of the program.
from Modules.WebTest import Check_URL # Local module. To check each URL created, store the ones online, and store Web error messages, if any.
from Modules.OS_Files_Manager import Clear_Files # Local module. Deletes files created in previous runs.
import Modules.Main_Functions # Local module. Contains unclassified functions used by main.


start = time.time()

print("_____________________________________Initializing_Data_____________________________________________")
print()

# Removes the txt files that contains all the URL's info. 
Clear_Files() 
# After every run, the txt files needs to be kept for evaluation, so they need to be removed at the beginning of the rerun of the program.

# Unum_List contains all the elements of all the lists selected in E_Ploribus_Unum()
Unum_List = Modules.Main_Functions.E_Ploribus_Unum()

# Initialize Array2D with its arrays and the elements of every array.
Arrays_Of_Array2D, Array2D = Modules.Main_Functions.Array2D(Unum_List)

# Creates a 1 dimension array and makes it as long as the amount of arrays in Array2D, and makes every element to be empty "".
URL_Subdirectory_Test = [""] * Arrays_Of_Array2D

# For testing purposes.
Iteration_Count = 0 

# To id when the program should go back to array 1(index 0).
IsZero = True 
i = 0 

print("___________________________________________START___________________________________________________")

# While instead of a for. The for didn't allowed to modify i when it was inside another loop and if.
while i <= Arrays_Of_Array2D: 
    i += 1
    
    if IsZero == True:
        i = 0
    IsZero = False
    
    print("___________________________________________________________________________________________________")
    print("From i = 0 to i =", Arrays_Of_Array2D - 1, " |  i =", i)
    print("___________________________________________________________________________________________________")
    
    for j in range(len(Unum_List)):
        Iteration_Count += 1
        
        # Clears the contents of the string URL_Subdirectory before using it.
        URL_Subdirectory = ""
        # Every time URL_Subdirectory_Test is modified, its more efficient and simpler to use a string than an array.
        
        print("")
        print("Iteration #", Iteration_Count)
        print("From j = 0 to j =", len(Unum_List) - 1, "| i =", i, "& j =", j)
        print("________")
        print("")
        
        # Most important line in this program. 
        URL_Subdirectory_Test[i] = Array2D[i][j]  
        # As Array2D changes positioning thru its elements, they are stored on the 1d array. 
        # URL_Subdirectory_Test is like an overlay of Array2D that will save the elements Array2D is going thru.
        
        # Stores all the elements of the list URL_Subdirectory_Test on the string variable URL_Subdirectory
        print("URL_Subdirectory_Test = ", end="")
        for k in range(len(URL_Subdirectory_Test)): 
            print(URL_Subdirectory_Test[k], end="")
            URL_Subdirectory = URL_Subdirectory + str(URL_Subdirectory_Test[k])
        print()
        
        # Creates the complete url to test
        url = "https://www.youtube.com/" + URL_Subdirectory #+ "=" 
        print("URL =", url)

        # If website exist, saves the URL on txt.
        Check_URL(url) 
        
        print("___________________________________________________________________________________________________")
                
        if j == len(Unum_List)-1: #si llega al final, va al proximo array, si es 9 va al proximo array etc etc y si no es 9, aumenta 1 e i-- j =0 so on hasta que i =0
            IsZero, i = Modules.Main_Functions.Increase_To_Next_Option(i, j, Arrays_Of_Array2D, URL_Subdirectory_Test, Array2D, Unum_List)
        
print()
print("Count of items inside Array2D[0]:", len(Array2D[0]))
print("Count of arrays inside Array2D:", len(Array2D))

print()
end = time.time()
print("Time to compile:", round(end - start, 4), "seconds.")



# __________________________________________COMMENTS_________________________________________________

# brainstorm possible ways of reaching the end goal
# choose the most efficient, memory wise
# visualize the data flow, then describe it, then program it.

# To do:

# Comment code
# Clean code
# Create functions
# Modulate
# Expand program capabilities
    #gui
    # database. gui for link selection (calls db to get all links in a gui list.) this list could also give some extra information
    # about the link.
    # second function could be website download as pdf. 
    # webcrawl to id every webpage a website has, going thru all its links related to the website.
        #can individually download each link as pdf or can also download every link.
    # could web crawl to id databases on website (webpage by webpage.) gets webpages, and databases it contains.
        #can download all databases/database contents.
        # could be all databases from a given webpage, or crawl all website and get all databases from all webpages.
    # main should give up a gui to ask user what function the program is going to execute. 
        # brute force find webpages of a website, find all webpages of a website. find databases of webpage/website.
    # maybe organize by a module that calls the functions it needs, a module for each big function
# Optimize efficiency
    # Reevaluate processes used.
    # multithread (main function)
    
# ___________________________________________________________________________________________________

