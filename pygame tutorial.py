#In order to play music,pygame.mixer is used for loading and playing sounds.

from pygame import mixer 

#Starting the mixer
mixer.init()

#Loading the song
mixer.music.load("C:\\music\\bahli_sohni.mp3")

#Setting the volume
mixer.music.set_volume(0.7)

#Start playing the song
mixer.music.play()


#infinite loop
while True:
    print("Press 'p' for pause ,'r' to resume")

    print("press 'e' to exit the program")
    
    #User Input
    query = input("")


    #If press p - song pause
    if query == 'p':
        mixer.music.pause()

    
    #if press r - song unpause
    elif query == 'r':
        mixer.music.unpause()

    #If press e - song stop
    elif query == 'e':
        mixer.music.stop()
        break
