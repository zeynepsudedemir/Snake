import turtle
import time
import random


hız=0.20
pencere=turtle.Screen()
pencere.title("Pink Panter")
pencere.bgcolor('black')
pencere.setup(width=700,height=600)
pencere.tracer(0)

x=random.randint(-250,250)
y=random.randint(-250,250)

bonus=turtle.Turtle()
bonus.speed(0)
bonus.shape("square")
bonus.color("yellow")
bonus.shapesize(0.5)
bonus.penup()
bonus.goto(x,y)

kafa=turtle.Turtle()
kafa.speed(0)
kafa.shape('circle')
kafa.color("pink")
kafa.penup()
kafa.goto(0,70)
kafa.direction='stop'



yemek=turtle.Turtle()
yemek.speed(0)
yemek.shape('circle')
yemek.color('red')
yemek.shapesize(0.50,0.50)
yemek.penup()
yemek.goto(x,y)

kuyruklar=[]
puan=0
can=1
maksimum=0

yaz3=turtle.Turtle()
yaz3.speed(0)
yaz3.shape('square')
yaz3.color('red')
yaz3.penup()
yaz3.goto(0,0)
yaz3.hideturtle()

yaz2=turtle.Turtle()
yaz2.speed(0)
yaz2.shape('square')
yaz2.color('yellow')
yaz2.penup()
yaz2.goto(250,250)
yaz2.hideturtle()
yaz2.write("Can:{}".format(can),align='center',font=('Rophylar',12,'normal'))


yaz=turtle.Turtle()
yaz.speed(0)
yaz.shape('square')
yaz.color('white')
yaz.penup()
yaz.goto(0,250)
yaz.hideturtle()
yaz.write("Puan:{}".format(puan),align='center',font=('Rophylar',24,'normal'))


maks=turtle.Turtle()
maks.speed(0)
maks.shape("square")
maks.color("purple")
maks.penup()
maks.goto(-250,250)
maks.hideturtle()
maks.write("Maks Puan:{}".format(maksimum),align='center',font=('Rophylar',14,'normal'))

def move():
        if kafa.direction=='up':
            y=kafa.ycor()
            kafa.sety(y + 20)
        if kafa.direction == 'down':
            y = kafa.ycor()
            kafa.sety(y - 20)
        if kafa.direction == 'right':
            x = kafa.xcor()
            kafa.setx(x + 20)
        if kafa.direction == 'left':
            x = kafa.xcor()
            kafa.setx(x - 20)



def goup():
    if kafa.direction!='down':
        kafa.direction='up'
def godown():
    if kafa.direction!='up':
        kafa.direction='down'
def goright():
    if kafa.direction!='left':
        kafa.direction='right'
def goleft():
    if kafa.direction!='right':
        kafa.direction='left'


pencere.listen()
pencere.onkey(goup,'Up')
pencere.onkey(godown,'Down')
pencere.onkey(goright,'Right')
pencere.onkey(goleft,'Left')



