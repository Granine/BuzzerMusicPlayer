# BuzzerMusicPlayer
A music player that uses standard Buzzers (Tested with Piezo and Magnetic) to simulate and play baisc piano sheets. 

## Requirement / hardware:
- Microcontroller with pwm output
- Two buzzer
    - one buzzer for low tone (low frequency as represented by human left hand in piano)
    - one buzzer for high tone (high frequency as represented by human right hand in piano)
- If one desires to add their own song they will need actual music sheet that must be hand typed into a text file. Image recongnition is not supported due to scale of the project

## Sample use case
After setting up two buzzer on microcontroller one create an musicPlayer object, this sets up a new music player for the user. User repetiviely call the get function on the musicPlayer instance for the next frequency to play, returned frequency should take turn write to the buzzer. 

sudo code for structure (different depending on system)
while (playSd.isPlaying()):
    buzzerHigh = player.getHighFreq()
    buzzerLow = player.getLowFreq()
    time.sleep(player.getSpeed()) 

## Current feature: 
### piano simulator: simulate piano keypress logic and play on buzzer accordingly
- support 78/88 out of piano keys (other keys out of bound for buzzer frequency)
- allows dynamic base frequency offset to (simple music filter)
parse note data into piano keys (you can play it even if you never learned piano!)
- support different speed settings (tempo)

### music player: a built in music player that allows
- song selection
- pause/play song
- fast forward/go back
- have multiple music player instance (so two song can play individually with isoluated time/stop play stautus)
- support various other feature like get run time, get current note, get all music note etc
- read from file instead of code, so user can change with music without modifying the code (disabled as itsybitsy have weird file order)