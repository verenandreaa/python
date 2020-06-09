print("Enter your date of birth (mm dd yyyy)")
Date_of_birth = input("->")

print("Today's date: (mm dd yyyy)")
Todays_date = input("->")


import datetime
def calculate_age(born):
    today = datetime.date.today()
    return datetime.date(today.year - born.year - ((today.month, today.day) < (born.month, born.day)))

age = calculate_age(Date_of_birth)