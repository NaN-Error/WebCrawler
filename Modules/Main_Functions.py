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
