import urllib.request

def Check_URL(url, Databases_Path):
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
                with open(Databases_Path / 'Online.txt', 'a') as f:
                    f.write("Webpage: ")
                    f.write(url)
                    f.write('\n')
                    f.close()
        else:
            print("Unhandled code, see UnhandledCodes.txt for more information.")
            with open(Databases_Path / 'UnhandledCodes.txt', 'a') as f:
                f.write("Unhandled Code: ")
                f.write(getcode_url)
                f.write("- Webpage:")
                f.write(url)
                f.write('\n')
                f.close()
    except urllib.error.URLError as e:  #checks for no error in url access.
        print(e)
    except urllib.error.HTTPError as e:  #checks for error 404, webpage not found.
        print(e)
    else:
        print("Unhandled error, see UnhandledErrors.txt for more information.")
        with open(Databases_Path / 'UnhandledErrors.txt', 'a') as f:
            f.write("Unhandled Error: ")
            f.write(str(urllib.error))
            f.write("- Webpage:")
            f.write(url)
            f.write('\n')
            f.close()