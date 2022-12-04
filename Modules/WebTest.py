#module dedicated to Web functions management. This module can have more functions to expand program capabilities.

import urllib.request
from Modules.OS_Files_Manager import Store_Results

def Check_URL(url):
    try:
        r = urllib.request.urlopen(url)
        getcode_url = urllib.request.urlopen(url).getcode()
        if getcode_url == 200: #checks if site exist, and saves the URL and info on txt.
            print('Web page exists.')
            Site_Length = len(r.read())
            print("Site length =", Site_Length)
            print("Site length type =", type(Site_Length))
            if Site_Length > 1: #Filters placeholder sites with no info. #36539 Y, 31872 & 32064 N
                print("Contains relevant information.")
                Results = "Online"
                Store_Results(Results, url, 0, 0)
        else:
            print("Unhandled code, see UnhandledCodes.txt for more information.")
            Results = "UnhandledCodes"
            Store_Results(Results, url, getcode_url, 0)
    except urllib.error.URLError as e:  #checks for no error in url access.
        print(e)
    except urllib.error.HTTPError as e:  #checks for error 404, webpage not found.
        print(e)
    else:
        print("Unhandled error, see UnhandledErrors.txt for more information.")
        Results = "UnhandledErrors"
        Store_Results(Results, url, 0, urllib.error)