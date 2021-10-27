import turtle

screen = turtle.Screen()


def get_screen_size():
    screen_width = turtle.getcanvas().winfo_screenwidth()
    screen_height = turtle.getcanvas().winfo_screenheight()
    return screen_width, screen_height


def curve_minkowski(size: float, n: int):
    if n == 0:
        turtle.forward(size)
    else:
        curve_minkowski(size / 4, n - 1)
        turtle.left(90)
        curve_minkowski(size / 4, n - 1)
        turtle.right(90)
        curve_minkowski(size / 4, n - 1)
        turtle.right(90)
        curve_minkowski(size / 4, n - 1)
        curve_minkowski(size / 4, n - 1)
        turtle.left(90)
        curve_minkowski(size / 4, n - 1)
        turtle.left(90)
        curve_minkowski(size / 4, n - 1)
        turtle.right(90)
        curve_minkowski(size / 4, n - 1)


if __name__ == "__main__":

    screen_width, screen_height = get_screen_size()

    depth = int(turtle.textinput("Глубина рекурсии", "Введите глубину рекурсии. Максимум 6"))

    if depth > 6:
        print("Глубина рекурсии больше 6")
        exit(1)

    screen.setup(screen_width, screen_height)

    size = screen_width / 2
    turtle.speed('fastest')
    turtle.tracer(0, 0)

    turtle.penup()
    turtle.goto(-screen_width / 2, 0)
    turtle.pendown()

    curve_minkowski(size, depth)
    turtle.update()
    turtle.exitonclick()
