import random

# Constants
ROWS = 6
COLS = 7
EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'
WIN = 1
DRAW = 0.5
LOSS = 0

# Initialize the starting position
def create_starting_pos():
    return {"board": [[EMPTY for _ in range(COLS)] for _ in range(ROWS)], "to_move": PLAYER_X}

# Display the board
def dump_pos(pos):
    for row in pos['board']:
        print('|' + ''.join(row) + '|')
    print('|' + ''.join(str(i) for i in range(COLS)) + '|')

# Generate all legal moves
def moves(pos):
    return [col for col in range(COLS) if pos['board'][0][col] == EMPTY]

# Apply a move
def make_move(pos, col):
    new_pos = {"board": [row[:] for row in pos['board']], "to_move": PLAYER_X if pos['to_move'] == PLAYER_O else PLAYER_O}
    for row in reversed(new_pos['board']):
        if row[col] == EMPTY:
            row[col] = pos['to_move']
            break
    return new_pos

# Check for a win or draw
def is_over(pos):
    for row in range(ROWS):
        for col in range(COLS):
            if pos['board'][row][col] != EMPTY:
                if check_win(pos['board'], row, col):
                    return True
    return all(pos['board'][0][col] != EMPTY for col in range(COLS))

# Check for a win from a specific position
def check_win(board, row, col):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    player = board[row][col]

    for dr, dc in directions:
        count = 0
        for i in range(-3, 4):
            r, c = row + i * dr, col + i * dc
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0

    return False

# Simulate random games (Monte Carlo)
def simulate(pos, move, my_side, N=200):
    wins = 0
    for _ in range(N):
        sim_pos = make_move(pos, move)
        while not is_over(sim_pos):
            possible_moves = moves(sim_pos)
            sim_pos = make_move(sim_pos, random.choice(possible_moves))

        if is_winner(sim_pos, my_side):
            wins += 1
        elif is_over(sim_pos):
            wins += 0.5

    return wins / N

# Check if a player is the winner
def is_winner(pos, player):
    return any(check_win(pos['board'], r, c) for r in range(ROWS) for c in range(COLS) if pos['board'][r][c] == player)

# AI using Pure Monte Carlo
def pure_mc(pos, N=200):
    my_side = pos['to_move']
    win_counts = {move: simulate(pos, move, my_side, N) for move in moves(pos)}

    # Displaying win percentages
    print("\nWin Percentages for Each Move:")
    for move, win_rate in win_counts.items():
        print(f"Move {move}: {win_rate * 100:.2f}%")

    return max(win_counts, key=win_counts.get)

# Main Game Loop
def play_game(player_side="X"):
    pos = create_starting_pos()
    playing = True

    while playing:
        dump_pos(pos)
        if pos["to_move"] == player_side:
            movestr = input("Your move? ")
            move = int(movestr)
        else:
            move = pure_mc(pos)

        pos = make_move(pos, move)

        if is_over(pos):
            dump_pos(pos)
            print("Game Over!")
            playing = False

if __name__ == "__main__":
    play_game()
