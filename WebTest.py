import urllib.request

url = "https://islandmedpr.com/app/foto/index.php?code=" + Website_URL_Tests[0] + "="

status_code = urllib.request.urlopen(url).getcode()
website_is_up = status_code == 200
print(website_is_up)

r = urllib.request.urlopen(url)
print("Site length: ", len(r.read()))

Site_Length = len(r.read())

if Site_Length > 32064:
    print("Online")
    with open('online.txt', 'a') as f:
        f.write(str(Website_URL_Tests))
        f.write('\n')
        f.close()

#TO DO: do if
#36539 is my case, when site contains info
#32064 is when site doesnt contain info 31872