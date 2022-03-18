from .make_json import word_of_the_day
from datetime import datetime
import platform

def get_os():
    if platform.system() not in ['Linux', 'Darwin', 'Java', 'Windows']:
        return None
    return platform.system()

def get_word(day):
    start_day = datetime.strptime('17/Jun/2021', '%d/%b/%Y')
    day_diff=(day-start_day.date()).days
    if day_diff<0 or day_diff>2314:
        return None 
    word=word_of_the_day(day_diff)[day_diff].upper()
    return word

def get_date():
    today=datetime.now().date()
    return today