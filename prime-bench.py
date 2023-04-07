import time

number_of_primes_to_find = 500000

number = 1
number_of_primes = 1
start_time = time.time()

while number_of_primes <= number_of_primes_to_find - 1:
    number += 2
    # print(f'number : {number}')
    possible_factor = 3
    while possible_factor**2 <= number:
        if number % possible_factor == 0:
            # print(f'not prime: {number}')
            break
        possible_factor += 2
    else:
        # print(f'PRIME: {number}')
        number_of_primes += 1


end_time = time.time()


print(f'found {number_of_primes_to_find} primes in {end_time - start_time} seconds. {number_of_primes_to_find}th/nd prime: {number}')
