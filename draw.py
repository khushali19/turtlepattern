import turtle

dr = turtle.Turtle()

dr.penup()
dr.goto((-220, 220))
dr.pendown()

dr.speed(19)

dr.getscreen().bgcolor("cyan")

side = 500


for i in range(121):
   dr.forward(side)
   dr.right(90) 
   side = side - 4
    


turtle.done()