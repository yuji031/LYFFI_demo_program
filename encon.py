import tkinter as tk
from tkinter import Button, font
from tkinter.constants import ANCHOR, RADIOBUTTON, X
from typing import Text


item=['1','2','3','4','5']

job_list=[]

version = tk.Tcl().eval('info patchlevel')

question=["Q1: 自分が行動するときはいつも全体の利益を考える", "Q2:読み始めた本はあまり面白くなくても最後まで読む", 
"Q3:思いつきの行動はしない", "Q4物を買うときは自分に本当に必要なものかよく考える", "Q5クラスや学校が変わってもすぐにとけ込める"]


num = -1
co=0
job_count_1=0
job_count_2=0
job_count_3=0
job_count_4=0
job_count_5=0

list_1=[]
list_2=[]
list_3=[]
list_4=[]
list_5=[]
x=0
y=0
z=0
s=0

def return_back():
    list_1.clear()
    list_2.clear()
    list_3.clear()
    list_4.clear()
    list_5.clear()
    
    job_list.clear()

    global job_count_1
    job_count_1=0

    global job_count_2
    job_count_2=0

    global job_count_3
    job_count_3=0

    global job_count_4
    job_count_4=0

    global job_count_5
    job_count_5=0


    global co
    co = 0

    global num
    num = -1

    global window
    window.destroy()
    window = tk.Tk()

    window.geometry("1000x800")
    window.title("LYFFI  " + version)
    window.attributes('-fullscreen', True)
    window.configure(bg="white")

    canvas = tk.Canvas(window, bg="white", height=10000, width=10000)

    canvas.place(x=0, y=0)

    img_1 = tk.PhotoImage(file="LYFFI_home.png")

    canvas.create_image(350, 50, image=img_1, anchor=tk.NW)


    btn_2nd = tk.Button(window, text='START',font=('',20), command=btn_click_1, height=2, width=30)
    
    btn_2nd.place(x = 550, y = 600)
    

    window.mainloop()

def btn_event(event):
    if co==1:
        list_1.append(str(event.widget["text"]))
    elif co==2:
        list_2.append(str(event.widget["text"]))
    elif co==3:
        list_3.append(str(event.widget["text"]))
    elif co==4:
        list_4.append(str(event.widget["text"]))
    elif co==5:
        list_5.append(str(event.widget["text"]))

def job_btn_click_1(self):
    global job_count_1
    job_count_1=job_count_1+1
    job_list.append("科学者")

def job_btn_click_2(self):
    global job_count_2
    job_count_2=job_count_2+1
    job_list.append("俳優・女優")

def job_btn_click_3(self):
    global job_count_3
    job_count_3=job_count_3+1
    job_list.append("経営者")

def job_btn_click_4(self):
    global job_count_4
    job_count_4=job_count_4+1
    job_list.append("youtuber")

def job_btn_click_5(self):
    global job_count_5
    job_count_5=job_count_5+1
    job_list.append("教員")

def btn_click_1():
    global window
    window.destroy()
    
    window=tk.Tk()
    window.geometry("1000x800")
    window.title("LYFFI  " + version)
    window.configure(bg="white")
    window.attributes('-fullscreen', True)

    btn_job_1 = tk.Button(window, text="科学者", font=('',20), command=btn_click_2, height=1, width=20)
    btn_job_1.place(x=600,y=200)
    btn_job_2 = tk.Button(window, text="俳優・女優", font=('',20), command=btn_click_2, height=1, width=20)
    btn_job_2.place(x=600,y=300)
    btn_job_3 = tk.Button(window, text="経営者", font=('',20), command=btn_click_2, height=1, width=20)
    btn_job_3.place(x=600,y=400)
    btn_job_4 = tk.Button(window, text="youtuber", font=('',20), command=btn_click_2, height=1, width=20)
    btn_job_4.place(x=600,y=500)
    btn_job_5 = tk.Button(window, text="教員", font=('',20), command=btn_click_2, height=1, width=20)
    btn_job_5.place(x=600,y=600)


    btn_job_1.bind("<ButtonPress>" ,job_btn_click_1)
    btn_job_2.bind("<ButtonPress>" ,job_btn_click_2)
    btn_job_3.bind("<ButtonPress>" ,job_btn_click_3)
    btn_job_4.bind("<ButtonPress>" ,job_btn_click_4)
    btn_job_5.bind("<ButtonPress>" ,job_btn_click_5)

    window.mainloop
