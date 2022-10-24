from datetime import datetime, date 

def from_string(date_time):
    format = '%d-%m-%Y'  # The format
    date_obj = datetime.strptime(date_time, format).date()
    return date_obj

def today_date():
    today = date.today()
    return today

def diff_dates(fecha_desde, fecha_hasta):
    if fecha_hasta < fecha_desde:
        raise ValueError("Fecha Hasta < Fecha Desde")
    date_diff = fecha_hasta - fecha_desde
    totalDays = date_diff.days
    years = totalDays // 365
    months = (totalDays - years * 365) // 30
    days = (totalDays - years * 365 - months * 30)
    return (years, months, days)