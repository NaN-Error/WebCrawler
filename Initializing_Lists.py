# module Inizializing_Lists
# module WebTest
# for each found, put on a list of found
# make Combined_List public, or this module a function to be used

#brainstorm possible ways of reaching the end goal
#choose the most efficient, memory wise
# visualize the data flow, then describe it, then program it.


import urllib.request
# temporary import for testing purposes
import os
import string
import time  # testing time it takes to execute this code

start = time.time()

#TO DO ---------------------------------------------
#add enter array length, enter website main url.
# Loading the lowercase alphabet to a list
#functions to modulate the code. function to initialize Website_URL_Tests (calls function to initialize everything,
#returns Website_URL_Tests with all elements as "a") #I think lists doesnt need to be passed as parameters for they're
#already in memory of the program itself, and not just the function where it has been initialized/used).


Alphabet_Lowercase = list(string.ascii_lowercase)
print(Alphabet_Lowercase)

# Loading the uppercase alphabet to a list
Alphabet_Uppercase = list(string.ascii_uppercase)
print(Alphabet_Uppercase)

# Loading the numbers to a list
Numbers_List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(Numbers_List)
print()

## Special characters are not needed (they didnt used special characters in my link, I assume thats its programming).

# Combining the lists to make one big list.

Big_List = Alphabet_Lowercase + Alphabet_Uppercase + Numbers_List

## Combine the list with itself based on the desired length to test (my link had 47 characters of length).
Combined_List_Length = 47  # first append has to be done individually
# Combined_List = []  #List that contains the results of Big_List combined with itself by Combined_List_Length amount of
# times.

# removes the readme.txt file so it can start from scratch. = clear(readme.txt)
if os.path.isfile('Online.txt'):
    os.remove('Online.txt')
if os.path.isfile('UnhandledCodes.txt'):
    os.remove('UnhandledCodes.txt')
if os.path.isfile('UnhandledErrors.txt'):
    os.remove('UnhandledErrors.txt')

# Stores Big_List in the readme.txt file. Storing it in an array works but with many iteration gives memory error.
# Storing the list in hdd instead of ram.
# for i in Big_List:
#     Combined_List.append(str(i))  #copies Big_list into Combined_list
#     with open('readme.txt', 'a') as f:
#         f.write(str(i))
#         f.write('\n')
#         f.close()

# counter works as positioning for the txt files. The count of upper, lower and nums is 62, so each iteration is
# 62 * iteration#. if its the second iteration, then 124 is the last place in the txt. Useful to read from 63 to
# 124 and use the content of each line to append with initial list. aa, ab, etc, and use it to create aaa, aab, aac.
# counter = 0

array = [[0 for i in range(len(Big_List))] for i in range(Combined_List_Length)]

print("___________________________________________________________________________________________________")
print("Dimensions of main array initialized")
print("Count of items inside array 0:", len(array[0]))
print("The 62 items inside each array are initialized to 0")
print("Count of arrays inside main array:", len(array))
print("___________________________________________________________________________________________________")

# array has to be inizialized for every array of the array to contain the same elements as Big_List.

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
# print("i =", i, len(Big_List))
# for j in range(len(Combined_List)):

# DONE - each array of the array contains the same elements as Big_List

