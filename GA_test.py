import pygad
import numpy as np

function_inputs = [4, -2, 3.5, 5, -11, -4.7]  # Function inputs.
desired_output = 44  # Function output.


def fitness_func(solution, solution_idx):
    output = np.sum(solution * function_inputs)
    fitness = 1.0 / np.abs(output - desired_output)
    return fitness


def on_generation(ga_instance):
    print(np.average(ga_instance.last_generation_fitness))

sol_per_pop = 50
num_genes = len(function_inputs)

init_range_low = -2
init_range_high = 5

mutation_probability = 0.5

ga_instance = pygad.GA(num_generations=50,
                       num_parents_mating=5,
                       fitness_func=fitness_func,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       init_range_low=init_range_low,
                       init_range_high=init_range_high,
                       mutation_probability=mutation_probability,
                       save_solutions=True,
                       on_generation=on_generation)

ga_instance.run()
ga_instance.plot_fitness()
# ga_instance.plot_genes()
# ga_instance.plot_new_solution_rate()
print(ga_instance.best_solutions_fitness)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))
print(np.sum(solution * function_inputs))

