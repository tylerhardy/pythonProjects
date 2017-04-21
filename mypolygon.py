import turtle
import math

# def square(t, length):
#     t = turtle.Turtle()
#     t.speed('fastest')
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)
#     turtle.mainloop()

# square('bob', 200)

# def polygon(t, length, n):
#     t = turtle.Turtle()
#     t.speed('fastest')
#     angle = 360.0 / n
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)
#     turtle.mainloop()

# def arc(t, r):
#     circumference = 2.0 * math.pi * r
#     n = int(circumference / 3) + 3
#     length = circumference / n
#     polygon(t, length, n)

# def arc(t, r, a):
#     c = 2.0 * math.pi * r
#     n = 50
#     l = c / n
#     polygon(t, l, n, a)

# polygon('bob', 100, 100)

# arc('bob', 100, 360)

def arc(t, radius, angle):
    t = turtle.Turtle()
    t.speed('fastest')
    arc_length = 2.0 * math.pi * radius * angle / 360
    n = int(arc_length /3) + 1
    step_angle = angle / n
    step_length = arc_length / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
    turtle.mainloop()

arc('bob', 100, 360)
