import optim_server.endpoints.optim_algo_endpoints as work_endpoints
from methods.simplex import Simplex
from methods.genetic_algorithms import GeneticAlgorithm
from methods.interface import Test


def main():
    optim_problem = "quad_learning"
    optim_run = work_endpoints.get_run_num(optim_problem)
    print optim_problem, optim_run
<<<<<<< HEAD
    fitness = lambda tab: endpoints.eval_fitness_function(tab, optim_problem, optim_run)
    algo = GeneticAlgorithm(fitness)
    t = Test(algo, (None, 2), 1000)
=======
    fitness = lambda tab: work_endpoints.eval_fitness_function(tab, optim_problem, optim_run)
    algo = Simplex(fitness)
    size = 9  #num of free params
    t = Test(algo, (None, size), 1000)
>>>>>>> 8121bc2c2d5cb08321b0fe49be0a96d544931c83
    t.optimize()
    

if __name__ == "__main__":
    main()
