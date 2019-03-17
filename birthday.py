import datetime

def print_header():
    print('---------------------------')
    print('           BIRTHDAY APP')
    print('---------------------------')
    print()
#getting birthday from user
def get_birthday_from_user():
    print('When were you born? ')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input ('Day [DD]: '))

    birthday = datetime.date(year, month, day)
    return birthday
#computing how many days your birthday was or will be
def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year,original_date.month, original_date.day )

    dt = this_year - target_date
    return dt.days
#print out how many days birthday will be in or how may days it was if your birthday wishing you a happy birthday
def print_birthday_informatoin(days):
   if days < 0:
       print('You had your birthday  {} days ago this year' .format(-days))
   elif days > 0:
       print('Your birthday is in {} days!'.format(days))
   else:
       print('Happy birthday!!!')
def main():
    print_header()
    bday = get_birthday_from_user()
    today= datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print(number_of_days)
    print_birthday_informatoin(number_of_days)

main()
