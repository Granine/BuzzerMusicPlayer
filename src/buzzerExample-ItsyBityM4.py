#Author: Granine
#Purpose: demonstrate the functionality of music player on itsybitsy m4
import board
import pwmio
import time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
import piano
import musicPlayer

# Configure PWM buzzer and other state:
# Using two buzzers, one for High frequency, one for low, if two buzzer
# is different, louder buzzer should be High
# using pin D13 for High, D4 for low
BUZZER_High = board.D13
BUZZER_Low = board.D4

buzHigh = pwmio.PWMOut(
    BUZZER_High, variable_frequency=True
)
buzLow = pwmio.PWMOut(
    BUZZER_Low, variable_frequency=True
)
# Custuom duty_cycle of buzzer:
buzHigh.frequency = 1
buzHigh.duty_cycle = 2**15
buzLow.frequency = 1
buzLow.duty_cycle = 2**15

#one must rename this file to "main.py" to directly run on itsybity

#Keep playing the 7 base note in order on both buzzer, basic test
def buzzerTest():
    # Main loop will go through each tone in order up and down.
    
    print ("Starting to play 7 base tone")
    while True:
        # Play tones going from start to end of list.
        for i in range(len(piano.MusicRef.ToneTest)):
            buzHigh.frequency = piano.MusicRef.ToneTest[i]
            buzLow.frequency = piano.MusicRef.ToneTest[i]
            time.sleep(0.5)  # Half second delay.
        # Then play tones going from end to start of list.
        for i in range(len(piano.MusicRef.ToneTest)-1, -1, -1):
            buzHigh.frequency = piano.MusicRef.ToneTest[i]
            buzLow.frequency = piano.MusicRef.ToneTest[i]
            time.sleep(0.5)
        
 
# play two actual song, Untitled world and 9981, Utilizing the music player
# and piano simulator
def pianoSoundTest():
    print ("Music Player Start")
    # starting player, with song set to 4
    playSd = musicPlayer.musicPlayer(4)
    # start play
    playSd.playMusic()
    print ("Playing Untitled world")
    #Play each note until song is over
    while (playSd.isPlaying()):
            buzHigh.frequency = int(playSd.getHighFreq())
            buzLow.frequency = int(playSd.getLowFreq())
            # delay based on tempo
            time.sleep(playSd.getSpeed()) 
            
    playSd.newSong(5)
    playSd.playMusic()
    print ("Playing 9981")
    while (playSd.isPlaying()):
            buzHigh.frequency = int(playSd.getHighFreq())
            buzLow.frequency = int(playSd.getLowFreq())
            time.sleep(playSd.getSpeed())
            
    # Try to let user write music, should be disabled, uncomment only if 
    # physical input device exsist
    
    # playSd.writeSong()
    # playSd.playMusic()
            
def main():
   #buzzerTest()
    pianoSoundTest()

if __name__ == "__main__":
    main()
     
