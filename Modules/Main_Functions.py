import string # To get the characters and numbers to create the URLs.
from Modules.WebTest import Check_URL # Local module. To check each URL created, store the ones online, and store Web error messages, if any.
import time # To get the execution time of the program.

# Clean comments, clean Increase_To_Next_Option =="" option to reuse function.
# for len(x-1)

def E_Ploribus_Unum(): # Function to initialize characters to test
    # Can be checkbox input for user to select which ones to include in tests.
    Alphabet_Lowercase = list(string.ascii_lowercase)
    print(f"Lowercase List: {Alphabet_Lowercase}")
    print()

    Alphabet_Uppercase = list(string.ascii_uppercase)
    print(f"Uppercase List: {Alphabet_Uppercase}")
    print()

    Numbers_List = list(string.digits)
    print(f"Number's List: {Numbers_List}")
    print()

    Special_Characters = list(string.punctuation)
    print(f"Special Characters List: {Special_Characters}")
    print()

    # Test url lookup with special_characters
    #return Alphabet_Lowercase + Alphabet_Uppercase + Numbers_List + Special_Characters #the elements that each Array2D of the multidimensiona Array2D will have.

    return Numbers_List  #+ Special_Characters #the elements that each Array2D of the multidimensiona Array2D will have.


def Initializing_Arrays(Unum_List): # Function to initialize Array2D and URL_Subdirectory_Test(Array1D)
    # This can be a single user input, maybe in a textbox to define lenght of test.
    Arrays_Of_Array2D = 47

    # Initializes the dimensions of the multidimensional array using Arrays_Of_Array2D as the amount of arrays
    # And with Unum_List as the elements every array in the multidimensional array will contain.
    Array2D = [[0 for i in range(len(Unum_List))] for i in range(Arrays_Of_Array2D)]
    # Array2D doesnt change or store anything, its only purpose is to scroll thru its elements.

    print("___________________________________________________________________________________________________")
    print("Dimensions of Array2D initialized")
    print("Count of items inside Array2D 0:", len(Array2D[0]))
    print("The items inside each Array2D are initialized to 0")
    print("Count of arrays inside Array2D:", len(Array2D))
    print("___________________________________________________________________________________________________")

    # Adds the elements of Unum_List to every array of Array2D.
    for i in range(Arrays_Of_Array2D):
        for j in range(len(Unum_List)):
            Array2D[i][j] = Unum_List[j]

    print("___________________________________________________________________________________________________")
    print("Items of Array2D initialized")
    print("Count of items inside Array2D 0:", len(Array2D[0]))
    print("The items inside each Array2D are initialized to contain a-z, A-Z, and 0-9")
    print("Count of arrays inside Array2D:", len(Array2D))
    print("___________________________________________________________________________________________________")
    
    # Creates a 1 dimension array and makes it as long as the amount of arrays in Array2D, and makes every element to be empty "".
    URL_Subdirectory_Test = [""] * Arrays_Of_Array2D   
    
    return Arrays_Of_Array2D, Array2D, URL_Subdirectory_Test


def Start_URL_Tests(Unum_List, Arrays_Of_Array2D, Array2D, URL_Subdirectory_Test): # Evaluates every combination of selected characters.
    
    # For testing purposes.
    Iteration_Count = 0 

    # To id when the program should go back to array 1(index 0).
    IsZero = True 
    i = 0 

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
                IsZero, i = Increase_To_Next_Option(i, j, Arrays_Of_Array2D, URL_Subdirectory_Test, Array2D, Unum_List)


def Increase_To_Next_Option(i, j, Arrays_Of_Array2D, URL_Subdirectory_Test, Array2D, Unum_List): # Increases to the next combination after reaching last character of array.
    print(f"j indeed is equal to {j}")
    i += 1          
    
    while URL_Subdirectory_Test[i] == Unum_List[len(Unum_List) - 1] and i < Arrays_Of_Array2D: #cant be 9, has to be end of biglist. #[i] is actually just the position of URL_Subdirectory_Test[i] and see if contents of that index == 9
        i += 1 #im using i somewhere that is causing the loop to end at 47, at i end.
        #add a hasbeenincreased var to do an if yes then ReinitializeArrto0 to avoid execution of function every time.
    if URL_Subdirectory_Test[i] == "":
        URL_Subdirectory_Test[i] = Array2D[i][0]
        print(URL_Subdirectory_Test[i])
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
                
                print("Character to add: ", end="")
                print(URL_Subdirectory_Test[i])
                
                print("Entire string: ", end="")    
                for k in range(len(URL_Subdirectory_Test)):
                    print(URL_Subdirectory_Test[k], end="")
                break
        Reinitialize_Arrays_To_Zero(URL_Subdirectory_Test, Array2D, i, j)
    return True, 0


def Reinitialize_Arrays_To_Zero(URL_Subdirectory_Test, Array2D, i, j): # Inizialize previous arrays to 0
    while i != 0: 
        i -= 1
        URL_Subdirectory_Test[i] = Array2D[i][0] # Decrease other 9's to index 0("a")
        print(f"\nValue of i: {URL_Subdirectory_Test[i]}")
        print("New string: ", end="")
        for k in range(len(URL_Subdirectory_Test)):
            print(URL_Subdirectory_Test[k], end="")
        print(f"\ni equals : {i}")
        print(f"j equals : {j}")


def End_URL_Tests(Array2D, Start_Program_Time): # Shows an end message with the time the program took to run.
    print()
    print("Count of items inside Array2D[0]:", len(Array2D[0]))
    print("Count of arrays inside Array2D:", len(Array2D))
    print()
    End_Program_Time = time.time()
    print("Time to compile:", round(End_Program_Time - Start_Program_Time, 4), "seconds.")