from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

# Variabler

hub = PrimeHub()

# Program

while True: # Vis rød eller grønn lanternelys basert på helningen til basen
    
    helning = hub.motion_sensor.get_roll_angle() # Hent og lagre verdien på helning fra gyro-sensoren til variabelen 'helning' 
    
    if helning > 5: # Når basen heller mot høyre, lys opp hjemkanppen til grønn
        hub.status_light.on('green')
    
    elif helning < -5: # Når basen heller mot venstre, lys opp hjemkanppen til rød
        hub.status_light.on('red')

    else: # Når basen ikke heller, lys opp hjemkanppen til gult
        hub.status_light.on('yellow')

    print(helning) # Skriv verdien på helning til consollen i Spike-appen
    
    if hub.left_button.is_pressed(): # Avslutt programmet ved å trykke på venstre knapp på basen
        break
