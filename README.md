Web Utilities Program
Overview
This script provides a GUI for selecting and executing various web-related tasks. Users can choose options like brute-force webpage discovery, link extraction, and keyword-based webpage monitoring. The GUI is built using Tkinter, and the script integrates various modules to perform specific tasks efficiently.
Features
- GUI Interface: Built with Tkinter for easy option selection.
- Brute Force Webpage Discovery: Uses the Brute_Force module to find webpages.
- Link Extraction: Finds all links on a specified website.
- Keyword Monitoring: Monitors a webpage for specific keywords.
- Execution Time Tracking: Measures and displays the program's execution time.
Requirements
Python 3.x
Tkinter (included with Python)
Additional required modules (specified in `Modules`)
Installation
Clone the repository:
```
git clone https://github.com/YourUsername/Web-Utilities-Program](https://github.com/NaN-Error/WebCrawler.git
cd Web-Utilities-Program
```
Install dependencies:
```
pip install -r requirements.txt
```
Usage
Run the application:
```
python main.py
```
1. Choose an Option: Select a task from the GUI.
2. Execute Task: Click "Start" to execute the selected task.
3. Monitor Output: Follow on-screen instructions and view results.
File Structure
```
Web-Utilities-Program/
│
├── .gitignore                  # Specifies files to ignore
├── requirements.txt            # Lists the required dependencies
├── main.py                     # Main script for the application
├── Modules/
│   ├── Brute_Force.py          # Module for brute force webpage discovery
│   ├── textChange_alert.py     # Module for keyword monitoring
│   └── ...
└── README.md                   # This README file
```
Author
[WB]
