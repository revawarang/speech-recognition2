import speech_recognition as sr
import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD
GPIO.setmode(GPIO.BCM)
lcd_rs = 26
lcd_en = 19

lcd_d4 = 13
lcd_d5 = 6
lcd_d6 = 5
lcd_d7 = 11
lcd_columns = 16
lcd_rows = 2
lcd_backlight = 15

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,  lcd_columns, lcd_rows, lcd_backlight )
lcd.message("Say Password")
time.sleep(5.0)
lcd.clear()  
#enter the name of usb microphone that you found 
#using lsusb 


mic_name = "USB PnP Sound Device: Audio (hw:1,0)"
#Sample rate is how often values are recorded 

#sample_rate = 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data) 
#here.  
#it is advisable to use powers of 2 such as 1024 or 2048 

#chunk_size = 2048
#Initialize the recognizer 

r = sr.Recognizer() 

  
#generate a list of all audio cards/microphones 

mic_list = sr.Microphone.list_microphone_names() 

  
#the following loop aims to set the device ID of the mic that 
#we specifically want to use to avoid ambiguity. 

for i, microphone_name in enumerate(mic_list): 

    if microphone_name == mic_name: 

        device_id = i 

  
#use the microphone as source for input. Here, we also specify  
#which device ID to specifically look for incase the microphone  
#is not working, an error will pop up saying "device_id undefined" 

with sr.Microphone(device_index = device_id) as source: 

    #wait for a second to let the recognizer adjust the  

    #energy threshold based on the surrounding noise level 

    r.adjust_for_ambient_noise(source) 

    print ("Say Something")

    #listens for the user's input 

    audio = r.listen(source) 

          

    try: 

        text = r.recognize_google(audio) 

        

        
        if (text=="password"):
            lcd.message("opened")
            time.sleep(5.0)
            lcd.clear()
          
          
        else:
             lcd.message("incorrect password")
             time.sleep(5.0)
             lcd.clear()
    





        
    #error occurs when google could not understand what was said 

      

    except sr.UnknownValueError: 

        print("Google Speech Recognition could not understand audio") 

      

    except sr.RequestError as e: 

        print("Could not request results from Google  Speech Recognition service; {0}".format(e)) 
 