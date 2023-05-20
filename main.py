def count_primes(num):
    #Checks 0 or 1 input
    if num < 2:
        return 0

    # 2 or greater

    #Store the prime numbers
    primes = [2]
    #Counter that goes into the input num
    x = 3

    # X is going through every number up to the input number
    while x <= num:
        # Check if x is prime
        for y in range(3,x,2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

count_primes(100)