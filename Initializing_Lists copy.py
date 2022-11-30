# Purpose of this program:
    # Check which webpages exist, using brute force.

# __________________________________________COMMENTS_________________________________________________

# To do:

# Comment code
# Clean code
# Create functions
# Modulate
# Expand program capabilities
# Optimize efficiency
    # Reevaluate processes used.
    # multithread (main function)

# ___________________________________________________________________________________________________

import urllib.request
import os
import string
import time  

start = time.time()

print("___________________________________________START___________________________________________________")
print()

#this can be a main function to initialize characters to test. can be checkbox input for useer to select which ones to include in tests.
Alphabet_Lowercase = list(string.ascii_lowercase)
print(f"Lowercase List: {Alphabet_Lowercase}")
print()

Alphabet_Uppercase = list(string.ascii_uppercase)
print(f"Uppercase List: {Alphabet_Uppercase}")
print()

Numbers_List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Number's List: {Numbers_List}")
print()

Big_List = Alphabet_Lowercase + Alphabet_Uppercase + Numbers_List


#this can be a single user input, maybe in a textbox to define lenght of test.
Combined_List_Length = 47

#this can be a module dedicated to local file management. This module can have more functions to expand program capabilities. 
# e.x. database. gui for link selection (calls db to get all links in a gui list.) this list could also give some extra information
# about the link.
if os.path.isfile('Online.txt'):
    os.remove('Online.txt')
if os.path.isfile('UnhandledCodes.txt'):
    os.remove('UnhandledCodes.txt')
if os.path.isfile('UnhandledErrors.txt'):
    os.remove('UnhandledErrors.txt')

# The rest can be on main. One web module can be made for the url tests. Find recommendation in the next comments.
# to initialize array.
array = [[0 for i in range(len(Big_List))] for i in range(Combined_List_Length)]

print("___________________________________________________________________________________________________")
print("Dimensions of main array initialized")
print("Count of items inside array 0:", len(array[0]))
print("The 62 items inside each array are initialized to 0")
print("Count of arrays inside main array:", len(array))
print("___________________________________________________________________________________________________")

for i in range(Combined_List_Length):
    for j in range(len(Big_List)):
        array[i][j] = Big_List[j]

print("___________________________________________________________________________________________________")
print("Items of arrays initialized")
print("Count of items inside array 0:", len(array[0]))
print("The 62 items inside each array are initialized to contain a-z, A-Z, and 0-9")
print("Count of arrays inside array:", len(array))
print("___________________________________________________________________________________________________")

print("___________________________________________START___________________________________________________")
Website_URL_Tests = [""] * Combined_List_Length
Website_URL = ""
Iteration_Count = 0

