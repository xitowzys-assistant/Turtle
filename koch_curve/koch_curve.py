import turtle

screen = turtle.Screen()


def get_screen_size():
    screen_width = turtle.getcanvas().winfo_screenwidth()
    screen_height = turtle.getcanvas().winfo_screenheight()
    return screen_width, screen_height


def koch_curve(size, n):
    if n == 0:
        # Проползти size пикселей вперед
        turtle.forward(size)
    else:
        koch_curve(size / 3, n - 1)
        # Поворот влево на 60 градусов
        turtle.left(60)
        koch_curve(size / 3, n - 1)
        # Поворот вправо на 120 градусов
        turtle.right(120)
        koch_curve(size / 3, n - 1)
        # Поворот влево на 60 градусов
        turtle.left(60)
        koch_curve(size / 3, n - 1)


if __name__ == "__main__":

    screen_width, screen_height = get_screen_size()

    depth = int(turtle.textinput("Глубина рекурсии", "Введите глубину рекурсии. Максимум 10"))

    if depth > 10:
        print("Глубина рекурсии больше 10")
        exit(1)

    screen.setup(screen_width, screen_height)

    size = screen_width
    turtle.speed('fastest')
    turtle.tracer(0, 0)

    turtle.penup()
    turtle.goto(-screen_width / 2, -200)
    turtle.pendown()

    koch_curve(size, depth)
    turtle.update()
    turtle.exitonclick()
