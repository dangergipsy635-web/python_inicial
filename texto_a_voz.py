import pyttsx3

#inicializar el motor
motor = pyttsx3.init()
texto = "hola mundo, te leo un cuento."
motor.say(texto)
motor.runAndWait()