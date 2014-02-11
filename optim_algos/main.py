import optim_server.endpoints.optim_algo_endpoints as endpoints
from methods.simplex import Simplex
from methods.interface import Test



def main():
    optim_problem = "test"
    optim_run = endpoints.get_run_num(optim_problem)
    print optim_problem, optim_run
    fitness = lambda tab: endpoints.eval_fitness_function(tab, optim_problem, optim_run)
    algo = Simplex(fitness)
    t = Test(algo, (None, 2), 1000)
    t.optimize()
    

if __name__ == "__main__":
    main()
