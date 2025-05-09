import random

class NQPosition:
    def __init__(self, N):
        self.N = N
        # Initialize a random board state
        self.board = [random.randint(0, N - 1) for _ in range(N)]

    def value(self):
        # Calculate the number of conflicts between queens
        conflicts = 0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                if self.board[i] == self.board[j] or \
                   abs(self.board[i] - self.board[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def make_move(self, move):
        col, row = move
        self.board[col] = row

    def best_move(self):
        current_value = self.value()
        best_move = None
        best_value = current_value

        for col in range(self.N):
            original_row = self.board[col]
            for row in range(self.N):
                if row == original_row:
                    continue

                self.board[col] = row
                value = self.value()

                if value < best_value:
                    best_value = value
                    best_move = (col, row)

            self.board[col] = original_row  # Restore original

        return best_move, best_value


def hill_climbing(pos):
    curr_value = pos.value()
    while True:
        move, new_value = pos.best_move()
        if new_value >= curr_value:
            return pos, curr_value
        else:
            curr_value = new_value
            pos.make_move(move)


if __name__ == '__main__':
    N = 4  # board sizes
    pos = NQPosition(N)
    print("Initial position:", pos.board)
    print("Initial value:", pos.value())

    best_pos, best_value = hill_climbing(pos)
    print("Final position:", best_pos.board)
    print("Final value:", best_value)
