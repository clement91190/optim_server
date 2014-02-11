from optim_algos.methods.interface import square_function
import optim_server.endpoints.worker_endpoints as endpoints


def main():
    while True:
        id, params = endpoints.get_task("test")

        print "...got task params: {}".format(params)
        score = square_function(params)
        print " ..returned {}".format(score)
        endpoints.send_results(id, score)


if __name__ == "__main__":
    main()

