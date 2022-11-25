#Check which webpages exist, using brute force.

import urllib.request
import os
import string
import time  

start = time.time()


Alphabet_Lowercase = list(string.ascii_lowercase)
print(Alphabet_Lowercase)

Alphabet_Uppercase = list(string.ascii_uppercase)
print(Alphabet_Uppercase)

Numbers_List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(Numbers_List)
print()

Big_List = Alphabet_Lowercase + Alphabet_Uppercase + Numbers_List

Combined_List_Length = 10

if os.path.isfile('Online.txt'):
    os.remove('Online.txt')
if os.path.isfile('UnhandledCodes.txt'):
    os.remove('UnhandledCodes.txt')
if os.path.isfile('UnhandledErrors.txt'):
    os.remove('UnhandledErrors.txt')

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
        print(array[i][j])

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
for i in range(Combined_List_Length):
    print("___________________________________________________________________________________________________")
    print("From i = 0 to i =", Combined_List_Length - 1, " |  i =", i)
    print("___________________________________________________________________________________________________")

    for j in range(len(Big_List)):
        Iteration_Count += 1
        print("")
        print("Iteration #", Iteration_Count)
        print("From j = 0 to j =", len(Big_List) - 1, "| i =", i, "& j =", j)
        print("________")
        print("")

        Website_URL_Tests[i] = array[i][j]

        print("Website_URL_Tests = ", end="")
        for k in range(len(Website_URL_Tests)):
            print(Website_URL_Tests[k], end="")
            Website_URL = Website_URL + str(Website_URL_Tests[k])
        print()
        url = "https://www.youtube.com/" + Website_URL #+ "="
        print("URL =", url)

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

print()
print("Count of items inside array 0:", len(array[0]))
print("Count of arrays inside array:", len(array))

print()
end = time.time()
print("Time to compile:", round(end - start, 4), "seconds.")