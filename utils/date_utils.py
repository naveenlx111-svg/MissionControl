from datetime import datetime

def days_remaining(target_date):
    target = datetime.strptime(target_date,"%Y-%m-%d")
    today = datetime.now()

    return (target-today).days