# two arrays needed, first one initial one, base, core, second one the one it keeps adding the first array.
print("___________________________________________START___________________________________________________")
Website_URL_Tests = ["a"] * Combined_List_Length
Website_URL = ""
Iteration_Count = 0
for i in range(Combined_List_Length):
    print("___________________________________________________________________________________________________")
    print("From i = 0 to i =", Combined_List_Length - 1, " |  i =", i)
    print("___________________________________________________________________________________________________")
    # for j in range(len(Combined_List)):

    # a for that evaluates in parallel with j for. after i has been incremented, if i > 0, if websiteurltest[i-1] = 9 it goes into
    # second for, else, goes into first for (built already). second for is in charge of resetting i -1 so it continues
    # to go up until its 9.
    # does it has to be second for or a simple if works? seems like it may.

    #visualize the data flow, then describe it, then program it.
    #array 0 keeps increasing
    #after it reaches the end, it increases

    #should Websiteurtest contains as elements just the indexes
    #and then use those those indexes(webisteurtest elements) to get the data off the multidimensional array
    #single array is the new for, where each element is the index
    #1darray[0, 1,2,3...46)
    #array[1darray[0(use i maybe)]][j] then save contents on 1Darray.
    #as multi array second array keeps increasing constantly syncs up w 1darray
    #1d array stores array[i][j] because in 2darray, i works as the 47 length it needs to check, and j as the letters
    #so array[i][j] would give up the letter the i array has, but its also stored on 1darray[i], so they both would
    #run under the same index at the same time, is just 1darray would store up the letter that the j array would
    #point at in the index of array[i][j]. 1darray n 2darray are the same, just 1darray stores where 2darray second array
    #is at. # Website_URL_Tests[i] = array[i][j]

    #the issue is that after reaching 9, instead of changing index i permanently,
    # if there's a next index, if the next index <> 9,  its supposed to increase the next index by 1, and turn itself into index 0
    #and so it keeps going until next index is 9 too, but because next index is 9 too, then increases the next one
    #and so on until the last index has been increased.
    #if next index = 9, increase index, if it is 9, increase, so on until an index without a 9 is found or is the end.

#increases 1, else,y

# while Website_URL_Tests[i] != 9
        # i += 1
    #else:
        #i -= 1
    # if i > 0:
    #     if Website_URL_Tests[i-1] == 9:
    #         #do something with Websiteurltest to make it as previous
    #         #i = i-1
    #         continue


    for j in range(len(Big_List)):
        Iteration_Count += 1
        print("")
        print("Iteration #", Iteration_Count)
        print("From j = 0 to j =", len(Big_List) - 1, "| i =", i, "& j =", j)
        print("________")
        print("")
        # if www.site.com/code=Combined_List[j] + str(k) is online, then append n store in txt

#needs to have proper logic, and also needs to stop evaluating for aaaaaaa if its just starting. should go from a to 9, then aa to 9a, then keep increasing in size.

        # does it need multidimensional array or a simple array with 47 positioning that changes each index with the
        # next letter should do? #think of memory error too.
        #array easier to manage than a concatenated string. 1d array needed for simplicity.
        Website_URL_Tests[i] = array[i][j]
        #in i but out of j, goes to i and increases it, stores in website url test, and goest to j to retest everything
        #in j but with i changed in array and web ur test.


        #remember that the only thing you need is that WEbsite_URL_tests does what we want to, the end goal of url

        # Combined_List.append(Combined_List[j] + str(k))  # logic works, but gives memory error

        #to check Website_URL logic, indentation, similarities to Website_URL_Tests to see if data passing thru right.
        print("Website_URL_Tests = ", end="")
        for k in range(len(Website_URL_Tests)):
            print(Website_URL_Tests[k], end="")
            Website_URL = Website_URL + str(Website_URL_Tests[k])
        #print(Website_URL) #to check
            #store in a single variable to use as URL

        print()
        #

        # DONE: needs to store the whole array current 47 positioning, j changes from 0 to 46 but i stays the same.
        # Website_URL_Tests should be a 1d array of 47 items?

# TO DO: reevaluate logic. Some combinations are not being evaluated. (last task)
        # what's happening is that the second for is putting the info correctly, but, the first for still contains
        # the 9. its supposed to become "a" and reevaluate everything again.
        # #think of the multidimensional array, the logic issue is there, in the fors, not combining every element.

# TO DO should call function in webtest.py and send Website_URL_Tests as parameter for it to check if site exist.
# meanwhile, test in this module alltogether.

