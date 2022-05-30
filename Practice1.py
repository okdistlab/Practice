import random
import time

for i in range(3,13):
    bit_s = 2**i                                  # біти
    keys = 2**bit_s                               # кількість варіантів ключів
    rand_key = int(random.getrandbits(bit_s))     # випадкове значення ключа,що залежить від довжини ключа
    print(rand_key)
    start = time.monotonic_ns()
    k = 0
    for k in range(0,keys):
        if k == rand_key:
            print(k)
            break
    finish = time.monotonic_ns()
    duration = finish - start
    print(f"That took {duration // 1000000}ms")   #кількість часу в мілісекундах,яка була витрачена
                                                          #для знаходження ключа
