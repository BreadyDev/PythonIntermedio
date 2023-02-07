### Dates ###

# Datetime

from datetime import datetime

def print_datetime(date):
    print(f"\nAño: {date.year}")
    print(f"Mes: {date.month}")
    print(f"Dia: {date.day}")
    print(f"Hora: {date.hour}")
    print(f"Minuto: {date.minute}")
    print(f"Segundo: {date.second}")
    print(f"Time stamp: {date.timestamp()}\n")
    
now = datetime.now()

print_datetime(now)


año_2023 = datetime(2023,1,1)

print_datetime(año_2023)

# Time

from datetime import time

def print_time(date):
    print(f"\nHora: {date.hour}")
    print(f"Minuto: {date.minute}")
    print(f"Segundo: {date.second}\n")

current_time = time(20, 6, 15)
print_time(current_time)

# Date

from datetime import date

def print_date (date):
    print(f"\nAño: {date.year}")
    print(f"Mes: {date.month}")
    print(f"Dia: {date.day}\n")

current_date = date.today()
print_date(current_date)

current_date = date(2023, 2, 7)
print_date(current_date)

# Operaciones

diff = now - año_2023
print(f"\nDiferencia: {diff}")

diff = current_date - año_2023.date()
print(f"\nDiferencia: {diff}")

print(f"Tipo: {type(diff)}\n")

from datetime import timedelta

start_time_delta = timedelta(200, 100, 100, weeks= 10)

end_time_delta = timedelta(300, 100, 100, weeks= 13)

print(end_time_delta - start_time_delta)
print(end_time_delta + start_time_delta)