import time
import random
import datetime
from math import log
print ("Welcome to Stanley's Rocket Calculator")
input("Press enter to continue...")
name = input("What should we call your rocket?: ")
drymass = input("How heavy is the dry mass of the rocket in kilos: ")
wetmass = input("How heavy is the wet mass of the rocket in kilos: ")
fuelmass = input("How heavy is the fuel of the rocket: ")
burntime = input ("What is the burn time of your rocket: ")
massflow = float(wetmass)-float(drymass)/float(burntime)
exhaustvelocity = input ("What is your exhaust velocity: ")
thrust = float(exhaustvelocity)*float(massflow)
deltav = float(exhaustvelocity)*log(float(wetmass)/float(drymass))
print (f"""Summary:
Name: {name}
Burn Time: {burntime}
Fuel Mass: {fuelmass}
Dry Mass: {drymass}
Wet Mass: {wetmass}
Mass Flow: {massflow}
Exhaust Velocity: {exhaustvelocity}
Thrust: {thrust}
Rocket Birthdate: {datetime.date.today()}
""")

