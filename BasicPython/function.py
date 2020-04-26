def hello(name):
    print(f"hello {name}")


hello("kim")


def area(width, heigth=10):
    total = width*heigth
    return total


print(area(5, 2))


def show_info(name="", salary=0.00, lang="not"):
    print(name)
    print(salary)
