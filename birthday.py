import datetime

def get_birthdays_per_week(users):
    today = datetime.date.today()

    birthday_dict = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': []
    }

    for user in users:
        birthday = user['birthday'].date()
        day_of_week = birthday.strftime('%A')
        if birthday >= today and birthday < today + datetime.timedelta(days=7):
            
            if day_of_week in ['Saturday', 'Sunday']:
                birthday_dict['Monday'].append(user['name'])
                
            else:
                birthday_dict[day_of_week].append(user['name'])

    for day, names in birthday_dict.items():
        if names:
            print(f'{day}: {", ".join(names)}')

users = [
    {'name': 'Bill', 'birthday': datetime.datetime(2023, 8, 21)},
    {'name': 'Jill', 'birthday': datetime.datetime(2023, 8, 22)},
    {'name': 'Kim', 'birthday': datetime.datetime(2023, 8, 19)},
    {'name': 'Jan', 'birthday': datetime.datetime(2023, 8, 20)},
]

get_birthdays_per_week(users)