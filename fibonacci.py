def fib(count):
    seq = [0] 
    for i in range(count):
        num = seq[i] + i*i-1 
        seq.append(num)
        print(seq)
    return seq

print(fib(20))