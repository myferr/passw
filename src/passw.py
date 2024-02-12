import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "z",
    "a",
    "v",
    "o",
    "m",
    "n",
    "o",
    "m",
    "q",
    "q",
    "x",
    "x",
    "x",
    "p",
    "i",
    "w",
    "w",
    "x",
    "k",
    "l",
    "r",
    "e",
    "t",
    "y",
    "u",
    "i",
    "o",
    "p",
    "a",
    "s",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "z",
    "x",
    "c",
    "v",
    "b",
    "n",
    "m"
]

numbers = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
]

special_characters = [
    "!",
    "?",
    "#",
    "*",
    ".",
    ",",
    "`"
]

def generate_letters():
    amletters = (random.choice(letters))
    return amletters

def generate_numbers():
    amnumbers = (random.choice(numbers) + random.choice(numbers))
    return amnumbers

def generate_special_characters():
    amspecial_characters = (random.choice(special_characters))
    return amspecial_characters

def generate_password(amount, generatedpasswordmsg):
    if generatedpasswordmsg:
        gpm = "PASSWORD: "
    else:
        gpm = ""
    def psw():
        dice = random.randint(1, 10)
        for i in range(dice):
            n = generate_numbers()
            l = generate_letters()
            sc = generate_special_characters()
    
        part1 = (sc+l+n)
        n = generate_numbers()
        l = generate_letters()
        sc = generate_special_characters()
        part2 = (sc+n+l)
        n = generate_numbers()
        l = generate_letters()
        sc = generate_special_characters()
        part3 = (sc+n+l)
    
        print(gpm+part1+part2+part3)
    
    for i in range(int(amount)):
        psw()
