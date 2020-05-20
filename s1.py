import random

colors = {
    1: 'red',
    2: 'blue',
    3: 'green',
    4: 'yellow',
    5: 'white'
}

GAME_LEN = 4
initial = []
while len(initial) < GAME_LEN:
    r = random.randint(1, 5)
    if r not in initial:
        initial.append(r)
# c = []
# for i in initial:
#     c.append(colors[i])

# print(c)
initial = [colors[i] for i in initial]
# print(initial)

win = False
for i in range(2):
    guess = input()
    guess = guess.split(",")
    black = 0
    white = 0

    for i in range(GAME_LEN):
        if initial[i] == guess[i]:
            black += 1
        else:
            if guess[i] in initial:
                white += 1
    print('black: {} , white: {}'.format(black, white))
    if black == GAME_LEN:
        print("you won!")
        win = True
if not win:
    initial_state = ','.join(initial)
    print("you lost! and initial state was {}:".format(initial_state))