def btn_click_2():
    global co
    if co<5:
        global window
        window.destroy()
    
        global num
        num = num + 1

        co = co + 1

        window = tk.Tk()
        window.geometry("1000x800")
        window.title("LYFFI  " + version)
        window.configure(bg="white")
        window.attributes('-fullscreen', True)

        global img_1
        img_1 = tk.PhotoImage(file="LYFFI_image.png")

        canvas = tk.Canvas(window, bg="white", height=10000, width=10000)
        canvas.place(x=0, y=-50)
        canvas.create_image(250, 50, image=img_1, anchor=tk.NW)


        Label_1 = tk.Label(window,text=str(question[num]),font=('',30),foreground='light blue', background='white')
        Label_1.place(x=343,y=75)
        

        
        label_q1 = tk.Label(window,text='そうではない',font=('',20))
        label_q1.place(x=400,y=200)

        label_q2 = tk.Label(window,text='たまにそう',font=('',20))
        label_q2.place(x=400,y=300)

        label_q3 = tk.Label(window,text='常にそう',font=('',20))
        label_q3.place(x=400,y=400)



        btn_1 = tk.Button(window, text=1, font=('',20), command=btn_click_2, height=1, width=2)
        btn_1.place(x=343,y=200)
        
        btn_2 = tk.Button(window, text=2, font=('',20), command=btn_click_2, height=1, width=2)
        btn_2.place(x=343,y=300)

        btn_3 = tk.Button(window, text=3, font=('',20), command=btn_click_2, height=1, width=2)
        btn_3.place(x=343,y=400)
        
        
        btn_1.bind("<ButtonPress>", btn_event)
        btn_2.bind("<ButtonPress>", btn_event)
        btn_3.bind("<ButtonPress>", btn_event)
    
        window.mainloop
    else:
        window.destroy()

        window = tk.Tk()
        window.geometry("1000x800")
        window.title("LYFFI  " + version)
        window.configure(bg="white")
        window.attributes('-fullscreen', True)

        
        label_status = tk.Label(window, text='STATUS', font=('',30))
        label_status.place(x=90,y=40)
        
        label_status_1 = tk.Label(window, text=('客観性  '+str(list_1)), font=('',20))
        label_status_1.place(x=90,y=100)

        label_status_2 = tk.Label(window, text=('責任感  '+str(list_2)), font=('',20))
        label_status_2.place(x=90,y=150)

        label_status_3 = tk.Label(window, text=('計画性  '+str(list_3)), font=('',20))
        label_status_3.place(x=90,y=200)

        label_status_4 = tk.Label(window, text=('先見性  '+str(list_4)), font=('',20))
        label_status_4.place(x=90,y=250)

        label_status_5 = tk.Label(window, text=('コミュニケーション能力  '+str(list_5)), font=('',20))
        label_status_5.place(x=90,y=300)
        
        if job_count_1==1:
            s = list_2[0]
            x = list_3[0]
            y = list_4[0]
            z=int(x)+int(y)
            if z==6 and int(s)==3:
                label_runk=tk.Label(window, text='S',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==6:
                label_runk=tk.Label(window, text='A',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==5:
                label_runk=tk.Label(window, text='B',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==4:
                label_runk=tk.Label(window, text='C',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==3:
                label_runk=tk.Label(window, text='D',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==2:
                label_runk=tk.Label(window, text='E',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
        
        if job_count_2==1:
            s = list_2[0]
            x = list_3[0]
            y = list_4[0]
            z=int(x)+int(y)
            if z==6 and int(s)==3:
                label_runk=tk.Label(window, text='S',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=700,y=430)
            elif z==6:
                label_runk=tk.Label(window, text='A',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=700,y=430)
            elif z==5:
                label_runk=tk.Label(window, text='B',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=700,y=430)
            elif z==4:
                label_runk=tk.Label(window, text='C',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=700,y=430)
            elif z==3:
                label_runk=tk.Label(window, text='D',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=700,y=430)
            elif z==2:
                label_runk=tk.Label(window, text='E',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=700,y=430)
        if job_count_3==1:
            s = list_2[0]
            x = list_3[0]
            y = list_4[0]
            z=int(x)+int(y)
            if z==6 and int(s)==3:
                label_runk=tk.Label(window, text='S',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==6:
                label_runk=tk.Label(window, text='A',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==5:
                label_runk=tk.Label(window, text='B',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==4:
                label_runk=tk.Label(window, text='C',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==3:
                label_runk=tk.Label(window, text='D',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==2:
                label_runk=tk.Label(window, text='E',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            
        if job_count_4==1:
            s = list_2[0]
            x = list_3[0]
            y = list_5[0]
            z=int(x)+int(y)
            if z==6 and int(s)==3:
                label_runk=tk.Label(window, text='S',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==6:
                label_runk=tk.Label(window, text='A',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==5:
                label_runk=tk.Label(window, text='B',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==4:
                label_runk=tk.Label(window, text='C',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==3:
                label_runk=tk.Label(window, text='D',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==2:
                label_runk=tk.Label(window, text='E',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)

        if job_count_5==1:
            s = list_3[0]
            x = list_2[0]
            y = list_5[0]
            z=int(x)+int(y)
            if z==6 and int(s)==3:
                label_runk=tk.Label(window, text='S',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==6:
                label_runk=tk.Label(window, text='A',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==5:
                label_runk=tk.Label(window, text='B',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==4:
                label_runk=tk.Label(window, text='C',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==3:
                label_runk=tk.Label(window, text='D',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
            elif z==2:
                label_runk=tk.Label(window, text='E',font=('', 100))
                label_runk.configure(bg='white')
                label_runk.place(x=600,y=430)
        
        

        label_result = tk.Label(window, text="あなたの"+str(job_list)+"の適性は", font=('',30))
        label_result.configure(bg='white')
        label_result.place(x=100, y=500)

        s=0
        x=0
        y=0
        z=0

        print(job_list)

        return_btn = tk.Button(window, text = 'Restart', font=('',20), command=return_back, height=2, width=30)
        return_btn.place(x = 550, y = 600)


        window.mainloop()
    


window = tk.Tk()
window.geometry("1000x800")
window.title("LYFFI  " + version)
window.attributes('-fullscreen', True)
window.configure(bg="white")

canvas = tk.Canvas(window, bg="black", height=10000, width=10000)
canvas.place(x=0, y=0)

img_1 = tk.PhotoImage(file="LYFFI_home.png")
canvas.create_image(350, 50, image=img_1, anchor=tk.NW)
canvas.configure(bg='white')

btn = tk.Button(window, text='START',font=('',20), command=btn_click_1, height=2, width=30)
btn.place(x = 550, y = 600)


bg_window = tk.Tk()
bg_window.attributes('-fullscreen', True)
bg_window.configure(bg="white")
bg_window.mainloop()

window.mainloop()
