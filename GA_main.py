import numpy as np
import pygad
import time
import fitness_func

t = time.time()
materials_space = [0, 1, 2]
thickness_space = np.arange(10, 1201)
thickness_space = list(thickness_space)
num_generations = 100
num_parents_mating = 10
sol_per_pop = 80
num_genes = 24
crossover_probability = 0.5
mutation_probability = [0.6, 0.3]
save_best_solutions = True
allow_duplicate_genes = True
gene_type = int
gene_space = []
fitness_average_list = []
for _ in range(12):
    gene_space.append(materials_space)
for _ in range(12):
    gene_space.append(thickness_space)


def on_generation(ga_instance):
    fitness_average = np.average(ga_instance.last_generation_fitness)
    fitness_average_list.append(fitness_average)
    print("Generation : {}".format(ga_instance.generations_completed))
    print("Fitness value of the best solution = {}".format(ga_instance.best_solution()[1]))
    print("Average fitness value of the last generation = {}".format(fitness_average))
    elapsed = time.time() - t
    print('Elapsed time = ' + str(elapsed) + 's')


ga_instance = pygad.GA(
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    sol_per_pop=sol_per_pop,
    fitness_func=fitness_func.fitness_func,
    num_genes=num_genes,
    gene_space=gene_space,
    crossover_probability=crossover_probability,
    mutation_probability=mutation_probability,
    mutation_type="adaptive",
    save_best_solutions=save_best_solutions,
    allow_duplicate_genes=allow_duplicate_genes,
    on_generation=on_generation,
    gene_type=gene_type,
    suppress_warnings=True
)

ga_instance.run()
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))
ga_instance.plot_fitness()
filename = "genetic"
ga_instance.save(filename=filename)
with open("fitness.txt", "w", encoding="UTF-8") as file:
    file.write("Generation\taverage-fitness\tbest-fitness\n")
    for iii in range(len(fitness_average_list)):
        file.write("{}\t{:.3f}\t{:.3f}\n".format(iii+1, fitness_average_list[iii], ga_instance.best_solutions_fitness[iii]))


