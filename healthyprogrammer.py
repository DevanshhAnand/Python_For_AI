
from cmath import log
from syslog import LOG_NOTICE
from turtle import done
from pygame import init, mixer
from datetime import datetime
from time import sleep, time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    
    while True:
        # sleep(1)
        input_of_user = input("Enter drank to stop the music ")
        if input_of_user == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__=='__main__':
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    watersec=5
    exsecs=7
    eyesecs=9

    while True:
        if time()-init_water > watersec:
            print("Water Drinking Time, Enter 'drank' to stop the alaram. ")
            musiconloop('water.mp3','drank')
            init_water=time()
            log_now("Drank Water At")

        if time()-init_eyes > eyesecs:
            print("Eyes Exercise time, Enter 'done' to stop the alaram. ")
            musiconloop('eyes.mp3','done')
            init_eyes = time()
            log_now("Done Exercise At ")

        if time()-init_exercise > exsecs:
            print("Physical Exercise time, Enter 'done' to stop the alaram. ")
            musiconloop('exercise.mp3','done')
            init_exercise = time()
            log_now("Done Physical Exercise At ")