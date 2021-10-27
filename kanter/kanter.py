import turtle

screen = turtle.Screen()


def get_screen_size():
    screen_width = turtle.getcanvas().winfo_screenwidth()
    screen_height = turtle.getcanvas().winfo_screenheight()
    return screen_width, screen_height


def kanter(l, n, x=0, y=0):
    dist = l / 3
    if n == 0:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(l)
        return

    elif n >= 1:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(l)
        kanter(dist, n - 1, x, y - 20)
        kanter(dist, n - 1, x + dist * 2, y - 20)


if __name__ == "__main__":
    screen_width, screen_height = get_screen_size()
    # screen_width -=1000

    depth = int(turtle.textinput("Глубина рекурсии", "Введите глубину рекурсии. Максимум 10"))

    if depth > 10:
        print("Глубина рекурсии больше 10")
        exit(1)

    screen.setup(screen_width, screen_height)

    size = screen_width - 110
    turtle.speed('fastest')
    # turtle.tracer(0, 0)

    turtle.penup()
    # turtle.goto(-screen_width / 2, -200)
    turtle.pendown()

    kanter(size, depth, x=-screen_width / 2 + 50)
    # turtle.update()
    turtle.exitonclick()
