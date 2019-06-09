import pygame

#
import threading,requests, time

#

import pyaudio

import wave

#

k=1

pygame.init() 

CHUNK = 1024

FORMAT = pyaudio.paInt16

CHANNELS = 2

RATE = 48000

RECORD_SECONDS = 5

WHITE = (255, 255, 255) 

font = pygame.font.SysFont("comicsansms", 72) 

text = font.render("MP", True, (0, 128, 0)) 

 

pyscreen = pygame.display.set_mode((500,300), 0, 32) 
pyscreen.fill(WHITE) 
pyscreen.blit(text,(text.get_width() // 2,text.get_height() // 2)) 
pygame.display.flip() 


run = True 

 

#미완 시작

def loop_a():
    a5 = pygame.mixer.Sound('1.wav')#미완
    while 1:
        print("1")
        a5.play()
        time.sleep(20);
        
def loop_s():
    s5 = pygame.mixer.Sound('2.wav')
    while 1:
        print("2")
        s5.play()
        time.sleep(20);

def loop_d():
    d5 = pygame.mixer.Sound('3.wav') 
    while 1: 
        print("3")
        d5.play()
        time.sleep(20)

def loop_f():
    f5 = pygame.mixer.Sound('4.wav')#미완
    while 1:
        print("4")
        f5.play()
        time.sleep(20)
def loop_g():
    g5 = pygame.mixer.Sound('5.wav')#미완
    while 1:
        print("5")
        g5.play()
        time.sleep(20)
def loop_h():
    h5 = pygame.mixer.Sound('6.wav')#미완
    while 1:
        print("6")
        h5.play()
        time.sleep(20)
def loop_j():
    j5 = pygame.mixer.Sound('7.wav')#미완
    while 1:
        print("7")
        j5.play()
        time.sleep(5)

def loop_k():
    k5 = pygame.mixer.Sound('8.wav')#미완
    while 1:
        print("8")
        k5.play()
        time.sleep(5)
def loop_l():
    l5 = pygame.mixer.Sound('9.wav')#미완
    while 1:
        print("9")
        l5.play()
        time.sleep(5)

t1 = threading.Thread(target=loop_a)
t1.daemon = True 

t2 = threading.Thread(target=loop_s)
t2.daemon = True 

t3 = threading.Thread(target=loop_d)
t3.daemon = True 

t4 = threading.Thread(target=loop_f)
t4.daemon = True 

t5 = threading.Thread(target=loop_g)
t5.daemon = True

t6 = threading.Thread(target=loop_h)
t6.daemon = True

t7 = threading.Thread(target=loop_j)
t7.daemon = True

t8 = threading.Thread(target=loop_k)
t8.daemon = True

t9 = threading.Thread(target=loop_l)
t9.daemon = True


while run: 

    for event in pygame.event.get(): 

        if event.type == pygame.KEYDOWN: 

            if event.key == pygame.K_ESCAPE: #esc

                run = False 

 

            elif event.key == pygame.K_u: #u

                j=k

                WAVE_OUTPUT_FILENAME = str(j)+".wav"

                p = pyaudio.PyAudio()

                stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

 

                print("Start to record the audio.")

                frames = []

                for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):

                    data = stream.read(CHUNK)

                    frames.append(data)

                print("Recording is finished.")

 

                stream.stop_stream()

                stream.close()

                p.terminate()

                wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')

                wf.setnchannels(CHANNELS)

                wf.setsampwidth(p.get_sample_size(FORMAT))

                wf.setframerate(RATE)

                wf.writeframes(b''.join(frames))

                wf.close()

                #c4.play()

                k=k+1

                print(k)

            elif event.key == pygame.K_a: 
                t1.start()


            elif event.key == pygame.K_s: 
                t2.start()


            elif event.key == pygame.K_d: 
                t3.start() 


            elif event.key == pygame.K_f: 
                t4.start() 


            elif event.key == pygame.K_g: 
                t5.start()


            elif event.key == pygame.K_h: 
                t6.start() 


            elif event.key == pygame.K_j:
                t7.start() 


            elif event.key == pygame.K_k:
                t8.start()
 
                 
            elif event.key == pygame.K_l:
                t9.start()
           

pygame.quit() 
