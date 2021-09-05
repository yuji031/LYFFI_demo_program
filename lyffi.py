import tkinter as tk
from tkinter import font
from tkinter.constants import ANCHOR, RADIOBUTTON, X
from typing import Text


item=['1','2','3','4','5']

version = tk.Tcl().eval('info patchlevel')

question=["Q1: 自分が行動するときはいつも全体の利益を考える", "Q2:読み始めた本はあまり面白くなくても最後まで読む", 
"Q3:思いつきの行動はしない", "Q4物を買うときは自分に本当に必要なものかよく考える", "Q5クラスや学校が変わってもすぐにとけ込める"]

job_list= []
num = -1
co=0
list_1=[]
list_2=[]
list_3=[]
list_4=[]
list_5=[]

job_runk=[]

job_count1 = 0
job_count2 = 0
job_count3 = 0
job_count4 = 0
job_count5 = 0

window = tk.Tk()
window.geometry("1000x800")
window.title("LYFFI  " + version)
# window.attributes('-fullscreen', True)
window.configure(bg="white")

canvas = tk.Canvas(window, bg="black", height=1000, width=800)
canvas.place(x=100, y=0)



def btn_click_job1(self):
    global job_count1
    job_count1 = job_count1+1
    job_list.append("科学者")

def btn_click_job2(self):
    global job_count2
    job_count2 = job_count2+1
    job_list.append("演者")

def btn_click_job3(self):
    global job_count3
    job_count3 = job_count3+1
    job_list.append("教師")

def btn_click_job4(self):
    global job_count4
    job_count4 = job_count4+1
    job_list.append("youtuber")

def btn_click_job5(self):
    global job_count5
    job_count5 = job_count5+1
    job_list.append("経営者")
    


def btn_click_1():
    global window

    window.destroy()
    window = tk.Tk()
    window.geometry("1000x800")
    window.title("LYFFI  " + version)
    # window.attributes('-fullscreen', True)
    window.configure(bg="white")

    btn_job1 = tk.Button(window, text="科学者", font=('',20), command=btn_click_2, height=1, width=20)
    btn_job1.place(x=100,y=200)

    btn_job2 = tk.Button(window, text="演者", font=('',20), command=btn_click_2, height=1, width=20)
    btn_job2.place(x=100,y=300)

    btn_job3 = tk.Button(window, text="教師", font=('',20), command=btn_click_2, height=1, width=20)
    btn_job3.place(x=100,y=400)

    btn_job4 = tk.Button(window, text="youtuber", font=('',20), command=btn_click_2, height=1, width=20)
    btn_job4.place(x=100,y=500)

    btn_job5 = tk.Button(window, text="経営者", font=('',20), command=btn_click_2, height=1, width=20)
    btn_job5.place(x=100,y=600)

    btn_job1.bind("<ButtonPress>", btn_click_job1)
    btn_job2.bind("<ButtonPress>", btn_click_job2)
    btn_job3.bind("<ButtonPress>", btn_click_job3)
    btn_job4.bind("<ButtonPress>", btn_click_job4)
    btn_job5.bind("<ButtonPress>", btn_click_job5)




