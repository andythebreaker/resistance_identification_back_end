from datetime import datetime

def dateTimeNowStr():
    # datetime object containing current date and time
    now = datetime.now()
    
    print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
    print("date and time =", dt_string)	
    return dt_string

print(dateTimeNowStr())