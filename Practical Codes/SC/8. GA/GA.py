import random

# Parameters
POP_SIZE, CHR_LEN, MUT_RATE, GEN_MAX = 10, 10, 0.1, 100

# Initialize population
pop = [''.join(random.choice('01') for _ in range(CHR_LEN)) for _ in range(POP_SIZE)]

def fitness(c): return sum(map(int, c))
def select(pop, fit):
    r, s = random.uniform(0, sum(fit)), 0
    for i, f in enumerate(fit):
        s += f
        if s >= r: return pop[i]

def crossover(p1, p2):
    pt = random.randint(1, CHR_LEN - 1)
    return p1[:pt] + p2[pt:], p2[:pt] + p1[pt:]

def mutate(c):
    return ''.join('0' if g == '1' and random.random() < MUT_RATE else
                   '1' if g == '0' and random.random() < MUT_RATE else g for g in c)

for g in range(GEN_MAX):
    fit = [fitness(c) for c in pop]
    best = pop[fit.index(max(fit))]
    print(f"Gen {g}: Best = {best}, Fitness = {max(fit)}")
    if max(fit) == CHR_LEN: break
    new = []
    for _ in range(POP_SIZE // 2):
        p1, p2 = select(pop, fit), select(pop, fit)
        c1, c2 = crossover(p1, p2)
        new += [mutate(c1), mutate(c2)]
    pop = new
