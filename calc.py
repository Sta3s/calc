
# konvertē datu mērvienības
def megabyte_to_megabit(megabyte):
   result = megabyte*8
   return result

# saskaiti degvielas patēriņu uz 100 km
def fuel_consumption(litres, kilometers):
   km = kilometers/100
   result = litres/km
   return result

# konvertē temperatūru
def celsius_to_fahrenheit(celsius):
    result = celsius*1.8 + 32
    return result

# saliec visus skaitļus pirms dota skaitļa (izmanto for)
def sigma(tail):
    result = 0
    for i in range(int(tail)):
        result += i+1
        #print(result)
    return result

# nokonvertē svaru uz tuvāko mērvienību - grams, kilograms, tonna (izmanto if)
def weight(grams):
    if grams >= 1000 and grams < 1000000:
        return str(int(grams/1000)) + "kg"
    elif grams >= 1000000:
        return str(int(grams/1000000)) + "t"
    else:
        return str(int(grams)) + "g"
    


