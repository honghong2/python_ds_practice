def weekday_name(day_of_week):
    
    
    weekday_dict = {1 : 'Sunday', 2 : 'Monday', 3 : 'Tuesday',  4 : 'Wednesday', 5 : 'Thursday', 6 : 'Friday', 7 : 'Saturday'}
    
    if day_of_week < 1 or day_of_week > 7:
        return None
    
    return weekday_dict[day_of_week]

print(weekday_name(6))