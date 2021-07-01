import random

# Рандомный граф
print('Матрица смежности:')
N = []
for city in range(10):
    N.append([])
    for nearby_city in range(10):
        N[city].append(None)
for city in range(9):
    N[city][city] = 0
    for nearby_city in range(city + 1, 10):
        N[city][nearby_city] = random.randint(1, 9)
        N[nearby_city][city] = N[city][nearby_city]
    print(N[city])
N[9][9] = 0
print(N[9])


# Функция приспособленности
def fi(p):
    total = 0
    flag = True
    for i in range(10):
        if N[p[i]][p[(i+1) % 10]] != -1:
            total += N[p[i]][p[(i + 1) % 10]]
        else:
            flag = False

    if flag:
        return total
    else:
        return 1000


# Воспроизводство потомков
def children(chromosome):
    part = [[], [], []]
    part[0] = [chromosome[0], chromosome[1], chromosome[2]]
    part[1] = [chromosome[3], chromosome[4], chromosome[5], chromosome[6]]
    part[2] = [chromosome[7], chromosome[8], chromosome[9]]
    random.shuffle(part[random.randint(0, 2)])
    new_chromosome = []
    new_chromosome.extend(part[0])
    new_chromosome.extend(part[1])
    new_chromosome.extend(part[2])
    return new_chromosome


# Мутация
def mutation(chromosome):
    n = len(chromosome)
    i = random.randint(0, n-1)
    chromosome[i], chromosome[n - 1 - i] = chromosome[n - 1 - i], chromosome[i]
    return chromosome


# Селекция(та же сортировка просто потом отбираем 10 лучших)
def selection(p):

    for i in range(len(p)):
        for j in range(i, len(p)):
            if fi(p[i]) > fi(p[j]):
                p[i], p[j] = list(p[j]), list(p[i])
    new_p = []
    for i in range(10):
        new_p.append(p[i])

    return new_p


genes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
min_way = 1000
min_chromosome = []
population = []

# первое поколение
for ch in range(10):
    random.shuffle(genes)
    population.append(list(genes))
    if fi(population[ch]) != 1:
        if min_way > fi(population[ch]):
            min_way = fi(population[ch])
            min_chromosome = population[ch]

# следующее поколение
for generation in range(1000):
    # Воспроизводство потомсва
    child = []
    for _ in range(5):
        child.append(children(random.choice(population)))
    population.extend(child)

    # Воспроизводство мутантов
    mutant = []
    for _ in range(5):
        mutant.append(mutation(random.choice(population)))
    population.extend(mutant)

    # Селекция
    population = selection(population)

    for chrom in range(len(population)):
        if min_way > fi(population[chrom]):
            min_way = fi(population[chrom])
            min_chromosome = list(population[chrom])


print()
print('Минимальная найденная длина пути:', min_way)
print('Путь: ', min_chromosome)
