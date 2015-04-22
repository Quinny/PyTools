import sys

def assert_n_args(n, usage = None):
    if len(sys.argv) != n + 1:
        if usage is not None:
            print usage
        else:
            print sys.argv[0] + " requires at least " + str(n) + " argument(s)"
        exit(0)

def error_if(b, message = None):
    if (b):
        if message is not None:
            print message
        else:
            print sys.argv[0] + ": an error has occured"
        exit(0)
