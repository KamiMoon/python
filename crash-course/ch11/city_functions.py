def city_country(city, country, population=0):
    result = city + ", " + country
    if(population > 0):
        result += " - " + str(population)
    return result