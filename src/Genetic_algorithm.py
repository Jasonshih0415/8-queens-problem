import random
from typing import List, Tuple, Literal

class Queens8byGenetic:
    def __init__(self):
        self.size = 8
        self.numpopulation = 100
        self.max_conflict = 28
        self.maxgeneration = 100
        self.initial_population = [self.create_population() for _ in range(self.numpopulation)]

    def create_population(self) -> list[int]: #initial state
        return [random.randint(0,self.size-1) for _ in range(self.size)]
    
    def heuristic(self, state: List[int]) -> int: #count the conflict
        conflicts = 0
        for i in range(len(state)):
            for j in range(i+1, len(state)):
                if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                    conflicts += 1
        fitness = self.max_conflict-conflicts
        return fitness
    
    def display(self, state: List[int]) -> None: 
        print("\n  +-----------------+")
        for row in range(self.size):
            line = "  |"
            for col in range(self.size): 
                if state[col] == row: 
                    line += " Q"
                else:
                    line += " ."
            print(line + " |")
        print("  +-----------------+")

    def action(self,parents:Tuple[List[int], List[int]],mutation_rate=0.1)->List[int]:
        parent1=parents[0]
        parent2=parents[1]
        point = random.randint(1, self.size - 2)#crossover
        child=parent1[:point] + parent2[point:]

        for i in range(self.size): #mutate
            if random.random() < mutation_rate:
                child[i] = random.randint(0, self.size - 1)
        return child
    
    def select_parents(self,population) -> Tuple[List[int], List[int]]: #transition_model function
        weights = [self.heuristic(ind) for ind in population]
        parent1, parent2 = random.choices(population, weights=weights, k=2)
        return  parent1, parent2
    
    def genetic_algorithm(self): #transition_model
        generation = 0
        population = self.initial_population

        while True:
            generation += 1
            population = sorted(population, key=lambda x: -self.heuristic(x))
            #show progress
            best_fitness = self.heuristic(population[0])
            print(f"Generation {generation}: Best fitness = {best_fitness} / {self.max_conflict}, Best gene = {population[0]}")

            #check reach the best solution
            if self.heuristic(population[0]) == self.max_conflict:
                print(f"Found solution in generation {generation}")
                return population[0]

            new_population = population[:10]  # Elitism from parent: keep top 10

            while len(new_population) < self.numpopulation: # generate 90 of child 
                parents= self.select_parents(population)
                child = self.action(parents)
                new_population.append(child)

            population = new_population #update population
            #check diversity of population
            unique_genes = {tuple(ind) for ind in population}
            print(f"Unique individuals this generation: {len(unique_genes)} / {self.numpopulation}")
            print("")

            #check generation whether over the limit or not
            if generation > self.maxgeneration:
                print(f"No perfect solution found in {self.maxgeneration} generations.")
                print("Best solution:")
                return population[0]
                 
if __name__ == "__main__":
    ga = Queens8byGenetic()
    best_gene=ga.genetic_algorithm()
    ga.display(best_gene)

