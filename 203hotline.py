#!/usr/bin/python3
import sys
from math import *

def usage():
    print("USAGE")
    print("\t\t./203hotline [n k | d]\n")
    print("DESCRIPTION")
    exit(0)
    

def make_calc_for_two(nb):
    print("Binomial distribution:")
    phone = 3500
    power = nb / (3600 * 8)
    exit (0)

def make_calc_for_three(nb1, nb2):
    tmp1 = factorial(nb2)
    tmp2 = factorial(nb1)
    tmp3 = factorial(nb1 - nb2)
    tmp4 = tmp2 // (tmp1 * tmp3)
    print("%0.0f-combination of a %0.0f set:\n%d" %(nb2, nb1, tmp4))
    exit (0)

def do_all():
    if (len(sys.argv) == 2):
        nb = int(sys.argv[1])
        make_calc_for_two(nb)
    if (len(sys.argv) == 3):
        nb1 = int(sys.argv[1])
        nb2 = int(sys.argv[2])
        make_calc_for_three(nb1, nb2)

def check_error_for_two():
    try:
        nb = int(sys.argv[1])
    except:
        exit(84)

def check_error_for_three():
    try:
        nb = int(sys.argv[1])
        nb2 = int(sys.argv[2])
    except:
        exit(84)

def check_error():
    if (len(sys.argv) == 2):
        if (sys.argv[1] == "-h"):
            usage()
    if (len(sys.argv) > 3 or len(sys.argv) < 2):
        exit (84)
    if (len(sys.argv) == 2):
        check_error_for_two()
    if (len(sys.argv) == 3):
        check_error_for_three()

def main():
    check_error()
    do_all()

main()