# arguments = "2 2 2"
arguments = open("rosalind_iprb.txt").read().strip()
k, m, n = map(int, arguments.split(" "))
n_population = k + m + n
population = [0 for _ in range(k)] + [1 for _ in range(m)] + [2 for _ in range(n)]

probability = 0

for i in range(n_population):
    for j in range(i + 1, n_population):
        if population[i] == 0 and population[j] == 0:
            probability += 1
        elif population[i] == 0 and population[j] == 1:
            probability += 1
        elif population[i] == 0 and population[j] == 2:
            probability += 1
        elif population[i] == 1 and population[j] == 1:
            probability += 0.75
        elif population[i] == 1 and population[j] == 2:
            probability += 0.5
        elif population[i] == 2 and population[j] == 2:
            probability += 0

probability /= (n_population * (n_population - 1) / 2)

print(probability)