def return_back():

    global job_count1
    global job_count2
    global job_count3
    global job_count4
    global job_count5

    job_count1 = 0
    job_count2 = 0
    job_count3 = 0
    job_count4 = 0
    job_count5 = 0
    
    global job_list
    job_list.clear()

    global job_runk
    job_runk.clear()

    list_1.clear()
    list_2.clear()
    list_3.clear()
    list_4.clear()
    list_5.clear()

    global co
    co = 0

    global num
    num = -1

    global window
    window.destroy()
    window = tk.Tk()

    window.geometry("1000x800")
    window.title("LYFFI  " + version)
    # window.attributes('-fullscreen', True)
    window.configure(bg="white")

    canvas = tk.Canvas(window, bg="white", height=1000, width=800)

    canvas.place(x=100, y=0)

    img_1 = tk.PhotoImage(file="LYFFI_home.png")

    canvas.create_image(250, 50, image=img_1, anchor=tk.NW)


    btn_2nd = tk.Button(window, text='START',font=('',20), command=btn_click_1, height=2, width=30)
    
    btn_2nd.place(x = 300, y = 600)
    

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
        # window.attributes('-fullscreen', True)

        global img_1
        img_1 = tk.PhotoImage(file="LYFFI_image.png")

        canvas = tk.Canvas(window, bg="white", height=10000, width=10000)
        canvas.place(x=-100, y=-50)
        canvas.create_image(-50, 50, image=img_1, anchor=tk.NW)


        Label_1 = tk.Label(window,text=str(question[num]),font=('',30),foreground='light blue', background='white')
        Label_1.place(x=50,y=75)
        

        
        label_q1 = tk.Label(window,text='そうではない',font=('',20))
        label_q1.place(x=150,y=200)

        label_q2 = tk.Label(window,text='たまにそう',font=('',20))
        label_q2.place(x=150,y=300)

        label_q3 = tk.Label(window,text='常にそう',font=('',20))
        label_q3.place(x=150,y=400)



        btn_1 = tk.Button(window, text=1, font=('',20), command=btn_click_2, height=1, width=2)
        btn_1.place(x=100,y=200)
        
        btn_2 = tk.Button(window, text=2, font=('',20), command=btn_click_2, height=1, width=2)
        btn_2.place(x=100,y=300)

        btn_3 = tk.Button(window, text=3, font=('',20), command=btn_click_2, height=1, width=2)
        btn_3.place(x=100,y=400)
        
        
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
        # window.attributes('-fullscreen', True)

        
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
        
        print(job_list)

        if job_count1==1:
            s=int(list_2[0])
            x=int(list_3[0])
            y=int(list_4[0])
            z=x+y

            if z==6 and s==3:
                job_runk.append("S")
            elif z==6:
                job_runk.append("A")
            elif z==5:
                job_runk.append("B")
            elif z==4:
                job_runk.append("C")
            elif z==3:
                job_runk.append("D")
            elif z==2:
                job_runk.append("E")

            x=0
            y=0
            z=0

        if job_count2==1:
            s=int(list_2[0])
            x=int(list_1[0])
            y=int(list_5[0])
            z=x+y

            if z==6 and s==3:
                job_runk.append("S")
            elif z==6:
                job_runk.append("A")
            elif z==5:
                job_runk.append("B")
            elif z==4:
                job_runk.append("C")
            elif z==3:
                job_runk.append("D")
            elif z==2:
                job_runk.append("E")

            x=0
            y=0
            z=0

        if job_count3==1:
            s=int(list_3[0])
            x=int(list_2[0])
            y=int(list_5[0])
            z=x+y

            if z==6 and s==3:
                job_runk.append("S")
            elif z==6:
                job_runk.append("A")
            elif z==5:
                job_runk.append("B")
            elif z==4:
                job_runk.append("C")
            elif z==3:
                job_runk.append("D")
            elif z==2:
                job_runk.append("E")

            x=0
            y=0
            z=0

        if job_count4==1:
            s=int(list_2[0])
            x=int(list_5[0])
            y=int(list_4[0])
            z=x+y

            if z==6 and s==3:
                job_runk.append("S")
            elif z==6:
                job_runk.append("A")
            elif z==5:
                job_runk.append("B")
            elif z==4:
                job_runk.append("C")
            elif z==3:
                job_runk.append("D")
            elif z==2:
                job_runk.append("E")

            x=0
            y=0
            z=0

        if job_count5==1:
            s=int(list_1[0])
            x=int(list_2[0])
            y=int(list_4[0])
            z=x+y

            if z==6 and s==3:
                job_runk.append("S")
            elif z==6:
                job_runk.append("A")
            elif z==5:
                job_runk.append("B")
            elif z==4:
                job_runk.append("C")
            elif z==3:
                job_runk.append("D")
            elif z==2:
                job_runk.append("E")

            x=0
            y=0
            z=0


        label_runk = tk.Label(window, text=(job_runk),font=('',100))
        label_runk.configure(bg="white")
        label_runk.place(x=600,y=450)

        label_result = tk.Label(window, text="あなたの"+ str(job_list)+"の適正は", font=('',30))
        label_result.configure(bg="white")
        label_result.place(x=100, y=500)

        return_btn = tk.Button(window, text = 'Restart', font=('',20), command=return_back, height=2, width=30)
        return_btn.place(x = 300, y = 600)

        window.mainloop()
    
img_1 = tk.PhotoImage(file="LYFFI_home.png")
canvas.create_image(0, 50, image=img_1, anchor=tk.NW)
canvas.configure(bg='white')

btn = tk.Button(window, text='START',font=('',20), command=btn_click_1, height=2, width=30)
btn.place(x = 300, y = 600)




bg_window = tk.Tk()
# bg_window.attributes('-fullscreen', True)
bg_window.configure(bg="white")
bg_window.mainloop()

window.mainloop()
