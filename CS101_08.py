#### BT1
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


#### BT2
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hi, I'm " + self.name +
              ". I'm " + str(self.age) + " years old.")

# command to test
trau = Person("Trau", 11)
trau.introduce()


#### BT3
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hi, I'm " + self.name +
              ". I'm " + str(self.age) + " years old.")

    def increase_age(self):
        self.age += 1
        print("It's my birthday! I'm " + str(self.age) +
              " years old now.")

# command to test
trau = Person("Trau", 11)
trau.increase_age()


#### BT4
def compare_age(person1, person2):
    if person1.age > person2.age:
        print(person1.name + " is older than " + person2.name)
    elif person1.age == person2.age:
        print(person1.name + " and " +
              person2.name + " are of the same age")
    else:
        print(person2.name + " is older than " + person1.name)

# commands to test
trau = Person("Trau", 11)
william = Person("William", 13)
compare_age(trau, william)

trau = Person("Trau", 11)
william = Person("William", 11)
compare_age(trau, william)


#### BT5
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hi, I'm " + self.name +
              ". I'm " + str(self.age) + " years old.")

    def increase_age(self):
        self.age += 1
        print("It's my birthday! I'm " + str(self.age) +
              " years old now.")

    def greet(self, person):
        print("Hi, " + person.name + "! I'm " +
              self.name + ". Nice to meet you!")

# commands to test
trau = Person("Trau", 11)
william = Person("William", 13)
trau.greet(william)
william.greet(trau)


#### BTCB
class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def move(self, direction, step):
        if direction == "left":
            self.x -= step
        if direction == "right":
            self.x += step
        if direction == "up":
            self.y -= step
        if direction == "down":
            self.y += step

# commands to test
players = [
    Player('Elon Musk', 94, 28),
    Player('Issac', 39, 19),
    Player('Steve', 74, 24)
]
actions = [
    [0, 'up', 6],
    [0, 'right', 10],
    [0, 'down', 5],
    [2, 'right', 5],
    [1, 'up', 7],
    [1, 'left', 5]
]
for action in actions:
    index = action[0]
    players[index].move(action[1], action[2])
    print(players[index].x, players[index].y)


#### BTNC
class Player:
    def __init__(self, name, x, y, role):
        self.name = name
        self.x = x
        self.y = y
        self.role = role

    def move(self, direction, step):
        if direction == "left":
            self.x -= step
        if direction == "right":
            self.x += step
        if direction == "up":
            self.y -= step
        if direction == "down":
            self.y += step

def find_remaining(players):
    # loc ra catchers va runners
    catchers = []
    runners = []
    for player in players:
        if player.role == "catcher":
            catchers.append(player)
        if player.role == "runner":
            runners.append(player)
    # loai cac runners bi bat
    for runner in runners:
        for catcher in catchers:
            if (runner.x == catcher.x) and (runner.y == catcher.y):
                players.remove(runner)
    return players

# commands to test
players = [
    Player('William', 83, 73, 'catcher'),
    Player('Hung', 55, 49, 'runner'),
    Player('Ken', 76, 35, 'runner'),
    Player('Trau', 47, 94, 'runner'),
    Player('Louis', 97, 13, 'runner')
]
actions = [
    [3, 'right', 2],
    [0, 'left', 34],
    [0, 'down', 21]
]
for action in actions:
    index = action[0]
    players[index].move(action[1], action[2])

players = find_remaining(players)
remaining_players_name = []
for player in players: remaining_players_name.append(player.name)
print(remaining_players_name)