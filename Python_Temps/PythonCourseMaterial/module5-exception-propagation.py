def get_day(user_info):
    day = int(input('What is the day of your bday? '))
    user_info.append(day)
    
print()

def get_month(user_info):
    month = int(input('What is the month (1-12) of your bday? '))
    user_info.append(month)
    
print()

def get_year(user_info):
    year = int(input('What is the year of your bday? '))
    user_info.append(year)
    
print()

def get_user_bday(user_info):
    get_day(user_info)
    get_month(user_info)
    get_year(user_info)
    print('So your bday is', user_info)
    
print()

print('Hi, I Will collect some info about your bday! ')
user_info = []
get_user_bday(user_info)