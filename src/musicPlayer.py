#Author: Guan Zheng Huang
#Purpose: a music player that controls the flow of music

import piano
#import someInputHardware
'''
default list of songs
0: none
1: 7 base note
2: speedOfLightHigh
3: littleStarHigh
4: UWorldHigh
5: 9981
6: RickRoll
7: JoJo theme music
'''

# Description: music player that user can select songs, play, pause, restart, fast forward, back track, speed control
# Usage: user repeatetitively call one of the get functions for next note to play
# Hardware: no Hardware Interaction
# Dependency: one three text file for one song, high note, low note and inofmration file
#                   High: contains the high note normally played by human right hand
#                   Low: contains the low note normally played by human left hand
#                   Infor: contains tempo information and plack key to be pressed for the song
# Comment: The piano keys can be returned as physical key location, Note, or buzzer frequency
class musicPlayer:            
    #Abstraction: each object represent a seperate music player, one should not use a new player to play a new song
    
    #music note list: contains the notes in the current song
    highNote=[]
    lowNote=[]
    #Note counter: count the note being played (one for each buzzer)
    Hcount:int=0
    Lcount:int=0
    #piano instance
    pianoObj:piano
    #player attribute representation
    play:bool=False
    
    #Initiate new object with a default song
    #song: index of song to play, refere song list above
    def __init__(self, song):
        if (song == 0):
            return
        self.__playSong(song)
        
    #play a new song from the start (remmeber to start playMusic again)
    #song: index of new song to play
    def newSong(self, song):
        self.__clean()
        self.__playSong(song)
        
    #clean up and prepare for next song
    def __clean(self):
        self.highNote.clear()
        self.lowNote.clear()
        self.Hcount=0
        self.Lcount=0
        self.play=False
        
    #set up music by reading from file
    #songSelect: index of song to play
    def __playSong(self, songSelect):
        #list of song file, 3 file for each song
        if (songSelect == 0):
                songH="none.txt"
                songL="none.txt"
                songI="noneInfo.txt"
        elif (songSelect == 1):
                songH="sound.txt"
                songL="sound.txt"
                songI="soundInfo.txt"
        elif (songSelect == 2):
                songH="speedOfLightHigh.txt"
                songL="speedOfLightLow.txt"
                songI="speedOfLightInfo.txt"
        elif (songSelect == 3):
                songH="littleStarHigh.txt"
                songL="littleStarLow.txt"
                songI="littleStarInfo.txt"
        elif (songSelect == 4):
                songH="UWorldHigh.txt"
                songL="UWorldLow.txt"
                songI="UWorldInfo.txt"
        elif (songSelect == 5):
                songH="9981High.txt"
                songL="9981Low.txt"
                songI="9981Info.txt"
        elif (songSelect == 6):
                songH="RickRollHigh.txt"
                songL="RickRollLow.txt"
                songI="RickRollInfo.txt"
        elif (songSelect == 7):
                songH="JoJoHigh.txt"
                songL="JoJoLow.txt"
                songI="JoJoInfo.txt"
        else:
                print("Song select error")
        #read file
        #define your path here if changed
        fileHigh = open("data\musicSheet"+songH, "r")
        fileLow = open("data\musicSheet"+songL, "r")
        fileInfo = open("data\musicSheet"+songI, "r")
        fileHighContent = fileHigh.read()
        fileLowContent = fileLow.read()
        fileInfoContent = fileInfo.read()
        #parse file by comma
        highNoteS = fileHighContent.split(",")
        lowNoteS = fileLowContent.split(",")
        infoS = fileInfoContent.split(",")
        highNoteS = [x.strip() for x in highNoteS]
        lowNoteS = [x.strip() for x in lowNoteS]
        infoS = [x.strip() for x in infoS]
         
        info=[]
        print("note", highNoteS)
        #convert string parse to int parse
        for x in range(0, len(highNoteS)):
            #assign local note list
            self.highNote.append(float(highNoteS[x]))
            self.lowNote.append(float(lowNoteS[x]))
        for y in range(0, len(infoS)):
            #assign black key (plack pianoo key should be pressed instead)
            info.append(float(infoS[y]))
        #declare piano instance
        self.pianoObj=piano.PianoNote(info[0], info[1:], highNoteS, lowNoteS)
        #clean up
        fileHigh.close()
        fileLow.close()
        fileInfo.close()
        
    #get list of notes
    def getHighNoteList(self):
        return self.highNote
    def getLowNoteList(self):
        return self.lowNote
    
    #get note at defined location
    #index: location in current high.low note list
    def getHighNote(self, index):
        return self.highNote[index]
    def getLowNote(self, index):
        return self.lowNote[index]
    
    #get current note playing with out changing order
    def getHighNoteCurr(self):
        return self.highNote[self.Hcount]
    def getLowNoteCurr(self):
        return self.lowNote[self.Lcount]
    
    #get current pianoKey
    def getHighPKeyCurr(self):
        return self.pianoObj.getHighKey(self.highNote[self.Hcount])
    def getLowPKeyCurr(self):
        return self.pianoObj.getLowKey(self.lowNote[self.Lcount])
    
    #write music to replace song, have two mode, user can choose
    '''
    def writeSong(self):
        musicKeyPad=someHardware
        # find and replace all ".getKeys()[0]" with the get function for input device
        userMusicHigh=[]
        userMusicLow=[]
        
        #initilize input holder so enter loop
        currPress="someDelete"
        #only exsit if input =#
        while (currPress != "someEnter"):
            currPress=musicKeyPad.getKeys()[0]
            #cancel input
            if (currPress == "someDelete"):
                userMusicHigh.pop()
            elif (type(currPress) == int):
                #is pressing 0, enter as pause
                if (currPress == 0):
                    userMusicHigh.append(999)
                else:
                    #5=0, #6=0.5, #0=pause
                    print("record ", (currPress-5)/2)
                    userMusicHigh.append((currPress-5)/2)
                    
        #same as section above
        currPress="someDelete"
        while (currPress != "someEnter"):
            currPress=musicKeyPad.getKeys()[0]
            if (currPress == "someDelete"):
                userMusicLow.pop()
            elif (type(currPress) == int):
                #5=0, #6=0.5, #0=pause
                if (currPress == 0):
                    userMusicLow.append(999)
                else:
                    print("record ", (currPress-5)/2)
                    userMusicLow.append((currPress-5)/2)
        #high note length not equal to low error out, 
        if (len(userMusicLow) != len(userMusicLow)):
            return
        
        #record speed, in 3 digit input
        print("please input song speed (note/miniut) in 3 figure (exact: eg: 090, 110, 300)")
        digiCount=100
        currPress="someDelete"
        musicSpeed=0
        #if press #, exit, else record 3 digit, can be customized like guan Test but no need
        while (currPress != "someEnter" and digiCount >= 1):
            currPress=musicKeyPad.getKeys()[0]
            if (currPress == "someDelete"):
                print("invalid key try again")
            elif (type(currPress) == int):
                print("record ", (currPress-5)/2)
                musicSpeed+=digiCount*currPress
                digiCount=digiCount/10
                
        print ("music speed is", musicSpeed)
        
        #enter a list of black keys to press
        print("Please enter black keys to be pressed for high")
        currPress="someDelete"
        blackKey=[]
        while (currPress != "someEnter"):
            currPress=musicKeyPad.getKeys()[0]
            if (currPress == "someDelete"):
                blackKey.pop()
            elif (type(currPress) == int):
                
                #one should not have pause as black keys
                if (currPress == 0):
                    blackKey.pop()
                else:
                    #5=0, #6=0.5, #0=pause
                    print("record ", (currPress-5)/2)
                    blackKey.append((currPress-5)/2)
            
        #prepare to start playing music
        self.__clean()
        #print("high ", len(userMusicHigh), " low ", len(userMusicLow))
        self.highNote = userMusicHigh
        self.lowNote = userMusicLow
        print("record complete, enjoy your own song!")
        self.pianoObj=piano.PianoNote(musicSpeed, blackKey, userMusicHigh, userMusicLow)
    '''
    
    #you should call this to get next freq to play
    #it is suggested to call getHighFreq first before low
    # move "self.Hcount-=1" outside if if you want music to be silenced instead of paused
    # returns next high frequency of song to play, or 1 (silent) if song not playing
    # Modified: Song location counter
    def getHighFreq(self):
        #if still playing, return result, else return freq=1
        if (self.play == True):
            self.Hcount+=1
            # if reached end of high list but low list is still not over, error out
            if (self.Hcount-self.Lcount >= 2):
                print ("you are trying to access high Freq again without calling Low, this is bad")
            # if reached end of high list play nothing 
            if (self.Hcount == len(self.highNote)+1):
                return 1
            print(self.Hcount, self.Lcount )
            print("playin H Note" , self.highNote[self.Hcount-1], " at freq ", self.pianoObj.getHighPianoFreq(self.highNote[self.Hcount-1]))
            return self.pianoObj.getHighPianoFreq(self.highNote[self.Hcount-1])
        else:
            print ("music not playing")
            return 1
    
    #for more information see get highFreq above
    #you should call this to get hext freq to play
    #returns next low frequency of song
    def getLowFreq(self):
        if (self.play == True):
            self.Lcount+=1
            # music is over
            if (self.Lcount == len(self.lowNote)):
                self.play=False
            if (len(self.lowNote)<self.Lcount):
                print ("low shorter than high, do nothing")
                return 1
            print("note", self.lowNote[self.Lcount-1])
            return self.pianoObj.getLowPianoFreq(self.lowNote[self.Lcount-1])
        else:
            print ("music not playing")
            return 1
    
    #return the idea pause between note in second
    def getSpeed(self):
        return 60/self.pianoObj.tempo
    
    #return speed of song in of note/minuit (tempo)
    def getTemp(self):
        return self.pianoObj.tempo
    
    #fast forward x note, if skip>remain node, simply stop music
    #you can backtrack by setting amount negative
    #amount: number of note to skip forward/back
    def locationChange(self, amount):
        #pause if skip pass end of file
        if (self.Hcount+amount>len(self.highNote)):
            print("you tried to skip pass end of file")
            self.pauseMusic()
            self.Hcount=0
            self.Lcount=0
            return
        #restart if trying to go back to beginning
        if (self.Hcount+amount<0):
            print("you tried to skip pass start of file")
            self.Hcount=0
            self.Lcount=0
            return
        self.Hcount+=amount
        self.Lcount+=amount
        
    # return false if music over
    def isPlaying(self):
        return self.play
    
    # get current number of nude playing (in a sense how many node played since song start)
    def getCurrNoteNum(self):
        return self.Hcount
    
     # get in a sense how long since song start in ms
    def getPlayTime(self):
        return self.Hcount*self.getSpeed()
    
    #start playing (unpause music)
    #if playOn music that is over, restart
    def playMusic(self):
        if (self.Hcount == len(self.highNote)):
            self.Hcount=0
            self.Lcount=0
        self.play=True
        
    #pause music (futher call on current freq return 0)
    def pauseMusic(self):
        self.play=False    
