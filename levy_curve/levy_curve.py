import turtle

screen = turtle.Screen()


def get_screen_size():
    screen_width = turtle.getcanvas().winfo_screenwidth()
    screen_height = turtle.getcanvas().winfo_screenheight()
    return screen_width, screen_height


def levi(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        turtle.left(45)
        levi(order - 1, size / 4)
        turtle.right(90)
        levi(order - 1, size / 4)
        turtle.left(45)


def levi_full(depth, coefficient_size, coefficient_screen_width, height):
    size = screen_width * depth + coefficient_size

    turtle.penup()
    turtle.goto(-screen_width / coefficient_screen_width, height)
    turtle.pendown()

    levi(depth, depth * size)


if __name__ == "__main__":
    screen_width, screen_height = get_screen_size()
    screen.setup(screen_width, screen_height)

    depth = int(turtle.textinput("Глубина рекурсии", "Введите глубину рекурсии. Максимум 18"))

    if depth > 18:
        print("Глубина рекурсии больше 18")
        exit(1)

    dicts = {
        1: [depth, 2e3, 3, -250],
        2: [depth, 5e2, 4, -250],
        3: [depth, 5e2, 5, -250],
        4: [depth, 4e3, 5, -200],
        5: [depth, 1e4, 7, -150],
        6: [depth, 4e4, 6, -200],
        7: [depth, 1e5, 7, -200],
        8: [depth, 3e5, 6, -200],
        9: [depth, 8e5, 6, -200],
        10: [depth, 2e6, 6, -200],
        11: [depth, 5e6, 6, -200],
        12: [depth, 14e6, 6, -250],
        13: [depth, 4e7, 5, -250],
        14: [depth, 1e8, 6, -250],
        15: [depth, 25e7, 6, -250],
        16: [depth, 7e8, 6, -250],
        17: [depth, 18e8, 6, -250],
        18: [depth, 5e9, 6, -250]
    }

    turtle.tracer(0, 0)

    levi_full(depth=dicts[depth][0],
              coefficient_size=dicts[depth][1],
              coefficient_screen_width=dicts[depth][2],
              height=dicts[depth][3])

    turtle.update()
    turtle.exitonclick()
