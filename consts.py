GAME_LENGTH = 4
COLORS = {
    1: 'red',
    2: 'blue',
    3: 'green',
    4: 'yellow',
    5: 'white'
}

MIN_COLOR = min(COLORS.keys())
MAX_COLOR = max(COLORS.keys())

MAX_TURNS = 1

WIN_MESSAGE = "you won!"
LOSE_MESSAGE= "you lost! and initial state was {}:"
