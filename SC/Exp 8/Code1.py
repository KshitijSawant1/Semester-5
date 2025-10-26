import random

# Define parameters
population_size = 10
chromosome_length = 10
mutation_rate = 0.1

# Initialize a population with random binary strings
def initialize_population():
    return [''.join(random.choice('01') for _ in range(chromosome_length)) for _ in range(population_size)]

# Fitness function for the One Max problem
def fitness_function(chromosome):
    return sum(int(gene) for gene in chromosome)

# Selection operator: Roulette Wheel Selection
def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    rand_num = random.uniform(0, total_fitness)
    partial_sum = 0
    for i in range(len(population)):
        partial_sum += fitness_values[i]
        if partial_sum >= rand_num:
            return population[i]

# Crossover operator: Single-Point Crossover
def single_point_crossover(parent1, parent2):
    crossover_point = random.randint(1, chromosome_length - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation operator: Bit Flip Mutation
def bit_flip_mutation(chromosome):
    mutated_chromosome = list(chromosome)
    for i in range(chromosome_length):
        if random.random() < mutation_rate:
            mutated_chromosome[i] = '0' if chromosome[i] == '1' else '1'
    return ''.join(mutated_chromosome)

# Create a new generation
def generate_new_population(population, fitness_values):
    new_population = []
    for _ in range(population_size):
        parent1 = roulette_wheel_selection(population, fitness_values)
        parent2 = roulette_wheel_selection(population, fitness_values)
        child1, child2 = single_point_crossover(parent1, parent2)
        child1 = bit_flip_mutation(child1)
        child2 = bit_flip_mutation(child2)
        new_population.extend([child1, child2])
    return new_population

# Main GA loop
population = initialize_population()

generations = 100
for generation in range(generations):
    fitness_values = [fitness_function(chromosome) for chromosome in population]
    best_chromosome = population[fitness_values.index(max(fitness_values))]
    print(f"Generation {generation}: Best fitness = {max(fitness_values)}, Best solution = {best_chromosome}")

    if max(fitness_values) == chromosome_length:
        break

    population = generate_new_population(population, fitness_values)
