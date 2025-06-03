import matplotlib.pyplot as plt
import matplotlib.animation as animation

class VisualNQueen:
    def __init__(self, size=8):
        self.size = size
        self.states = []        # (row, col, is_placing, solution_count)
        self.solutions = []     # 完整的解
        self.solution_count = 0

    def solve(self):
        self.backtrack(0, [])

    def backtrack(self, row, state):
        if row == self.size:
            self.solution_count += 1
            self.solutions.append(state[:])
            self.states.append((row - 1, state[-1], True, self.solution_count))  # 解的最後一步
            return
        for col in range(self.size):
            if self.is_safe(state, row, col):
                state.append(col)
                self.states.append((row, col, True, self.solution_count))
                self.backtrack(row + 1, state)
                self.states.append((row, col, False, self.solution_count))
                state.pop()

    def is_safe(self, state, row, col):
        for r in range(row):
            c = state[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def print_solution_to_console(self, state, index):
        print(f"Solution {index + 1}:")
        for row in range(self.size):
            line = ""
            for col in range(self.size):
                line += "Q " if state[row] == col else ". "
            print(line)
        print()

    def animate(self):
        fig, ax = plt.subplots()
        table = ax.table(cellText=[[""] * self.size for _ in range(self.size)],
                         cellLoc='center',
                         loc='center',
                         cellColours=[['white'] * self.size for _ in range(self.size)],
                         colWidths=[0.1] * self.size)
        ax.axis('off')

        solution_text = ax.text(0.02, 1.05, f"Solutions found: 0", transform=ax.transAxes, fontsize=12)

        printed_solutions = set()

        def update(frame):
            row, col, is_placing, count = self.states[frame]
            color = 'lightblue' if is_placing else 'white'
            text = 'Q' if is_placing else ''
            table[row, col].get_text().set_text(text)
            table[row, col].set_facecolor(color)
            solution_text.set_text(f"Solutions found: {count}")

            # 如果 count 新增，印出對應的 solution
            if count > 0 and count not in printed_solutions:
                printed_solutions.add(count)
                self.print_solution_to_console(self.solutions[count - 1], count - 1)

        ani = animation.FuncAnimation(fig, update, frames=len(self.states), interval=30, repeat=False)
        plt.show()

if __name__ == "__main__":
    visual = VisualNQueen()
    visual.solve()
    visual.animate()
