Automated Web Search Script
This is a very simple Python script that opens your browser and performs a series of predefined Google searches. It’s meant to be easy to run and easy to modify — no complicated setup needed.

How It Works
The script contains a list called search_items.
Each item in the list will be searched on Google in your default browser.
Thre is a 5-second pause before moving to the next search.
<img width="645" height="140" alt="image" src="https://github.com/user-attachments/assets/d7f45b70-5c88-4aba-94d7-e5f897696eb6" /><br>

You can edit the search terms directly in the list.
Running the Script

Create a new Python file in VS Code or any IDE of your choice.
Copy the script into the file.
Run the program.

That’s it — the browser will start opening search tabs one by one.

Modifying Search Terms
Open the file and edit the values inside:
<img width="1094" height="347" alt="image" src="https://github.com/user-attachments/assets/de2c16f5-b28e-43ad-818a-63327f341dba" />

Stopping the Script
If you want to terminate the program while it’s running:
Press Ctrl + C in the terminal.
This will stop the next searches from opening.

Requirements
Python 3 installed
No external libraries required
Uses built-in modules like webbrowser, time and os

Purpose
This small project is mainly for practice — automating simple browser actions and working with loops, delays, and basic Python modules.
