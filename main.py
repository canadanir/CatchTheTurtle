import time
import random
import turtle

turtle_instance = turtle.Turtle()
turtle_screen = turtle.Screen()
turtle_screen.screensize(700,700)
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle Game")

turtle.color("dark green")
turtle_instance.color("black")
turtle_instance.write("Hello")

turtle.shape("turtle")
turtle.shapesize(2, 2, 7) #shape size of turtle

turtle_instance.hideturtle()
turtle_instance.penup()
turtle_instance.goto(0, 260)

game_over = False

def new_position():
    global game_over
    if game_over == False:
        turtle.hideturtle()
        turtle.right(random.randint(-360, 360))
        turtle.teleport(x = random.randint(-350,350),y = random.randint(-350,350))
        turtle.showturtle()



game_point = 0

def handle_click(x,  y):
    global game_point
    game_point += 1
    new_position()
    turtle.clear()
    turtle_instance.goto(0, 230)
    turtle_instance.write(f"Puan: {game_point}", align="center", font=("Arial", 24, "bold"))

turtle.onclick(handle_click)

time_left = 30

def countdown():
    global time_left
    global game_point
    global game_over
    turtle_instance.clear()
    if time_left > 0:
        turtle_instance.goto(0, 260)
        turtle_instance.write(f"Zaman: {time_left} saniye", align="center", font=("Arial", 24, "normal"))
        turtle_instance.goto(0, 230)
        turtle_instance.write(f"Puan: {game_point}", align="center", font=("Arial", 24, "bold"))
        time_left -= 1
        turtle_screen.ontimer(countdown, 1000)
        turtle_screen.listen()


    else:
        turtle_instance.goto(0, 230)
        turtle_instance.write(f"Oyun Bitti! Oyun puanınız: {game_point}", align="center", font=("Arial", 24, "bold"))
        turtle.hideturtle()
        turtle_screen.oneclick(None)
        turtle.hideturtle()
        game_over = True


countdown()

time_left2 = 60

def troll_position():
    global time_left2
    global time_left
    if time_left < 0.1:
        turtle.hideturtle()

    elif time_left2 > 0:
        wait_time = random.uniform(0.7, 1.2)
        time_left2 -= wait_time
        turtle_screen.ontimer(troll_position, int(wait_time * 1000))
        new_position()


troll_position()

turtle_screen.mainloop()


