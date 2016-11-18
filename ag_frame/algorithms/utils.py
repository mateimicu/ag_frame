"""
Util functions for Algiruthms.
"""
import math
import random


def get_nr_bits(domain, pre):
    """Return the number of bits that are needed."""
    domain_lenght = domain[1] - domain[0]
    return int(math.ceil(math.log(domain_lenght * 10 ** pre, 2)))


def get_real(domain, pre, bits):
    """Return the real number."""
    nr_bits = get_nr_bits(domain, pre)
    converted = int(bits, 2)  # convert in base 10
    domain_lenght = domain[1] - domain[0]
    return domain[0] + ((float(converted)*float(domain_lenght)) /
                        float(2 ** nr_bits - 1))


def mutate(string, poz):
    """Mutate a position."""
    rand = random.random()
    string = list(string)
    if rand <= 0.5:
        string[poz] = '1'
    else:
        string[poz] = '0'
    return "".join(string)


def mutate_random(string):
    """Mutate a string random."""
    needle = random.randint(0, len(string)-1)
    return mutate(string, needle)


def randomise_a_string(string):
    """Random on a string."""
    for i, _ in enumerate(string):
        string = mutate(string, i)

    return string


def string_to_args(string, size_var, domains, precision):
    """Convert a binary string to a list of arguments.

    :param string: The binary string
    :param size_var: A list with the size of every variable
    :param domains: A list with the domain for every variable
    :param precision: The precision
    """
    args = []
    for index, size in enumerate(size_var):
        start = sum(size_var[0:index-1])
        bit = string[start:start+size]

        args.append(get_real(domains[index],
                             precision,
                             bit))
    return args
