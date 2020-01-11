from datetime import datetime


def get_timestamp():
    try:
        return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
    except:
        return "An error ocured"
