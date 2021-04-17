import tkinter as tkinter
from datetime import date

window = tkinter.Tk()
window.title("Calender")
window.geometry("1000x800")
btn = tkinter.Button(window, text = 'This should quit the program', bd = '5', command = window.destroy)
btn.pack(side = 'right')
window.mainloop()

#create function for calculating if it is a leap year
def isLeapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 ==0):
        return True
    else:
        return False

#create function for calculating what day month starts
def dayMonthStarts (month, year):
    #get last two digits (default 21 for 2021)
    lastTwoYear = year - 2000
    #integer division by 4
    calculation = lastTwoYear // 4
    #add day of month (always 1) 
    calculation += 1
    #table for adding proper month key
    if month == 1 or month == 8:
        calculation += 1
    elif month == 2 or month == 3 or month == 11:
        calculation += 1
    elif month == 5:
        calculation += 2
    elif month == 6:
        calculation += 5
    elif month == 8:
        calcualtion += 3
    elif month == 9 or month == 12:
        calculation += 6
    else:
        calculation += 0
    #check if the year is a leap year
    leapYear = isLeapYear(year)
    #subtract 1 if it is January or February of a leap year
    if leapYear and month == 1 or month == 2:
        calculation -= 1
    #add century code (assume we are in 2000's)
    calculation += 6
    #add last two digits to the caluclation
    calculation += lastTwoYear
    #get number output based on calculation (Sunday = 1, Monday =2..... Saturday =0)
    dayOfWeek = calculation % 7
    return dayOfWeek

    
        

dayOf1st = dayMonthStarts ( date.today().month, date.today().year)
print(dayOf1st)