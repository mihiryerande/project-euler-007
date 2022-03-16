# Problem 7:
#     10,001st Prime
#
# Description:
#     By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
#       we can see that the 6th prime is 13.
#
#     What is the 10,001st prime number?

def main(n):
    """
    Return the `n`th consecutive prime number.

    Args:
        n (int): Natural number

    Returns:
        `n`th prime number

    Raises:
        AssertError: if incorrect params are given
    """
    assert type(n) == int and n > 0

    x = 1
    primes = []
    while len(primes) < n:
        x += 1
        is_prime = True
        for p in primes:
            if x % p == 0:
                is_prime = False
                break
            else:
                continue
        if is_prime:
            # x not divisible by any primes found so far
            primes.append(x)
        else:
            continue
    return primes[-1]


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    prime = main(num)
    print('Prime #{}:\n{}'.format(num, prime))
