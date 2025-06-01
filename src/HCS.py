import random
from typing import List, Tuple, Literal

TransitionModelType = Literal['swap', 'move']

class EightQueensProblem:
    def __init__(self, initial_state: List[int] = None, transition_model: TransitionModelType = 'move'):
        self.size = 8
        self.transition_model = transition_model
        self.initial_state = initial_state if initial_state else self.random_state()
        #print("self.initial_state",self.initial_state) #set the position of the row

    def random_state(self) -> List[int]: 
        return [random.randint(0, self.size - 1) for _ in range(self.size)]
    
    def actions(self, state: List[int]) -> List[Tuple[int, int]]:
        if self.transition_model == 'move': #return every posible move
            return [(col, row) for col in range(self.size)
                    for row in range(self.size) if state[col] != row]
        elif self.transition_model == 'swap': #change the position of two queen
            return [(i, j) for i in range(self.size) for j in range(i+1, self.size)]

    def result(self, state: List[int], action: Tuple[int, int]) -> List[int]:
        new_state = state.copy()
        if self.transition_model == 'move':
            col, new_row = action
            new_state[col] = new_row
        elif self.transition_model == 'swap':
            i, j = action
            new_state[i], new_state[j] = new_state[j], new_state[i]
        return new_state

    def heuristic(self, state: List[int]) -> int: #count the conflict
        conflicts = 0
        for i in range(len(state)):
            for j in range(i+1, len(state)):
                if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def cost(self, state: List[int], action: Tuple[int, int]) -> int:
        return 1

    def is_goal(self, state: List[int]) -> bool:
        return self.heuristic(state) == 0

    def display(self, state: List[int]) -> None: #because the rule(not in same col),set the program just care about row
        print("\n  +-----------------+")
        for row in range(self.size):
            line = "  |"
            for col in range(self.size): #check every col
                if state[col] == row: 
                    line += " Q"
                else:
                    line += " ."
            print(line + " |")
        print("  +-----------------+")

    def solve_hill_climbing(self) -> Tuple[List[int], int]:
        current = self.initial_state
        steps = 0
        while True:
            current_h = self.heuristic(current)
            neighbors = [self.result(current, action) for action in self.actions(current)]
            neighbors.sort(key=self.heuristic)
            best_neighbor = neighbors[0] if neighbors else None
            if best_neighbor is None or self.heuristic(best_neighbor) >= current_h:
                break
            current = best_neighbor
            steps += 1
        return current, steps

if __name__ == "__main__":
    problem = EightQueensProblem(transition_model='move')
    print("Initial State:")
    problem.display(problem.initial_state)
    print(f"Initial Heuristic: {problem.heuristic(problem.initial_state)}")

    print("\nSolving using Hill Climbing...")
    final_state, steps = problem.solve_hill_climbing()

    print("\nFinal State:")
    problem.display(final_state)
    print(f"Final Heuristic: {problem.heuristic(final_state)}")
    print(f"Total Cost (steps taken): {steps}")
