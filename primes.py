"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    list = []
    num = 2
    if (number_of_primes > 0):
        while len(list) < number_of_primes:
            if all(num % prime != 0 for prime in list):
                list.append(num)
            num += 1
    else:
        raise ValueError(
            f"You entered {number_of_primes}, which is not a positive number.")
    return list
