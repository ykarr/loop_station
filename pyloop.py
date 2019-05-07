import pygame
#
import threading,requests, time

#
import pyaudio
import wave

#
k=2
pygame.init() 
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 1
WHITE = (255, 255, 255) 
font = pygame.font.SysFont("comicsansms", 72) 
text = font.render("MP", True, (0, 128, 0)) 

pyscreen = pygame.display.set_mode((1024,768), 0, 32) 
pyscreen.fill(WHITE) 
pyscreen.blit(text,(512 - text.get_width() // 2, 384 - text.get_height() // 2)) 
pygame.display.flip() 

run = True 

c4 = pygame.mixer.Sound('1.wav') 
d4 = pygame.mixer.Sound('1.wav') 
e4 = pygame.mixer.Sound('1.wav') 
f4 = pygame.mixer.Sound('1.wav') 
g4 = pygame.mixer.Sound('1.wav') 
a4 = pygame.mixer.Sound('1.wav') 
b4 = pygame.mixer.Sound('1.wav') 
f5 = pygame.mixer.Sound('1.wav') 
g5 = pygame.mixer.Sound('1.wav') 
a5 = pygame.mixer.Sound('1.wav') 
b5 = pygame.mixer.Sound('1.wav') 


#미완 시작
def loop_a():
    while 1: 
         c5.play() 
def loop_b():
    while 1: 
         d5.play() 
def loop_c():
    while 1: 
        e5.play()

        
t1 = threading.Thread(target=loop_a)
t1.daemon = True 
t2 = threading.Thread(target=loop_b)
t2.daemon = True 
t3 = threading.Thread(target=loop_c)
t3.daemon = True 

    
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
            elif event.key == pygame.K_y: 
                d4.play() 

            elif event.key == pygame.K_t: 
                e4.play() 

            elif event.key == pygame.K_r: 
                f4.play() 

            elif event.key == pygame.K_e: 
                g4.play() 

            elif event.key == pygame.K_w: 
                a4.play() 

            elif event.key == pygame.K_q: 
                b4.play() 

            elif event.key == pygame.K_a:
                c5 = pygame.mixer.Sound('1.wav')#미완
                t1.start()

            elif event.key == pygame.K_s:
                d5 = pygame.mixer.Sound('2.wav')
                t2.start()
                 
            elif event.key == pygame.K_d:
                e5 = pygame.mixer.Sound('3.wav')
                t3.start()

            elif event.key == pygame.K_f: 
                f5.play() 

            elif event.key == pygame.K_g: 
                g5.play() 

            elif event.key == pygame.K_h: 
                a5.play() 

            elif event.key == pygame.K_j: 
                b5.play() 
                 
pygame.quit() 
