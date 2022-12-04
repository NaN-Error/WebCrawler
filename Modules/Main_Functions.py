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