while True:
    pencere.update()
    
    if kafa.xcor()>350 or kafa.xcor()<-350 or  kafa.ycor()>300 or kafa.ycor()<-300:
        
        yaz2.clear()
        yaz2.write("Can:{}".format(can),align='center',font=('Rophylar',12,'normal'))
        time.sleep(1)
        if can <= 1:
            
            time.sleep(1)
            kafa.goto(0,0)
            kafa.color("pink")
            kafa.direction='stop'

            for kuyruk in kuyruklar:
                kuyruk.goto(1000,1000)
            kuyruklar=[]
            maksimum=puan
            puan=0
            
            yaz2.clear()
            yaz2.write("Can:{}".format(can),align='center',font=('Rophylar',12,'normal'))
            yaz3.clear()
            yaz3.write("GAME OVER",align='center',font=('Rophylar',30,'normal'))
            maks.clear()
            maks.write("Maks Puan:{}".format(maksimum),align='center',font=('Rophylar',24,'normal'))
            
            yaz.clear()
            turtle.done()
            exitonclick()
        
        elif can == 2:
            
            time.sleep(1)
            kafa.goto(0,0)
            kafa.color("pink")
            kafa.direction = 'stop'
            if puan >= 20:
                puan -= 20

            yaz2.clear()
            yaz2.write("Can:{}".format(can),align='center',font=('Rophylar',12,'normal'))
            yaz.clear()
            yaz.write("Puan:{}".format(puan), align='center', font=('Rophylar', 24, 'normal'))

        else:
            
            if can < 0:
                can = 0
            else:
                can -= 1

            time.sleep(1)
            kafa.goto(0,0)
            kafa.color("pink")
            kafa.direction='stop'
            if puan>=20:
                puan-=20
            else:
                puan=0
                
            yaz2.clear()
            yaz2.write("Can:{}".format(can),align='center',font=('Rophylar',12,'normal'))
            yaz.clear()
            yaz.write("Puan:{}".format(puan), align='center', font=('Rophylar', 24, 'normal'))
            
        

        hız=0.20

    if kafa.distance(bonus)<30:
        x=random.randint(-500,500)
        y=random.randint(-500,500)
        bonus.goto(x,y)
        can+=1
        yaz2.clear()
        yaz2.write("Can:{}".format(can),align='center',font=('Rophylar',12,'normal'))


    if kafa.distance(yemek) < 30:
        x=random.randint(-250,250)
        y=random.randint(-250,250)
        yemek.goto(x,y)
        x=random.randint(-500,500)
        y=random.randint(-500,500)
        bonus.goto(x,y)
        

        puan=puan+10
        yaz.clear()
        yaz.write("Puan:{}".format(puan),align='center',font=('Rophylar',24,'normal'))




        hız-=0.005
        yeniKuyruk=turtle.Turtle()
        yeniKuyruk.speed(0)
        yeniKuyruk.shape('circle')
        yeniKuyruk.color('white')
        yeniKuyruk.penup()
        kuyruklar.append(yeniKuyruk)


    for i in range(len(kuyruklar)-1,0,-1):
        x=kuyruklar[i-1].xcor()
        y=kuyruklar[i-1].ycor()
        kuyruklar[i].goto(x,y)

    if len(kuyruklar)>0:
        x=kafa.xcor()
        y=kafa.ycor()
        kuyruklar[0].goto(x,y)


    move()

    for i in kuyruklar:
        if i.distance(kafa)<20:
            
            
            yaz2.clear()
            yaz2.write("Can:{}".format(can),align='center',font=('Rophylar',12,'normal'))
            if can <= 0:
                time.sleep(1)
                kafa.goto(0,0)
                kafa.color("pink")
                kafa.direction='stop'

                for kuyruk in kuyruklar:
                    kuyruk.goto(1000,1000)
                kuyruklar=[]
                puan=0
                can=0
                yaz3.clear()
                yaz3.write("GAME OVER",align='center',font=('Rophylar',20,'normal'))
                maks.clear()
                maks.write("Maks Puan:{}".format(maksimum),align='center',font=('Rophylar',24,'normal'))
                yaz2.clear()
                yaz.clear()
                turtle.done()
                exitonclick()
            
           
            
            else:
                can-=1
                time.sleep(1)
                kafa.goto(0,0)
                kafa.color("pink")
                kafa.direction='stop'
                if puan>=20:
                    puan-=20
                
                yaz2.clear()
                yaz2.write("Can:{}".format(can),align='center',font=('Rophylar',12,'normal'))
                yaz.clear()
                yaz.write("Puan:{}".format(puan), align='center', font=('Rophylar', 24, 'normal'))
        

            time.sleep(1)
            kafa.goto(0, 0)
            kafa.color("pink")
            kafa.direction = 'stop'
            for kuyruk in kuyruklar:
                kuyruk.goto(1000, 1000)
            kuyruklar = []
            

            hız = 0.20
    time.sleep(hız)