import string #To get the characters and numbers to create the URLs.

def E_Ploribus_Unum(): #function to initialize characters to test
    #can be checkbox input for user to select which ones to include in tests.
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

    return Alphabet_Lowercase + Alphabet_Uppercase + Numbers_List  #+ Special_Characters #the elements that each Array2D of the multidimensiona Array2D will have.
    #test url lookup with special_characters
    
def Array2D(Unum_List):
    #this can be a single user input, maybe in a textbox to define lenght of test.
    Arrays_Of_Array2D = 47

    #initializes the dimensions of the multidimensional array using Arrays_Of_Array2D as the amount of arrays
    #and with Unum_List as the elements every array in the multidimensional array will contain.
    Array2D = [[0 for i in range(len(Unum_List))] for i in range(Arrays_Of_Array2D)]
    #Array2D doesnt change or store anything, its only purpose is to scroll thru its elements.

    print("___________________________________________________________________________________________________")
    print("Dimensions of Array2D initialized")
    print("Count of items inside Array2D 0:", len(Array2D[0]))
    print("The items inside each Array2D are initialized to 0")
    print("Count of arrays inside Array2D:", len(Array2D))
    print("___________________________________________________________________________________________________")

    #adds the elements of Unum_List to every array of Array2D.
    for i in range(Arrays_Of_Array2D):
        for j in range(len(Unum_List)):
            Array2D[i][j] = Unum_List[j]

    print("___________________________________________________________________________________________________")
    print("Items of Array2D initialized")
    print("Count of items inside Array2D 0:", len(Array2D[0]))
    print("The items inside each Array2D are initialized to contain a-z, A-Z, and 0-9")
    print("Count of arrays inside Array2D:", len(Array2D))
    print("___________________________________________________________________________________________________")
    
    return Arrays_Of_Array2D, Array2D

def Increase_To_Next_Option(i, j, Arrays_Of_Array2D, URL_Subdirectory_Test, Array2D, Unum_List):
    print("j indeed is equal to 61")
    i += 1  #needs rest of code to go back clean etc, what is          
    while URL_Subdirectory_Test[i] == 9 and i < Arrays_Of_Array2D: #[i] is actually just the position of URL_Subdirectory_Test[i] and see if contents of that index == 9
        i += 1 #im using i somewhere that is causing the loop to end at 47, at i end.
        
    #look up Array2D[i][j] #if not 9, use a 
    for l in range(len(Unum_List)): #compares#to compare contents of Array2D[i][j] with URL_Subdirectory_Test[i] and if same, then increases Array2D[i][l+1] and stores it in URL_Subdirectory_Test[i])
        if URL_Subdirectory_Test[i] == "":
            URL_Subdirectory_Test[i] = Array2D[i][0]
            #this can be put outside of the for to optimize efficiency but needs initialize previous arrays to 0 function instead
            # of the break.
            #call function (inizialize previous arrays to 0)
            break #changed to b, didnt ran thru a first. move this to if inside for.
        elif URL_Subdirectory_Test[i] == Array2D[i][l]: #compare contents of Array2D[i][j] with URL_Subdirectory_Test[i] and if same, then 
            URL_Subdirectory_Test[i] = Array2D[i][l+1]#issue here is that WURLTSTS is initialized with "" so it doesnt have anything to compare with.
            #inside of for, but can be an if, instead of elif. needs == "" if to be changed as recommended.
            
            print("Character to add: ", end="")
            print(URL_Subdirectory_Test[i])
            
            print("Entire string: ", end="")    
            for k in range(len(URL_Subdirectory_Test)):
                print(URL_Subdirectory_Test[k], end="")
            break
    while i != 0: #inizialize previous arrays to 0
        #make this a function (inizialize previous arrays to 0)
        #call function (inizialize previous array to 0)
        i -= 1
        URL_Subdirectory_Test[i] = Array2D[i][0] # decrease other 9's to index 0("a")
        print(f"Value of i: {URL_Subdirectory_Test[i]}")
        print("New string: ", end="")
        for k in range(len(URL_Subdirectory_Test)):
            print(URL_Subdirectory_Test[k], end="")
        print(f"\ni equals : {i}")
        print(f"j equals : {j}")
    else:
        return True, i 