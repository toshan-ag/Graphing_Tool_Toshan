# Graphing_Tool_Toshan

Graphing Tool is my self-project made as a part of CBSE Class 12 Computer Science Project during the year 2022-23. I have made a few changes during my UG Freshie year as well. I would look to develop it further in order to learn more about frontend and backend using python,

Features:
- NOTE: The Project runs ONLY on my LOCAL PC as the MySQL server has a localhost.
- The Graphing Tool starts off with a login screen whose interface is designed using Tkinter while the login and registration details are stored and checked using MySQL local server. All possibilites of login are checked in the login screen:
    * During login , check whether username exists, if yes, then check for passwd. If passwd is right, then login else no login.
    * During login, if username does not exist, then prompt user to register as a new user.
    * During registration, check if username already exists. If password matches then prompt that user is already resgitered. If password doesn't match, then prompt the user to use a different username. If uername does not exist, then register user.
- After successful login, the TOOL moves to the terminal and it provides three choices:
    * Plot data from a csv file => Implemented using csv module, matplotlib and file handling methods.
    * Plot an equation of the form y = f(x) => Implemented using matplotlib and numpy
    * Plot the data of closing prices of stocks over a specified range of time => implemented using datetime, yfinance and pandas modules.
    * Exit
