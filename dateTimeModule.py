# Imports
from datetime import datetime, timedelta, date
from time import strftime

my_age = date(1992, 6, 6) + timedelta(days=15000)
print(my_age.strftime("%Y-%m-%d %H:%M:%S"))

def main():
    now = datetime.now()
    utc = datetime.utcnow()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    print(utc.strftime("%Y-%m-%d %H:%M:%S"))
    print(f'Offset: {now.utcoffset()}')

    # Time
    print(f'Hour: {now.hour}')
    print(f'Minute: {now.minute}')
    print(f'Second: {now.second}')
    print(f'Micro: {now.microsecond}')

    # Date
    print(f'Year: {now.year}')
    print(f'Month: {now.month}')
    print(f'Day: {now.day}')

    # Timedelta
    print(f"Next Month: {now + timedelta(days=30)}")
    print(f"Last week: {now + timedelta(weeks=-1)}")

    # ISO Strings
    d = datetime.fromisoformat('2022-09-01')
    print(d)

    try:
        m = datetime.fromisoformat('2022-09-01')
    except Exception as ex:
        print(ex.args)

    print(f"ISO: {now.isoformat()}")

if __name__ == "__main__":
    main()