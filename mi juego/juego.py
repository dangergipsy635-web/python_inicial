import tkinter as tk
import random
import math

WIDTH = 800
HEIGHT = 600

root = tk.Tk()
root.title("Shooter Tkinter")

canvas = tk.Canvas(root,width=WIDTH,height=HEIGHT,bg="black")
canvas.pack()

player_x = WIDTH//2
player_y = HEIGHT//2
player_health = 100

player = canvas.create_rectangle(player_x-15,player_y-15,player_x+15,player_y+15,fill="green")

bullets = []
enemies = []
score = 0

score_text = canvas.create_text(70,20,fill="white",text="Puntos: 0",font=("Arial",16))
health_text = canvas.create_text(70,40,fill="white",text="Vida: 100",font=("Arial",16))

def spawn_enemy():
    x = random.randint(50,750)
    y = random.randint(50,550)
    enemy = canvas.create_oval(x-15,y-15,x+15,y+15,fill="red")
    enemies.append(enemy)

for i in range(5):
    spawn_enemy()

def shoot(event):
    bullet = canvas.create_oval(player_x-5,player_y-5,player_x+5,player_y+5,fill="yellow")
    bullets.append([bullet,event.x,event.y])

canvas.bind("<Button-1>",shoot)

keys = set()

def key_press(e):
    keys.add(e.keysym)

def key_release(e):
    keys.discard(e.keysym)

root.bind("<KeyPress>",key_press)
root.bind("<KeyRelease>",key_release)

def move_player():
    global player_x,player_y

    if "w" in keys:
        player_y -= 5
    if "s" in keys:
        player_y += 5
    if "a" in keys:
        player_x -= 5
    if "d" in keys:
        player_x += 5

    canvas.coords(player,player_x-15,player_y-15,player_x+15,player_y+15)

def update():
    global player_health,score

    move_player()

    for bullet in bullets[:]:
        b,tx,ty = bullet
        bx1,by1,bx2,by2 = canvas.coords(b)

        angle = math.atan2(ty-player_y,tx-player_x)

        canvas.move(b,math.cos(angle)*10,math.sin(angle)*10)

        for enemy in enemies[:]:
            ex1,ey1,ex2,ey2 = canvas.coords(enemy)

            if bx2>ex1 and bx1<ex2 and by2>ey1 and by1<ey2:
                canvas.delete(enemy)
                enemies.remove(enemy)
                canvas.delete(b)
                bullets.remove(bullet)

                spawn_enemy()

                score+=1
                canvas.itemconfig(score_text,text=f"Puntos: {score}")

    for enemy in enemies:
        ex1,ey1,ex2,ey2 = canvas.coords(enemy)
        ex=(ex1+ex2)/2
        ey=(ey1+ey2)/2

        angle=math.atan2(player_y-ey,player_x-ex)

        canvas.move(enemy,math.cos(angle)*2,math.sin(angle)*2)

        if abs(player_x-ex)<20 and abs(player_y-ey)<20:
            player_health-=1
            canvas.itemconfig(health_text,text=f"Vida: {player_health}")

    if player_health>0:
        root.after(16,update)
    else:
        canvas.create_text(WIDTH/2,HEIGHT/2,text="GAME OVER",fill="white",font=("Arial",40))

update()
root.mainloop()