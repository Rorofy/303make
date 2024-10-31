from sys import *

def print_help():
    if "-h" in argv or "--help" in argv:
        print(
            "USAGE\n"
            "\t./303make makefile [file]\n"
            "DESCRIPTION\n"
            "\tmakefile\tname of the makefile\n"
            "\tfile\t\tname of a recently modified file"
        )
        exit(0)
    return


def check_file_valid():
    try:
        f = open(argv[1])
    except IOError:
        print("%s is not a valid file." % (argv[1]))
        exit(84)
    else:
        f.close()
        return 0

def checkArgs():
    if (len(argv) != 2 and len(argv) != 3):
        print("Wrong number of arguments")
        exit(84)
    print_help()
    check_file_valid()
    