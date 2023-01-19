
def decimal_to_binary(convert):
    i = 0
    op = convert

    binary = [0,0,0,0,0,0,0,0,0,0]

    for count in range(10,0,-1):

        square = 2**(count-1)

        if op - square >= 0:
            binary[count-1] = 1
            op -= square
        else:
            continue

    return print(" ".join(str(binary[::-1])))

decimal_to_binary(345)

