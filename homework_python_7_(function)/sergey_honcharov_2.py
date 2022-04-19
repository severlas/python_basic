def month_of_season(month):
    if (month >= 1) and (month < 3) or month == 12:
        season = 'winter'
        return season
    if (month >= 3) and (month < 6):
        season = 'spring'
        return season
    if (month >= 6) and (month < 9):
        season = 'summer'
        return season
    if (month >= 9) and (month < 12):
        season = 'autumn'
        return season


month_ = int(input('Введите номер месяца: '))
season_ = month_of_season(month_)
print(season_)
