from datetime import datetime, date

def get_days_from_today(date):
    try:
        input_day = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - input_day).days
    except ValueError:
        return "Введіть правильний формат дати наприклад'2024-01-01'"

print(get_days_from_today("2024-08-12"))