tracker = True
i = 0
while i <= Combined_List_Length:
    i += 1
    print("___________________________________________________________________________________________________")
    print("From i = 0 to i =", Combined_List_Length - 1, " |  i =", i)
    print("___________________________________________________________________________________________________")
    if tracker == True:
        i = 0
        tracker = False
    for j in range(len(Big_List)):
        Iteration_Count += 1
        print("")
        print("Iteration #", Iteration_Count)
        print("From j = 0 to j =", len(Big_List) - 1, "| i =", i, "& j =", j)
        print("________")
        print("")

        Website_URL_Tests[i] = array[i][j] # Overlaying wURLTST over array2d 
        #the first 6 out of the 47 might be aaaaaa.
        #when this is adding whats on view in array, it adds nothing in other positions bc i and j are reinizialized. 
        #how to keep up? look up in WURLTST, compare and initialize array as per WURLTSTS?
        #array is like ram, WURLTST is like storage, and WURL is just the medium to facilitate transfer between storage and program.

        print("Website_URL_Tests = ", end="")
        for k in range(len(Website_URL_Tests)):
            print(Website_URL_Tests[k], end="")
            Website_URL = Website_URL + str(Website_URL_Tests[k])
        print()
        
        url = "https://www.youtube.com/" + Website_URL #+ "="
        print("URL =", url)

        # web test module function. This module can have more functions to expand program capabilities.
        
        # second function could be website download as pdf. (screen scraping)
        
        # webcrawl to id every webpage a website has, going thru all its links related to the website.
            #can individually download each link as pdf or can also download every link.
            
        # could web crawl to id databases on website (webpage by webpage.) gets webpages, and databases it contains.
            #can download all databases/database contents.
            # could be all databases from a given webpage, or crawl all website and get all databases from all webpages.
            
        # main should give up a gui to ask user what function the program is going to execute. 
            # brute force find webpages of a website, find all webpages of a website. find databases of webpage/website.
        try:
            r = urllib.request.urlopen(url)
            getcode_url = urllib.request.urlopen(url).getcode()
            if getcode_url == 200:
                print('Web page exists.')
                Site_Length = len(r.read())
                print("Site length =", Site_Length)
                print("Site length type =", type(Site_Length))

                if Site_Length > 1: #Stores only webpages that its lenght are more than 1. Relevant for something I might do, do not change.
                    print("Contains relevant information.")
                    with open('Online.txt', 'a') as f:
                        f.write("Webpage: ")
                        f.write(url)
                        f.write('\n')
                        f.close()
            else:
                print("Unhandled code, see UnhandledCodes.txt for more information.")
                with open('UnhandledCodes.txt', 'a') as f:
                    f.write("Unhandled Code: ")
                    f.write(getcode_url)
                    f.write("- Webpage:")
                    f.write(url)
                    f.write('\n')
                    f.close()
        except urllib.error.URLError as e: 
            print(e)
        except urllib.error.HTTPError as e: 
            print(e)
        else:
            print("Unhandled error, see UnhandledErrors.txt for more information.")
            with open('UnhandledErrors.txt', 'a') as f:
                f.write("Unhandled Error: ")
                f.write(str(urllib.error))
                f.write("- Webpage:")
                f.write(url)
                f.write('\n')
                f.close()

        Website_URL = ""
        print("___________________________________________________________________________________________________")
        
        #this could be a main function to check if reached the end of the array.
        
        if j == 61: #si llega al final, va al proximo array, si es 9 va al proximo array etc etc y si no es 9, aumenta 1 e i-- j =0 so on hasta que i =0
            print("j indeed is equal to 61")
            i += 1  #needs rest of code to go back clean etc, what is          
            while Website_URL_Tests[i] == 9 and i < 47: #[i] is actually just the position of Website_URL_Test[i] and see if contents of that index == 9
                i += 1 #im using i somewhere that is causing the loop to end at 47, at i end.
                
            #look up array [i][j] #if not 9, use a 
            for l in range(len(Big_List)): #compares#to compare contents of array[i][j] with Website_URL_Test[i] and if same, then increases array[i][l+1] and stores it in Website_URL_Tests[i])
                if Website_URL_Tests[i] == "":
                    Website_URL_Tests[i] = "a"
                    #this can be put outside of the for to optimize efficiency but needs initialize previous arrays to 0 function instead
                    # of the break.
                    #call function (inizialize previous arrays to 0)
                    break #changed to b, didnt ran thru a first. move this to if inside for.
                elif Website_URL_Tests[i] == array[i][l]: #compare contents of array[i][j] with Website_URL_Test[i] and if same, then 
                    Website_URL_Tests[i] = array[i][l+1]#issue here is that WURLTSTS is initialized with "" so it doesnt have anything to compare with.
                    #inside of for, but can be an if, instead of elif. needs == "" if to be changed as recommended.
                    
                    print("Character to add: ", end="")
                    print(Website_URL_Tests[i])
                    
                    print("Entire string: ", end="")    
                    for k in range(len(Website_URL_Tests)):
                        print(Website_URL_Tests[k], end="")
                    break
            while i != 0: #inizialize previous arrays to 0
                #make this a function (inizialize previous arrays to 0)
                #call function (inizialize previous arrays to 0)
                i -= 1
                Website_URL_Tests[i] = array[i][0] # decrease other 9's to index 0
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
print("Count of items inside array 0:", len(array[0]))
print("Count of arrays inside array:", len(array))

print()
end = time.time()
print("Time to compile:", round(end - start, 4), "seconds.")

