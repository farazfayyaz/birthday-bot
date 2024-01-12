from datetime import date

# Dictionary with person's name and birthday
birthdays = {
    "Andrew Gervasi" : "05/04",
    "Toreona Walls" : "11/02",
    "Mom" : "09/23",
    "Isha" : "12/18",
    "Insha" : "08/06",
    "Faisal" : "12/24",
    "Erin" : "07/20",
    "Andres" : "08/22",
    "Olu" : "04/28",
    "Faraz" : "12/07"
}

def find_birthday_today():
    today_date = date.today() # today's date
    today = today_date.strftime("%m/%d") # today's date in MM/DD format

    # iterates through dictionary
    for name, birthday in birthdays.items():
        if birthday == today:
            return f"Hey, it's {name}'s birthday today!" # result if birthday was found matching today
    
    return "There is no birthday today!" # result if no birthday matched with today

print("Today's Date: ", date.today().strftime("%m/%d")) # Print's today's date

result = find_birthday_today() # runs function to check birthday and compare to today and stores result

print(result) # returns result
