from operator import add 


def convert(celcius):
    f = celcius * 9 / 5 + 32
    return f

def add_vectors(a, b):
    return list(map(add, a, b))
