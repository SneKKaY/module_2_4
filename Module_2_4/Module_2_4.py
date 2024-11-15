# for i in range(1, 11):
#     for k in range(1, 11):
#         print(f'{i} * {k} = {i*k}')
#
# dict_ = {'Dima' : 21, 'Vany' : 18, 'Sofia' : 9}
# for i,k in dict_.items():
#     print(i,k)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i % 2 == 1:
        primes = [i]
        print("Primes: ",[i])
    else:
        print("Not_primes: ", [i])








