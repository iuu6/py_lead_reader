from __future__ import print_function
import BIC.speech_segmentation as bic_seg
import listensin_die_audio_python_one_file as check
import tkinter
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import Scale
from tkinter import Label,PhotoImage
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import Toplevel
from pymediainfo import MediaInfo
import re
from tkinter import Message
import threading
import pygame
import time
import os
import random
from tkinter.filedialog   import askopenfilename
from tkinter.filedialog import askdirectory
from tkinter import StringVar
from pydub import AudioSegment
import wave
import shutil
import sys
from sys import path
import easygui
from playsound import playsound
import pyaudio
import wave
import os.path
import soundfile as sf

top=tkinter.Tk()
top.geometry("800x450")
top.title("英语听力播放器")
def printsrceen(texts):
    t=int(texts)
    top.attributes("-alpha",t/100)
 
screenwidth = top.winfo_screenwidth()
screenheight = top.winfo_screenheight() - 100

pygame.init()
path=StringVar()
paths=StringVar()
patht=StringVar()
v=StringVar()
v1=StringVar()


def callback():#搜索本地文件
    path_= askopenfilename() 
    return path_





def selectPath():#随机播放
    folder_path="D:/音乐"
    folder_list = os.listdir(folder_path)#遍历文件夹里面每个文件
    list=[]
    count=0
    for i in folder_list:#将文件夹里的文件按顺序传提给变量i  此处区别os.walk()
        if os.path.splitext(i)[1]=='.flac':#提取特定后缀文件'.***'
            list.append (i)
        #print(type(list))
            count=count+1
    #print(count)
           
    s=random.randint(0,(count-1))#获取随机数
    file=list[s]
    fil=folder_path+"\\"+file
 
   
    pygame.mixer.music.load(fil)
    pygame.mixer.music.play(1,0)
    media_info = MediaInfo.parse(fil)
    data = media_info.to_json()#medio到json()这两行是获取文件的所有属性
    rst=re.search('other_duration.*?(.*?)min(.*?)s.*?',data)
    t=int(rst.group(0)[19:20])
    r=int(rst.group(0)[-4:-2])
    m=(t*60+r)*1000
    
    musictime=str(t)+':'+str(r)
    l2.config(text=file)
    l3.config(text=musictime)
    lbTime=tkinter.Label(top,anchor='w')
    lbTime.place(x=25,y=150)
    def autoclose():
        for i in range(m//1000):
            lbTime['text']='-{} /'.format((m//1000)-i)
            time.sleep(1)
    t=threading.Thread(target=autoclose)
    t.start()
    loopl=top.after(m,selectPath)



def printScale(text):
    t=int(text)
    pygame.mixer.music.set_volume(t/100)
    
def update_timeText():
    # Get the current time, note you can change the format as you wish
    current = time.strftime("%H:%M:%S")#获取当前时间

# Update the timeText Label box with the current time
    timeText.configure(text=current)

# Call the update_timeText() function after 1 second
    top.after(1000, update_timeText)


    

'''
    
    
def reminds():
    top = Toplevel()
    top.title('使用提示')
    top.geometry("200x200")
    t="宝贝可以休息一会啦"
    msg = Message(top,text = t)
    msg.config( font=('times', 24, 'italic'))
    msg.place(x=0,y=0)
    folder_path="D:/音乐"
    folder_list = os.listdir(folder_path)#遍历文件夹里面每个文件
    list=[]
    count=0
    for i in folder_list:#将文件夹里的文件按顺序传提给变量i  此处区别os.walk()
        if os.path.splitext(i)[1]=='.flac':#提取特定后缀文件'.***'
            list.append (i)
        #print(type(list))
            count=count+1
        #print(count)
    s=random.randint(0,(count-1))
    file=list[s]
    fil=folder_path+"\\"+file
    pygame.mixer.music.load(fil)
    pygame.mixer.music.play(1,0)
    lbTime=tkinter.Label(top,fg="red",anchor='w')
    lbTime.place(x=100,y=45)
    def autoclose():
        for i in range(300):
            lbTime['text']='距离窗口关闭还有{}秒'.format(300-i)
            time.sleep(1)
        top.destroy()
    t=threading.Thread(target=autoclose)
    t.start()
    loopl=top.after(60*60000,reminds)

'''
    

def play():#播放音乐
    f=callback()#选择制定文件
    pygame.mixer.music.load(f)
    pygame.mixer.music.play()
    path.set(f)
    media_info = MediaInfo.parse(f)
    data = media_info.to_json()#medio到json()这两行是获取文件的所有属性
    rst=re.search('other_duration.*?(.*?)min(.*?)s.*?',data)
    t=int(rst.group(0)[19:20])
    r=int(rst.group(0)[-4:-2])
    m=(t*60+r)*1000
    musictime=str(t)+':'+str(r)
#    l2.config(text=f)
#    l3.config(text=musictime)
    lbTime=tkinter.Label(top,anchor='w')
    lbTime.place(x=25,y=150)
    def autoclose():
        for i in range(m//1000):
            lbTime['text']='-{} /'.format((m//1000)-i)
            time.sleep(1)
    t=threading.Thread(target=autoclose)
    t.start()
#    loopl=top.after(m,selectPath)
    
'''
def cut_the_record():#切割音频
    f1=callback()#选择制定文件
    #如果给定的音乐不是wav，是MP3，则mp3 转wav
    if os.path.splitext(f1)[1]=='.mp3':
        sound = AudioSegment.from_mp3(f1)
        sound.export('%s.wav'%os.path.splitext(f1)[0],format ='wav')
    f1=os.path.splitext(f1)[0]+'.wav'

    easygui.msgbox("即将开始分割，可能耗费大量系统资源!但我认为这非常值得，如果您认为这样不好，请关闭该程序！", ok_button="我同意!")
    sig, sample_rate = sf.read(f1)
    qiegetime=(sig.shape[0]/sample_rate)*0.07
    qiegetime=str(qiegetime)
    easygui.msgbox(("我们预计需要大约"+qiegetime+"秒"), ok_button="嗯!")
    # -*- coding:UTF-8 -*-
    frame_size = 256
    frame_shift = 128
    sr = 16000

    seg_point = bic_seg.multi_segmentation(f1, sr, frame_size, frame_shift, plot_seg=True, save_seg=True,cluster_method='bic')
    print('The segmentation point for this audio file is listed (Unit: /s)', seg_point)
    easygui.msgbox("我们已对您的音频完成分割处理，所有文件保存在save_audio文件夹内！", ok_button="谢谢!")

'''
def lead_the_reading():#领读音频

    f1=callback()#选择制定文件
    #如果给定的音乐不是wav，是MP3，则mp3 转wav
    if os.path.splitext(f1)[1]=='.mp3':
        sound = AudioSegment.from_mp3(f1)
        sound.export('%s.wav'%os.path.splitext(f1)[0],format ='wav')
    f1=os.path.splitext(f1)[0]+'.wav'
    
    cmd = "ffmpeg -i "+f1+".wav -ac 1 -ar 16000 "+f1+".wav"
    # 执行命令
    os.system(cmd)

    easygui.msgbox("即将开始分割，可能耗费大量系统资源!但我认为这非常值得，如果您认为这样不好，请关闭该程序！", ok_button="我同意!")
    sig, sample_rate = sf.read(f1)
    qiegetime=(sig.shape[0]/sample_rate)*0.07
    qiegetime=("%.2f" % qiegetime)
    qiegetime=str(qiegetime)
    easygui.msgbox(("我们预计需要大约"+qiegetime+"秒"), ok_button="嗯!")
   # -*- coding:UTF-8 -*-
    frame_size = 256
    frame_shift = 128
    sr = 16000

    seg_point = bic_seg.multi_segmentation(f1, sr, frame_size, frame_shift, plot_seg=True, save_seg=True,cluster_method='bic')
#    print('The segmentation point for this audio file is listed (Unit: /s)', seg_point)
    easygui.msgbox("我们已对您的音频完成分割处理，所有文件保存在save_audio文件夹内！我们检测到了一些问题，我们会自己处理！", ok_button="谢谢!")
    os.mkdir('save_wrong')
    # 音频存放文件夹相对路径
    filedir = "save_audio"
    
    # 获取目录下所有文件
    files = os.listdir(filedir)
    
    # 获取目录下所有的WAV文件
    wav_files = list()

    for i in files:
        if os.path.splitext(i)[1] == '.wav':
            wav_files.append(i)
#    print(wav_files)
#    print(len(wav_files))
    the_things_for_wrong = len(wav_files)
    the_things_for_wrong=str(the_things_for_wrong)
#    print(the_things_for_wrong)
    counts = 0
    counts = str(counts)
    
    while True:
       cmd = "ffmpeg -i save_audio/"+ counts +".wav -ac 1 -ar 16000 save_wrong/"+ counts +".wav"
       os.system(cmd)
       counts = int(counts)
       counts = counts + 1
       counts = str(counts)
       #print(counts)
       if counts == the_things_for_wrong:
           break

    easygui.msgbox("错误处理完成", ok_button="谢谢!")
    shutil.rmtree("save_audio")
    shutil.move("save_wrong","save_audio")

######################
#    f2=callback()#选择制定文件
    easygui.msgbox("我们即将开始领读，在此其他，我们需要使用您的麦克风用来录音！", ok_button="我同意!")

    timed=0
    a=0
    b=0
    HowLong = 0
#    HowLong = easygui.enterbox(msg='您希望播放的最短时长是（默认值为0）：', title='请输入', default='', strip=True, image=None, root=None)
#    HowLong=input("How long do you want to stop: ")
    HowLong=int(HowLong)
#    print(HowLong)
    # 音频存放文件夹相对路径
    filedir = "save_audio"
    
    # 获取目录下所有文件
    files = os.listdir(filedir)
    
    # 获取目录下所有的WAV文件
    wav_files = list()

    for i in files:
        if os.path.splitext(i)[1] == '.wav':
            wav_files.append(i)
#    print(wav_files)
#    print(len(wav_files))
    
    for i in range(len(wav_files)):
        
        #playsound("D:\py_speech_seg_master\save_audio\\%s.wav"%i)
        musicFileName = "save_audio\\%s.wav"%i
        sig, sample_rate = sf.read(musicFileName)
        
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        #RECORD_SECONDS = sig.shape[0]/sample_rate+1
        #WAVE_OUTPUT_FILENAME = "D:\py_speech_seg_master\save_audio\\record%s.wav"%i
    
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        timed=timed+(sig.shape[0]/sample_rate)
#        print(timed)
        if timed > HowLong:
            RECORD_SECONDS = timed+1
            while a <= i:
                playsound("save_audio\\%s.wav"%a)
                a=a+1

            playsound("start_record.wav")
#            print("开始录音,请说话......")
        
            frames = []
            WAVE_OUTPUT_FILENAME = "save_audio\\record%s.wav"%b
            b=b+1
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

#            print("录音结束!")
            playsound("end_record.wav")
            stream.stop_stream()
            stream.close()
            p.terminate()

            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
            timed=0

    countss = 0
    countss = str(countss)
    
    while True:
       pinfeng1 = "save_audio/"+ countss +".wav"
       pinfeng2 = "save_audio/record"+ countss +".wav"
       check.wav_die_check(pinfeng1,pinfeng2)
       countss = int(countss)
       countss = countss + 1
       countss = str(countss)
       #print(countss)
       if countss == the_things_for_wrong:
           break

def stop():
    pygame.mixer.music.stop()#停止播放
    top.after_cancel(loopl)
def pause():
    pygame.mixer.music.pause()#暂停   
def unpause():
    pygame.mixer.music.unpause()#继续播放

def choosepic():#保存的路径不能有中文，若需要中文则把/换成\
    path_s=askopenfilename()
    paths.set(path_s)
    img_open=Image.open(e1.get())
    img=ImageTk.PhotoImage(img_open)
    l1.config(image=img)
    l1.image=img



    
def create():
    top = Toplevel()
    top.title('使用提示')
    top.geometry("450x400")
    t="功能一：直接播放：即直接播放音频，通过暂停等等，来控制\n功能二：领读，点击就可以开始对您的音频切割，领读，打分！"
    msg = Message(top,text = t)
    msg.config( font=('times', 24, 'italic'))
    msg.place(x=0,y=0)

def create2():
    top = Toplevel()
    top.title('使用提示')
    top.geometry("450x400")
    t="感谢深圳灵声讯科技提供语音相似度打分python SDK，有需要学习资料可以联系QQ群：696554058"
    msg = Message(top,text = t)
    msg.config( font=('times', 24, 'italic'))
    msg.place(x=0,y=0)

def loop():
    top.after(60*60000,reminds)
    top.after(60*59500,remind)

    
def loops():
     selectPath()
def gettime():
    t=time.strftime('%H%M%S')
    s=int(t[0:2])
    d=int(t[2:4])
    f=int(t[4:6])
    g=s*60*60+d*60+f
    return g    


    
errmsg = 'Error!'
#时间
timeText = Label(top, text="", font=("Helvetica", 15))
timeText.place(x=200,y=385)
update_timeText()
#选择文件直接播放
Button(top,text="选择文件直接播放",command=play,width=13,bg="deepskyblue").place(x=16,y=20)
Entry(top,text=path,width=25,state='readonly').place(x=120,y=20)
'''
#选择文件切割
Button(top,text="选择文件进行切割",command=cut_the_record,width=13,bg="deepskyblue").place(x=16,y=55)
Entry(top,text=path,width=25,state='readonly').place(x=120,y=55)
'''
#选择文件领读播放
Button(top,text="选择文件领读播放",command=lead_the_reading,width=13,bg="deepskyblue").place(x=16,y=55)
Entry(top,text=path,width=25,state='readonly').place(x=120,y=55)

#选择图片
Button(top,text='选择图片', command=choosepic,width=13,bg="deepskyblue").place(x=16,y=90)
e1=Entry(top,text=paths,state='readonly',width=25)
e1.place(x=120,y=90)
l1=Label(top)#图片放置位置
l1.place(x=320,y=0)

#暂停，继续播放，结束播放
Button(top,text="暂停",command=pause,width=7,bg="deepskyblue").place(x=16,y=260)
Button(top,text="继续播放",command=unpause,width=7,bg="deepskyblue").place(x=96,y=260)
Button(top,text="结束播放",command=stop,width=7,bg="deepskyblue").place(x=176,y=260)

#使用说明
Button(top,text="使用说明",command = create,width=10,bg="deepskyblue").place(x=20,y=385)
#技术支持
Button(top,text="感谢深圳灵声讯科技提供语音相似度打分python SDK，有需要学习资料可以联系QQ群：696554058",command = create2,width=105,bg="Lavender").place(x=20,y=415)
#音量
w1 = Scale(top, from_=0,to=100, orient="horizontal",length=75,variable=v,command=printScale,label="音量")
w1.place(x=200,y=300)

w2 = Scale(top, from_=30,to=100, orient="horizontal",length=100,variable=v1,command=printsrceen,label="透明度")
w2.place(x=20,y=300)

top.mainloop()

