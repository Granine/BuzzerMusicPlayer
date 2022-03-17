#Author: Guan Zheng Huang
#simulation of piano with piano sheet file (converted to txt)
import MusicRef

#a class that represents a piano sheet digitally to frequency
# high/lowNote: for simplicity, each note is represented at location on Staff
#location 0= first note below line (high tone D), location 0.5= note on line above 0 (E3), 1=F, -0.5=C1 etc
#tempo: represents the song speed, should be reasonable size (depend on buzzer)
#black note: specifies which note shoule be played with black key
class PianoNote:
    #default frequency of general Piano, different buzzer might need adjustment
    #Base_Freq=440
    Base_Freq=2640
    tempo:int
    #note to press black instead of white
    blackNote=[]
    #note list (in human reable form (reference at 0=space below bottom line, each line is 0.5 gap, space is 0.5))
    highNote=[]
    lowNote=[]
    
    #Create song with nessaosry indormation
    def __init__(self, tempo, blackNote, highNote, lowNote):
        self.blackNote = blackNote
        self.tempo = tempo
        self.highNote=highNote
        self.lowNote=lowNote
    
    #overwrite default Frequency to account for buzzer difference
    def freqOverwrite(self, freq):
        self.Base_Freq=freq
    
    #return key on piano based on note informatiuon
    def highKeyLook(self, Loc:float):
        highKeyTb=[-1, 35, 37, 39, 40,                                                    #-2 to -0.5
                    42, 44, 45, 47, 49, 51, 52, 54, 56, 57, 59, 61, 63, 64, 66, 68, 69, 71]        #0 location to 8.5
        if (Loc>100):
            return -1
        return highKeyTb[int(2*Loc+5)]
    #return key on piano based on note informatiuon
    def lowKeyLook(self, Loc:float):
        lowKeyTb=[4, 6, 8, 9, 11, 13, 15, 16, 18, 20,                                                    #-5 to -0.5
                    21, 23, 25, 27, 28, 30, 32, 33, 35, 37, 39, 40, 42, 44, 45, 47, 49]        #0 location to 8
        if (Loc>100):
            return -1
        return lowKeyTb[int(2*Loc+10)]
        
    #return key pressed sequence on piano based on note information
    def highKeyList(self):
        highKey=[]
        for x in range(len(self.highNote)):
            #calculate note on piano
            if (x not in self.blackNote):
                highKey.append(self.highKeyLook(x))
            elif (x in self.blackNote):
                # all low key is one position before 1
                highKey.append(self.highKeyLook(x)-1)
        return highKey
    
   #return key pressed sequence on piano based on note information
    def lowKeyList(self):
        lowKey=[]
        for x in range(len(self.lowNote)):
            #calculate note on piano
            if ((x+1) not in self.blackNote):
                lowKey.append(self.lowKeyLook(x))
            elif (x in self.blackNote):
                # all low key is one position before 1
                lowKey.append(self.lowKeyLook(x)-1)

        return lowKey
    
    #return key press on piano based on note information
    #note: note object
    def getHighKey(self, note:float):
        if (note not in self.blackNote):
                return self.highKeyLook(note)
        elif (note in self.blackNote):
                # all low key is one position before 1
                return self.highKeyLook(note)-1
            
    #return key presse on piano based on note information
    #note: note object
    def getLowKey(self, note:float):
        if (note not in self.blackNote):
                return self.lowKeyLook(note)
        elif (note in self.blackNote):
                # all low key is one position before 1
                return self.lowKeyLook(note)-1
                
    #map piano keys to frequency based on base frequency
    #Key: keys on piano counted form left
    def getGenFreq(self, key):
        if (key>100):
            return 1
        return 440*(2**((key-49)/12))
    
    #map keys to frequency based on base frequency
    #note: note object 
    def getHighPianoFreq(self, note):
        if (note>100):
            return 1
        return self.Base_Freq*(2**((self.getHighKey(note)-49)/12))
    
    
    
    #map keys to freequency based on base frequency
    #note: note object 
    def getLowPianoFreq(self, note):
        if (note>100):
            return 1
        return self.Base_Freq*(2**((self.getLowKey(note)-49)/12))
    
    #return complete list of high frequency
    def getHighFreqAll(self):
        freqList=[0]
        for x in range(len(self.highNote)):
            freqList.append(self.Base_Freq*(2**((x-49)/12)))
        return freqList
    
     #return complete list of low frequency
    def getLowFreqAll(self):
        freqList=[0]
        for x in range(len(self.lowNote)):
            freqList.append(self.Base_Freq*(2**((x-49)/12)))
        return freqList

