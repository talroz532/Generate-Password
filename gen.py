import random

small = "abcdefghijklmnopqrstuvwxyz"
large = small.upper()
numbers = "0123456789"
special = "~!@#$%^&*()-_+=<>.?"
all_letters = small + large + numbers + special


def generate_password():
    password = ""
    rand_range = random.randint(6, 20)
    for x in range(rand_range):
        password = password + all_letters[random.randint(0, len(all_letters) - 1)]
    return password


def main():
    print("Keep generate press ENTER \n For exit press ANY KEY")
    while True:
        i = input()
        if i:
            break
        print("your password: " + generate_password())


if __name__ == "__main__":
    main()
