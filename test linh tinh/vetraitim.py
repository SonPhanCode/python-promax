import turtle

obj = turtle.Turtle()
obj.shape("turtle")
obj.speed(1)
"""Draw_Heart"""
obj.pensize(5)

def heart():
	for i in range(200):
		obj.right(1)
		obj.forward(1)

obj.color("blue", "pink")
obj.begin_fill()
obj.left(140)
obj.forward(111.65)
heart()

obj.left(120)
heart()
obj.forward(111.65)
obj.begin_fill()
obj.hideturtle()

"""OUTPUT"""
turtle.done()