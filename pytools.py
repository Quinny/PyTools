import sys

def assert_n_args(n, usage = None):
    if len(sys.argv) != n + 1:
        if usage is not None:
            print usage
        else:
            print sys.argv[0] + " requires at least " + str(n) + " argument(s)"
        exit(0)
