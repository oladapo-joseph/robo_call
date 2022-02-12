from ast import Try
import os
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse




class Robotcall:
    """
        Calling app for automated voice messaging

        Requires registration on Twilio, the ssid, authentication token,
        registered phone number.
    
    """


    def __init__(self,file_to_play):
        """
            Attach the xml file at the point of initiation, the xml file contains the 
            response format, the action word play and a link to the audio message.
            The audio message has to be in mp3 format and very small in size. 
        """
        self.phone = ''
        self.called = []
        self.file = file_to_play


    def __repr__(self) -> str:
        """
            Returns info about the class
        """
        x = " ".join(self.called)
        return 'Phone number is {} \nCalling this number {},\nPlaying this music file:{}'.format(self.phone, x, self.file)



    def call(self, number):
        client = Client(self.SSID,self.TOKEN)
        try:
            to_call = client.calls.create(
                to=str(number),
                from_=self.phone,
                url = self.file) 
            
            print(to_call.sid)
        except ConnectionError as e:
            print('Unable to connect to Internet ')
        self.called.append(number)
        return 


    def get_token(self, name_of_file):
        tokens = []
        with open(name_of_file, 'r') as file:
            self.SSID = file.readline()
            self.TOKEN, self.phone = [str(line) for line in file]
                
FILE = 'https://github.com/oladapo-joseph/robo_call/blob/main/voice.xml'
TOKENS = 'tokens.txt'
PHONE = '+2347019080897'

if __name__ =='__main__':
    robot = Robotcall(FILE)
    robot.get_token(TOKENS)
    robot.call(PHONE)
    print(robot)



