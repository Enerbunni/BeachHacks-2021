import tkinter as tkinter
from datetime import date

# creates the
def monthGenerator(startDate, numberOfDays):
    dayNames = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    for nameNumber in range(len(dayNames)):
        names = tkinter.Label(window, text = dayNames[nameNumber])
        names.grid(column = nameNumber, row = 0)

    index = 0
    day = 1
    for row in range(6):
        for column in range(7):
            if index >= startDate and index <= startDate + numberOfDays-1:
                t = tkinter.Label(window, text= day)
                t.grid(row=row + 1, column=column)
                day += 1
            index += 1
            #line = canvas.create_line(0, 500, 500, 500)


# create function for calculating if it is a leap year
def isLeapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# create function for calculating what day month starts


def dayMonthStarts(month, year):
    # get last two digits (default 21 for 2021)
    lastTwoYear = year - 2000
    # integer division by 4
    calculation = lastTwoYear // 4
    # add day of month (always 1)
    calculation += 1
    # table for adding proper month key
    if month == 1 or month == 8:
        calculation += 1
    elif month == 2 or month == 3 or month == 11:
        calculation += 1
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
    # check if the year is a leap year
    leapYear = isLeapYear(year)
    # subtract 1 if it is January or February of a leap year
    if leapYear and month == 1 or month == 2:
        calculation -= 1
    # add century code (assume we are in 2000's)
    calculation += 6
    # add last two digits to the caluclation
    calculation += lastTwoYear
    # get number output based on calculation (Sunday = 1, Monday =2..... Saturday =0)
    dayOfWeek = calculation % 7
    return dayOfWeek

#create function to figure out how many days are in a month
def daysInMonth (month, year):
    #all months that have 31 days
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 12 or month == 10:
        numberDays = 31
    #all months that have 30 days
    elif month == 4 or month == 6 or month == 9 or month == 11:
        numberDays = 30
    else:
        #check to see if leap year to determine how many days in Feb
        leapYear = isLeapYear(year)
        if leapYear:
            numberDays = 29
        else:
            numberDays = 28
    return numberDays
    
        

dayOf1st = dayMonthStarts ( date.today().month, date.today().year)

numberDaysofMonth = daysInMonth ( date.today().month, date.today().year)

window = tkinter.Tk()
window.title("Calender")
window.geometry("1000x800")
frame1 = tkinter.Frame(window)
#frame1.pack(background)


today = date.today()
monthGenerator(dayMonthStarts(today.month, today.year), daysInMonth(today.month, today.year))
window.mainloop()
