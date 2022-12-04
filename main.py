# Purpose of this program: Check which webpages exist, using brute force.

import time #To get the execution time of the program.
from Modules.WebTest import Check_URL #Local module. To check each URL created, store the ones online, and store Web error messages, if any.
from Modules.OS_Files_Manager import Clear_Files # Local module. Deletes files created in previous runs.
from Modules import Main_Functions

start = time.time()
Clear_Files()

print("___________________________________________START___________________________________________________")
print()

#Unum_List contains all the elements of all the lists selected in E_Ploribus_Unum()
Unum_List = E_Ploribus_Unum()

#this can be a single user input, maybe in a textbox to define lenght of test.
Arrays_Of_Array2D = 47

#initializes the dimensions of the multidimensional array using Arrays_Of_Array2D as the amount of arrays
#and with Unum_List as the elements every array in the multidimensional array will contain.
Array2D = [[0 for i in range(len(Unum_List))] for i in range(Arrays_Of_Array2D)]
#Array2D doesnt change or store anything, its only purpose is to scroll thru its elements.

print("___________________________________________________________________________________________________")
print("Dimensions of main Array2D initialized")
print("Count of items inside Array2D 0:", len(Array2D[0]))
print("The items inside each Array2D are initialized to 0")
print("Count of arrays inside Array2D:", len(Array2D))
print("___________________________________________________________________________________________________")

for i in range(Arrays_Of_Array2D):
    for j in range(len(Unum_List)):
        Array2D[i][j] = Unum_List[j]
#adds the elements of Unum_List to every array of the multidimensional array.

print("___________________________________________________________________________________________________")
print("Items of Array2D initialized")
print("Count of items inside Array2D 0:", len(Array2D[0]))
print("The items inside each Array2D are initialized to contain a-z, A-Z, and 0-9")
print("Count of arrays inside Array2D:", len(Array2D))
print("___________________________________________________________________________________________________")


print("___________________________________________START___________________________________________________")
Website_URL_Tests = [""] * Arrays_Of_Array2D
#creates a 1 dimension array and makes it as long as the amount of arrays in the multidimensional array, and makes every element to be empty "".
Website_URL = ""
Iteration_Count = 0 #for testing purposes, irrelevant for the Multithread test.

tracker = True
i = 0
while i <= Arrays_Of_Array2D:
    i += 1
    print("___________________________________________________________________________________________________")
    print("From i = 0 to i =", Arrays_Of_Array2D - 1, " |  i =", i)
    print("___________________________________________________________________________________________________")
    if tracker == True:
        i = 0
        tracker = False
    for j in range(len(Unum_List)):
        Iteration_Count += 1
        print("")
        print("Iteration #", Iteration_Count)
        print("From j = 0 to j =", len(Unum_List) - 1, "| i =", i, "& j =", j)
        print("________")
        print("")

        Website_URL_Tests[i] = Array2D[i][j]  #Most important line in this code. 
        #As Array2D changes positioning thru its elements, they are stored on the 1d array. 
        
        # Overlaying wURLTST over Array2D 
        #the first 6 out of the 47 might be aaaaaa.
        #when this is adding whats on view in Array2D, it adds nothing in other positions bc i and j are reinizialized. 
        #how to keep up? look up in WURLTST, compare and initialize Array2D as per WURLTSTS?
        #Array2D is like ram, WURLTST is like storage, and WURL is just the medium to facilitate transfer between storage and program.

        print("Website_URL_Tests = ", end="")
        for k in range(len(Website_URL_Tests)): #stores the elements of the 1d array on the variable Website_URL
            print(Website_URL_Tests[k], end="")
            Website_URL = Website_URL + str(Website_URL_Tests[k])
        print()
        
        url = "https://www.youtube.com/" + Website_URL #+ "=" #creates the url to test
        print("URL =", url)

        # web test module function. This module can have more functions to expand program capabilities.
        
        Check_URL(url) # Doesn't need to return anything.
        
        Website_URL = ""
        print("___________________________________________________________________________________________________")
        
        #this could be a main function to check if reached the end of the array.
        
        if j == 61: #si llega al final, va al proximo array, si es 9 va al proximo array etc etc y si no es 9, aumenta 1 e i-- j =0 so on hasta que i =0
            print("j indeed is equal to 61")
            i += 1  #needs rest of code to go back clean etc, what is          
            while Website_URL_Tests[i] == 9 and i < Arrays_Of_Array2D: #[i] is actually just the position of Website_URL_Test[i] and see if contents of that index == 9
                i += 1 #im using i somewhere that is causing the loop to end at 47, at i end.
                
            #look up Array2D [i][j] #if not 9, use a 
            for l in range(len(Unum_List)): #compares#to compare contents of Array2D[i][j] with Website_URL_Test[i] and if same, then increases Array2D[i][l+1] and stores it in Website_URL_Tests[i])
                if Website_URL_Tests[i] == "":
                    Website_URL_Tests[i] = "a"
                    #this can be put outside of the for to optimize efficiency but needs initialize previous arrays to 0 function instead
                    # of the break.
                    #call function (inizialize previous arrays to 0)
                    break #changed to b, didnt ran thru a first. move this to if inside for.
                elif Website_URL_Tests[i] == Array2D[i][l]: #compare contents of Array2D[i][j] with Website_URL_Test[i] and if same, then 
                    Website_URL_Tests[i] = Array2D[i][l+1]#issue here is that WURLTSTS is initialized with "" so it doesnt have anything to compare with.
                    #inside of for, but can be an if, instead of elif. needs == "" if to be changed as recommended.
                    
                    print("Character to add: ", end="")
                    print(Website_URL_Tests[i])
                    
                    print("Entire string: ", end="")    
                    for k in range(len(Website_URL_Tests)):
                        print(Website_URL_Tests[k], end="")
                    break
            while i != 0: #inizialize previous arrays to 0
                #make this a function (inizialize previous arrays to 0)
                #call function (inizialize previous array to 0)
                i -= 1
                Website_URL_Tests[i] = Array2D[i][0] # decrease other 9's to index 0
                print(f"\nValue of i: {Website_URL_Tests[i]}")
                print("New string: ", end="")
                for k in range(len(Website_URL_Tests)):
                    print(Website_URL_Tests[k], end="")
                print(f"\ni equals : {i}")
                print(f"\nj equals : {j}")
            else:
                tracker = True #when is tracker false?
                
                    # may be put on i because j wouldnt be reset until it starts the j loop, or not bc i has changed already and cant do i+1== 9 test.
                    #should I add variable to track when i should be 0 bc when it goes back to i, i becomes 1, so if theres a variable like a counter or tracker that here is added when
                    #needs to be 0, ej Isfirst = true and there if tracker == true then i = 0
                    #print("ok")
                    
                    #issue might be because U is 47 and it cannot increase more? has to be 62 tho.

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

