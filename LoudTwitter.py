#Author: @Whimsical1337 on twitter and https://www.twitch.tv/whimsicaldragon1337 on twitch
#Please join me on twitch some time and you can watch me code other awful things like this!

#Special Thanks:
#Keebo, the smart for helping with debugging this mess @secodntotopkek on twitter and https://www.twitch.tv/zeus_pants on twitch
#RandomGuy14x for moral support https://www.twitch.tv/randomguy14x on twitch
#Aquafiinaa because she asked me to idk? https://twitter.com/Aguafiina/status/1305749820276178945 @Aguafiina on twitter and https://www.twitch.tv/aquafiinaa on twitch
#You for taking the time to look at and read this mess

import requests
import json
import time
import os


# This is setup to run on a pi using omxplayer to play the sounds
#If you want to use this on windows use the playsound library, if you use mac please stop :)
#import playsound #import the library
def dit():
    time.sleep(0.05)
    os.system('omxplayer -o local /home/pi/Desktop/dit.mp3') #Change to playsound('path/to/file.mp3') for windows
    time.sleep(0.05)
    print(".")
def dah():
    time.sleep(0.05)
    os.system('omxplayer -o local /home/pi/Desktop/dah.mp3')
    time.sleep(0.05)
    print("-")
def newcharPause():
    print("Pause")
    time.sleep(0.3)

#This morse code is accurate, but you can change it if you want
lettertoMorse = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----",
    " " : " "
}


def morseDo(*argv):
    for x in range(len(argv[0])):
        if argv[0][x] == "-":
            dah() 
        elif argv[0][x] == ".":
            dit()
        else:
            newcharPause()

headers = {
    'Authorization': 'Bearer <Your bearer token here>', #You can get one by applying to be a twitter dev
}

#Gets the current rules
response = requests.get('https://api.twitter.com/2/tweets/search/stream/rules', headers=headers)

print(response.json())

headers = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer <Your bearer token here>',
}
#Change @Yourhandle to the your twitter handle
data = '{ "add": [{ "value": "@Yourhandle" }] }' #TODO: Fix this so we can search for @Yourhandle #! instead

response = requests.post("https://api.twitter.com/2/tweets/search/stream/rules", headers=headers, data=data)
#Adds @Yourhandle to the rules
print(response.json())

# If you messed up run this section to delete a rule
#data = '{"delete": {"values": ["@Wronghandle"] } }'
#response = requests.post("https://api.twitter.com/2/tweets/search/stream/rules", headers=headers, data=data)
#print(response.json())


#Set headers back to normal to stream
headers = {
    'Authorization': 'Bearer <Your bearer token here>',
}


s = requests.Session()
with s.get('https://api.twitter.com/2/tweets/search/stream', headers=headers, stream=True) as resp:
        print("foo")
        for line in resp.iter_lines():
            if len(line) > 5:
                print(line)
                newJson = json.loads(line)
                print(newJson["data"])
                #Change 14 to the length of your handle including the @
                print(newJson["data"]["text"][14:])
                textin = newJson["data"]["text"][14:] 
                if textin[1] == "#" and textin[2] == "!":
                    os.system('omxplayer -o local /home/pi/Desktop/movie_1.mp3')
                    textin = textin.upper()
                    textout = ""
                    for x in textin:
                        try:
                            textout += lettertoMorse[x] + " "
                        except:
                            textout += ""
                    print(textout)
                    morseDo(textout)
                    print(newJson["data"]["text"])
                    print("Foo")
                    print("oof")
                else:
                    print("Not a command")
print(response.json())