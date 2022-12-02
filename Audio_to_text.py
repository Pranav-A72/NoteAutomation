
"""
# device module?
import sounddevice
"""

import speech_recognition as sr
import pyttsx3

# Init recognizer object
speechrecognizer = sr.Recognizer()


def SpeakText(command):
	
	# Init eingine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
	
	
#INFINTE LOOP
while(1):
	
    #exception Handler? hopefully pls work
	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			
            # delay for background adjust
			speechrecognizer.adjust_for_ambient_noise(source2, duration=0.2)
			
			audio2 = speechrecognizer.listen(source2)
			
			# Using google to recognize audio
			OutputText = speechrecognizer.recognize_google(audio2)
			OutputText = OutputText.lower()

			print("OUTPUT:", OutputText)
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occurred")

