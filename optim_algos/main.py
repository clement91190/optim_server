import optim_server.endpoints.optim_algo_endpoints as work_endpoints
from methods.simplex import Simplex
from methods.genetic_algorithms import GeneticAlgorithm
from methods.interface import Test


def main():
    optim_problem = "quad_learning"
    optim_run = work_endpoints.get_run_num(optim_problem)
    print optim_problem, optim_run
    fitness = lambda tab: work_endpoints.eval_fitness_function(tab, optim_problem, optim_run)
    algo = GeneticAlgorithm(fitness)
    size = 9  # num of free params
    t = Test(algo, (None, size), 1000)
    t.optimize()
    

if __name__ == "__main__":
    main()