# -------------------------------------------------------------------------------------------------------------------
#temporary allocation of this code in this module for testing purposes

        #to check Website_URL logic

        url = "https://www.youtube.com/" + Website_URL + "="
        #https://islandmedpr.com/app/foto/index.php?code=

        #add condition if site exist, do this, else keeps going.
        #response = urllib.requests.get(url)
        print("URL =", url)

        #check status_code > 400 ??
        #using .getcode() and evaluating that code to be 200 reduces the open general use
        #and only gets the code it receives which might increase efficiency and reduce bandwidth.

        try:
            r = urllib.request.urlopen(url)
            getcode_url = urllib.request.urlopen(url).getcode()
            if getcode_url == 200:
                print('Web page exists.')
                Site_Length = len(r.read())
                print("Site length =", Site_Length)
                print("Site length type =", type(Site_Length))

                if Site_Length > 32064:
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

        except urllib.error.URLError as e: #checks for no error in url access.
            print(e)
        except urllib.error.HTTPError as e: #checks for error 404, webpage not found.
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

            #else:
                #print('Web site does not exist')
        Website_URL = ""
        print("___________________________________________________________________________________________________")

        # website_is_up = status_code == 200
        # print(website_is_up)


        # TO DO: do if
        # 36539 is my case, when site contains info
        # 32064 is when site doesnt contain info 31872

#-------------------------------------------------------------------------------------------------------------------
        # saving to txt to verify data integrity
#         with open('readme.txt', 'a') as f:
#             f.write(str(Website_URL_Tests))
#             f.write('\n')
# f.close()

print()
print("Count of items inside array 0:", len(array[0]))
print("Count of arrays inside array:", len(array))
# try length only, not from 1 to lenght. this way, it cuts every combination behind Combined_List_Length
# to speed it up.

# use a counter to

# try multidimensional array to test a specific length.

# create a multidimensional array that contains a (Combined_List_Length) amount of arrays
# and each of those arrays contains Big_List (a to 0) This way,

# IGNORE -- it just requires 2 indexes, first is 0 to 46, and second one a to 0.
# each first index, 0, 1, 2 etc contains a, b c - 0, for so, 46 lists has been created with a to 0.
# then, have a for that goes from 46 to 0 (first index --), and a for that goes from 61 to 0 ( --)
# after the second for reaches 0, then the first for changesthe first index to -- and the second for
# goes again. this way

# reads the last element of the txt and if last char

# every item of the list is multiplied 62 times because the Big_List is made of 62 items. meaning
# aaa is going to be used 62 times, then aab 62 times and so on. its the same for every iteration.
# this could be used to build a template that doesnt require storage in ram, and that
# could be saved directly to txt.


# Combined_List = Combined_List[j] + str(k) #append to txt the txt last 62 lines + str(k)

# use txt last 62 lines, based on iteration/ counter * 62 + 1, starts on first line


# counter += 1 #to increase it after every iteration

# reads the last 62 lines, stores in array, and uses array + Big_List to create new column

# or array that is reused.
# requires 3 arrays, a temp array, a previous iteration array, and Big_List
# first iteration is big list, all is saved in txt.
# then big list is copied in combined list array, then this loop starts.
# combined list = combined list + Big_List
# txt = combined list
# big_list++
# isnt it the same as Combined_List.append(str(i)) but without having new appends? should i be constant?


# do I need a for? or just read text t

# rethink #substitute combined_list with last 62 lines


# Combined_List.append(Combined_List[j] + str(k)) #logic works, but gives memory error


# append adds to the end, so its not needed to know positioning, its just for combining the last
# 62 entries of that text to the Big_List to create a new column e.x aaa, aab, aac where aa = the first
# of the 62 entries and a, b, c = Big_list , new column.

# memory issues because the initialized array keeps increasing in size with each iteration.
# have the initialized array to be reused, so it frees memory.


# save in txt, have a counter that increases each iteration * x amount (sum of lower, upper and nums) so it identifies
# the line it will use to append the initial list.


# this combines the Combined_List with Big_List, and after its finished, takes the new Combined_List and
# combines it with Big_List again. Big_List has 1 position, Combined_List has 2, then becomes 3, so on.

# Because of MemoryError, instead of storing the combined list in ram memory, store it in a txt in the hdd

# Verifying the output
# print(Big_List)
# print(len(Big_List))
#
# print()

# print(Combined_List)
# print()
# print("Amount of iterations:", len(Combined_List))

# with open('readme.txt', 'w') as f:
#     for line in Combined_List:
#         f.write(line)
#         f.write('\n')
print()
end = time.time()
print("Time to compile:", round(end - start, 4), "seconds.")