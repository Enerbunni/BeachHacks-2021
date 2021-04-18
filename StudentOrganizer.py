import json
import tkinter as tkinter
from tkinter import filedialog
from datetime import date

# Sets the month and year variable based on the current date
month = date.today().month
year = date.today().year

#create function to output the month and year
def printMonthYear(month, year):
    
    # Create table for the written month
    if month == 1:
        writtenMonth = "January"
    elif month == 2:
        writtenMonth = "February"
    elif month == 3:
        writtenMonth = "March"
    elif month == 4:
        writtenMonth = "April"
    elif month == 5:
        writtenMonth = "May"
    elif month == 6:
        writtenMonth = "June"
    elif month == 7:
        writtenMonth = "July"
    elif month == 8:
        writtenMonth = "August"
    elif month == 9:
        writtenMonth = "September"
    elif month == 10:
        writtenMonth = "October"
    elif month == 11:
        writtenMonth = "November"
    else:
        writtenMonth = "December"

    #output month and year at top of calendar
    monthYear = tkinter.Label(calendarFrame,  text = writtenMonth + " " + str(year), font= ("Arial", 20))
    monthYear.grid(column = 2, row = 0, columnspan = 3)

# Function to switch month calendar (1 for forwards and -1 for backwards)
def switchMonths(direction):
    global calendarFrame
    global month
    global year
    #check if we are goint to a new year
    if month == 12 and direction == 1:
        month = 0
        year += 1
    if month == 1 and direction == -1:
        month = 13 
        year -= 1
    #reprint the calendar witht the new values
    calendarFrame.destroy()
    calendarFrame = tkinter.Frame(window)
    calendarFrame.grid()
    printMonthYear(month + direction, year) # pylint: disable=E0601
    makeButtons()
    monthGenerator(dayMonthStarts(month + direction, year), daysInMonth(month + direction, year))
    month += direction
  


# Change month buttons at top of the page
def makeButtons():
    goBack = tkinter.Button(calendarFrame, text = "<", command = lambda : switchMonths(-1))
    goBack.grid(column = 0, row = 0)
    goForward = tkinter.Button(calendarFrame, text = ">", command = lambda : switchMonths(1))
    goForward.grid(column = 6, row = 0)


# Creates most of the calendar
def monthGenerator(startDate, numberOfDays):
    # Holds the names for each day of the week 
    dayNames = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # Places the days of the week on the top of the calender
    for nameNumber in range(len(dayNames)):
        names = tkinter.Label(calendarFrame, text = dayNames[nameNumber], fg = "black")
        names.grid(column = nameNumber, row = 1, sticky = 'nsew')

    index = 0
    day = 1
    for row in range(6):
        for column in range(7):
            if index >= startDate and index <= startDate + numberOfDays-1:
                # Creates a frame that will hold each day and text box
                dayFrame = tkinter.Frame(calendarFrame)

                # Creates a textbox inside the dayframe
                t = tkinter.Text(dayFrame, width = 15, height = 5)
                t.grid(row = 1)

                # Adds the text object to the save dict
                textObjectDict[day] = t 

                # Changes changes dayframe to be formated correctly
                dayFrame.grid(row=row + 2, column=column, sticky = 'nsew')
                dayFrame.columnconfigure(0, weight = 1)
                dayNumber = tkinter.Label(dayFrame, text = day)
                dayNumber.grid(row = 0)
                day += 1
            index += 1
    # Creates the buttons to load and save JSON's
    loadFrom = tkinter.Button(calendarFrame, text="load month from...", command = loadFromJSON)
    saveToButton = tkinter.Button(calendarFrame, text="save month to...", command = saveToJSON)

    # Places them below the calendar
    loadFrom.grid(row = 8, column = 4)
    saveToButton.grid(row = 8, column = 2)



def saveToJSON():
    # Saves the raw text data from the text objects 
    for day in range(len(textObjectDict)):
        saveDict[day] = textObjectDict[day + 1].get("1.0", "end - 1 chars")

    # Asks the user for a file location and saves a JSON containg the text for each day. 
    fileLocation = filedialog.asksaveasfilename(initialdir = "/", title = "Save JSON to..")
    if fileLocation != '':
        with open(fileLocation, 'w') as jFile:
            json.dump(saveDict, jFile)

def loadFromJSON():
    # Asks the user for a JSON file to open 
    fileLocation = filedialog.askopenfilename(initialdir = "/", title = "Select a JSON to open")
    if fileLocation != '':
        f = open(fileLocation)
        global saveDict
        saveDict = json.load(f)

        # Copies the saved text data to the current text objects
        for day in range(len(textObjectDict)):
            textObjectDict[day + 1].insert("1.0", saveDict[str(day)])
    
    
# Create function for calculating if it is a leap year
def isLeapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# Create function for calculating what day month starts
def dayMonthStarts(month, year):
    # Get last two digits (default 21 for 2021)
    lastTwoYear = year - 2000
    # Integer division by 4
    calculation = lastTwoYear // 4
    # Add day of month (always 1)
    calculation += 1
    # Table for adding proper month key
    if month == 1 or month == 10:
        calculation += 1
    elif month == 2 or month == 3 or month == 11:
        calculation += 4
    elif month == 5:
        calculation += 2
    elif month == 6:
        calculation += 5
    elif month == 8:
        calculation += 3
    elif month == 9 or month == 12:
        calculation += 6
    else:
        calculation += 0
    # Check if the year is a leap year
    leapYear = isLeapYear(year)
    # Subtract 1 if it is January or February of a leap year
    if leapYear and (month == 1 or month == 2):
        calculation -= 1
    # Add century code (assume we are in 2000's)
    calculation += 6
    # Add last two digits to the caluclation
    calculation += lastTwoYear
    # Get number output based on calculation (Sunday = 1, Monday =2..... Saturday =0)
    dayOfWeek = calculation % 7
    return dayOfWeek

# Create function to figure out how many days are in a month
def daysInMonth (month, year):
    # All months that have 31 days
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 12 or month == 10:
        numberDays = 31
    # All months that have 30 days
    elif month == 4 or month == 6 or month == 9 or month == 11:
        numberDays = 30
    else:
        # Check to see if leap year to determine how many days in Feb
        leapYear = isLeapYear(year)
        if leapYear:
            numberDays = 29
        else:
            numberDays = 28
    return numberDays

# Holds the raw text input for each day
saveDict = {}

# Holds the text objects on each day
textObjectDict = {}

# Creates the root window
window = tkinter.Tk()
window.title("Calender")
window.geometry("1000x800")

# Centers the calendar
window.columnconfigure(0, weight = 1)

# Creates frames from the main root window.
calendarFrame = tkinter.Frame(window)

# This makes the grid object appear
calendarFrame.grid()

today = date.today()

printMonthYear(month, year)
makeButtons()
monthGenerator(dayMonthStarts(month, year), daysInMonth(month, year))



window.mainloop()
