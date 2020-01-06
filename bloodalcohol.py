"""
BAC (Blood Alcohol Content) calculator with Widmark factor

The goal of this program is to show the BAC calculation method with Widmark
factor. Be careful, this is not a real alcohol-meter. If you want to know your
exact BAC, buy an alcohol-sensor. However, there are different rules in
different countries about drinking and driving, please DO NOT DRIVE if you have
drunk alcohol.
After a party walk, call a cab, an Uber or use the public transport.
"""

alcohol_density = 0.789 # g/cm^3
widmark_factor = {"man": 0.7,
                  "woman": 0.6}

gender = input('Are you man or woman? ')
drink_volume = float(input('Volume of drink (dl): ')) # dl
alcohol_concentration = float(input('Alcohol concentration (V/V%): '))
body_weight = float(input('body weight (kg): '))

bac = drink_volume * alcohol_concentration * alcohol_density / body_weight / widmark_factor[gender] # g
print(bac)


