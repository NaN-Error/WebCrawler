#get all links from a website, and store them in a sql database.
import mysql.connector
import requests
from bs4 import BeautifulSoup

# Connect to the MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="user",
  password="password",
  database="database"
)
cursor = db.cursor()

# Fetch the website's HTML code
url = "http://www.example.com"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Find all links on the page
links = soup.find_all('a')

# Save the links in the database
for link in links:
  cursor.execute("INSERT INTO links (url) VALUES (%s)", (link['href'],))
  db.commit()

# Close the database connection
db.close()