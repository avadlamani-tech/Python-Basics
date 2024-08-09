def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


# convert the boiling point of water
water_bp = celsius_to_fahrenheit(100)
print(water_bp) #212.0