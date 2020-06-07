def firstEquation(u, a, t):
    return int(u) + int(a) * int(t)


def secondEquation(u, a, t):
    return int(u) * int(t) + 1 / 2 * int(a) * int(t) ** 2


def thirdEquation(u, a, s):
    return int(u) ** 2 + 2 * int(a) * int(s)


def main():
    choice = int(input("Enter the equation to be used: "))
    if choice == 1:
        initial = input("Enter the inital velocity")
        acceleration = input("Enter the acceleration: ")
        time = input("enter the time")
        res = firstEquation(initial, acceleration, time)

    if choice == 2:
        initial = input("Enter the inital velocity")
        acceleration = input("Enter the acceleration: ")
        time = input("enter the time")
        res = secondEquation(initial, acceleration, time)

    if choice == 3:
        initial = input("Enter the inital velocity")
        acceleration = input("Enter the acceleration: ")
        displacement = input("Enter the displacement")
        res = thirdEquation(initial, acceleration, displacement)

    print("The answer is " + str(res))

main()
