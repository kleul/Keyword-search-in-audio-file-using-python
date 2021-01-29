import pyaudio, sys
import os
import warnings
import pyttsx3
import random
import speech_recognition as sr
import nltk
from nltk.corpus import PlaintextCorpusReader
import wave
import contextlib
import datetime
import time
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from pydub import AudioSegment
from pydub.playback import play
import pydub

engine = pyttsx3.init()



def speak(text):
    engine.say(text) 
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        audio = r.listen(source)
        user = r.recognize_sphinx(audio)
        try:
            return r.recognize_sphinx(audio)
        except sr.UnknownValueError:
            speak('Command unrecognized! Please try again')
            print('Command unrecognized! Please try again')
        #except sr.RequestError as e:
           # print("Recog Error (0))".format(e))

        return ""


    
def getReady():
    r = sr.Recognizer()
    speak('Locating file of Subject!')
    dirname = os.getcwd()
    for name in os.listdir(dirname):
            path = os.path.join(dirname, name)

            if os.path.isfile(path):
              
               if name == "Subject.WAV":
                    targetpath = path
    file_audio = sr.AudioFile(targetpath)
    speak('File located!')
    with file_audio as source:
        speak('Opening file!')
        print('Opening file!')
        file1 = open('myfile.txt', 'w')
        speak('File opened!')
        print('File opened!')
        speak('Recording Source...')
        print('Recording Source...')
        audio_text = r.record(source)
        speak('Recorded!...')
        print('Recorded!...')
        speak('Transcription in progress...This may take a while!')
        print('Transcription in progress...This may take a while!')
        textt = (type(audio_text))
        text_output = r.recognize_sphinx(audio_text)
        speak('Getting ready to write...')
        print('Getting ready to write...')
        sentence = nltk.sent_tokenize(text_output)
        file1.write('{0}' .format(sentence))
        file1.close()
        speak('Text has been written...')
        print('Text has been written...')
        speak('Process Completed! File is ready for analysis.')
        print('Process Completed! File is ready for analysis.')
        speak('Listening, Please provide your keyword...')
        print('Listening, Please provide your keyword...')
        command = listen()
        print(command)
        speak('Searching file for keyword')
        print('Searching file for keyword')
        search(command)



def search(x):
        speak('Initiating search...')
        print('Initiating search...')
        file = open('myfile.txt', 'r')
        read_file = file.read()
        text = nltk.Text(nltk.word_tokenize(read_file))
        words = word_tokenize(read_file)
        match = text.concordance(x)
        ##########################
        for i in range(len(words)):
            if words[i] == x:
                length = len(words)
                wordindx = i
                devidend = length / wordindx
                #specify the length of audio file
                dirname = os.getcwd()
                for name in os.listdir(dirname):
                        path = os.path.join(dirname, name)

                        if os.path.isfile(path):
                          
                           if name == "Subject.WAV":
                                targetpath = path
                                fname = targetpath
                with contextlib.closing(wave.open(fname,'r')) as f:
                        frames = f.getnframes()
                        rate = f.getframerate()
                        duration = frames / float(rate)
                        #calculate time in seconds
                        timeinsec = duration / devidend
                        timeinmili = timeinsec * 1000
                        timetoend = timeinmili + 12000
                        #convert seconds to TIME
                        timeintime = time.strftime('%H:%M:%S', time.gmtime(timeinsec))
                        print('Found At Time  : ',timeintime)
                        wav_file = AudioSegment.from_file(file = "Subject.WAV", format = "wav")
                        splice = wav_file[timeinmili:timetoend]
                        play(splice)
                        #####################################
        ##########################
        print('RESPECTIVLY')
        speak('Search completed!, Results are displayed on your screen...')
        print('Search completed!, Results are displayed on your screen...')
        speak('Search again? or Back to menu?, Please give your command...')
        print('Search again? or Back to menu?, Please give your command...')
        command1 = listen()
        print(command1)
        if command1 == "menu":
            mainfunction(source)
        if command1 == "search":
            speak('Listening, Please provide your keyword...')
            print('Listening, Please provide your keyword...')
            command2 = listen()
            print(command2)
            speak('Searching file for keyword')
            print('Searching file for keyword')
            search(command2)
       


def mainfunction(source):
   # warnings.filterwarnings("ignore")
    speak('System up')
    print('System up')
    speak('waiting for command')
    print('waiting for command!')
    user = listen()
    print(user)
    if user == "ready":
            getReady()
    if user == "locate":
            speak('Listening, Please provide your keyword...')
            print('Listening, Please provide your keyword...')
            command3 = listen()
            print(command3)
            speak('Searching file for keyword')
            print('Searching file for keyword')
            search(command3)
    

     
def loop():
    if __name__ == "__main__":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            while 1:
                mainfunction(source)



loop()
