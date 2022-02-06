from tkinter import *
from tkinter import messagebox
import random

def siddharth():
    pass

def kittu():
    pass

class Game:
    colour={'2':'#D9FFF4','4':'#54CFAA','8':'#00FFB4','16':'#00FE5E','32':'#00C8B9','64':'#6EA8FF','128':'#00ADFF','256':'#008DFF','512':'#A95EF5','1024':'#D95EF5','2048':'F5C05E',}
    font={'2':'#000000','4':'#000000','8':'#000000','16':'#000000','32':'#000000','64':'#000000','128':'#000000','256':'#000000','512':'#000000','1024':'#000000','2048':'#000000',}

    def __init__(s):
        s.n=4
        s.wndw=Tk()
        s.wndw.title('2048')
        s.p_area=Frame(s.wndw,bg= 'azure2')
        s.brd=[]
        s.grd=[[0]*4 for i in range(4)]
        s.compress=False
        s.merge=False
        s.moved=False
        s.score=0
        for i in range(4):
            rows=[]
            for j in range(4):
                l=Label(s.p_area,text='',bg='azure3',
                font=('arial',22,'bold'),width=4,height=2)
                l.grid(row=i,column=j,padx=7,pady=7)

                rows.append(l);
            s.brd.append(rows)
        s.p_area.grid()

    def rev(s):
        for ind in range(4):
            i=0
            j=3
            while(i<j):
                s.grd[ind][i],s.grd[ind][j]=s.grd[ind][j],s.grd[ind][i]
                i+=1
                j-=1

    def trans(s):
        s.grd=[list(trans)for trans in zip(*s.grd)]

    def Merge(s):
        s.compress=False
        temp=[[0] *4 for i in range(4)]
        for i in range(4):
            cnt=0
            for j in range(4):
                if s.grd[i][j]!=0:
                    temp[i][cnt]=s.grd[i][j]
                    if cnt!=j:
                        s.compress=True
                    cnt+=1
        s.grd=temp

    def g_merge(s):
        s.merge=False
        for i in range(4):
            for j in range(4 - 1):
                if s.grd[i][j] == s.grd[i][j + 1] and s.grd[i][j] != 0:
                    s.grd[i][j] *= 2
                    s.grd[i][j + 1] = 0
                    s.score += s.grd[i][j]
                    s.merge = True
                    siddharth()

    def rand(s):
        cells=[]
        for i in range(4):
            for j in range(4):
                if s.grd[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        s.grd[i][j]=2
    
    def check(s):
        for i in range(4):
            for j in range(3):
                if s.grd[i][j] == s.grd[i][j+1]:
                    return True
                    siddharth()
        
        for i in range(3):
            for j in range(4):
                if s.grd[i+1][j] == s.grd[i][j]:
                    return True
        return False

    def color(s):
        for i in range(4):
            for j in range(4):
                if s.grd[i][j]==0:
                    s.brd[i][j].config(text='',bg='azure3')
                else:
                    s.brd[i][j].config(text=str(s.grd[i][j]),
                    bg=s.colour.get(str(s.grd[i][j])),
                    fg=s.font.get(str(s.grd[i][j])))
                    siddharth()

class Play:
    
    def __init__(s,g):
        print("Start Game")
        print("Instructions:")
        print("Input 1 for Left")
        print("Input 2 for Right")
        print("Input 3 for UP")
        print("Input 4 for Down\n")
        s.g=g
        s.end=False
        s.won=False

    def start(s):
        s.g.rand()
        s.g.rand()
        s.g.color()
        s.g.wndw.bind('<Key>', s.check1)
        s.g.wndw.mainloop()
    
    def check1(s,event):
        if s.end or s.won:
            return

        s.g.compress = False
        s.g.merge = False
        s.g.moved = False

        presed_key=event.keysym

        if presed_key=='3':
            s.g.trans()
            s.g.Merge()
            s.g.g_merge()
            s.g.moved = s.g.compress or s.g.merge
            s.g.Merge()
            s.g.trans()
            print("3 Pressed moved Up")
            kittu()

        elif presed_key=='4':
            s.g.trans()
            s.g.rev()
            s.g.Merge()
            s.g.g_merge()
            s.g.moved = s.g.compress or s.g.merge
            s.g.Merge()
            s.g.rev()
            s.g.trans()
            print("4 Pressed moved Down")
            kittu()

        elif presed_key=='1':
            s.g.Merge()
            s.g.g_merge()
            s.g.moved = s.g.compress or s.g.merge
            s.g.Merge()
            print("1 Pressed moved Left")
            siddharth()

        elif presed_key=='2':
            s.g.rev()
            s.g.Merge()
            s.g.g_merge()
            s.g.moved = s.g.compress or s.g.merge
            s.g.Merge()
            s.g.rev()
            print("2 Pressed moved Right")
            siddharth()
        else:
            print("Enter Valid Key : 1, 2, 3, 4")

        s.g.color()
        a=(s.g.score)
        print("Current Score: " + str(a) + "\n")

        f=0
        for i in range(4):
            for j in range(4):
                if(s.g.grd[i][j]==2048):
                    f=1
                    break

        if(f==1):
            s.won=True
            messagebox.showinfo('2048', message='You Won!')
            print("Game Over "" You Loose")
            print("Final Score: " + str(a))
            return

        for i in range(4):
            for j in range(4):
                if s.g.grd[i][j]==0:
                    f=1
                    break

        if not (f or s.g.check()):
            s.end=True
            messagebox.showinfo('2048','Game Over!')
            print("Game Over "" You Loose" )
            print("Final Score: " + str(a))
            
        if s.g.moved:
            s.g.rand()
        
        s.g.color()
    

g =Game()
game2048 = Play(g)
game2048.start()
