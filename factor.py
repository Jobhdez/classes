def factor(exp):
    div = 1
    for i in range(2, 10):
        if exp[0] % i == 0 and exp[4] % i == 0:
            div = i
    
    e1 = exp[0] / div
    e2 = exp[4] / div

    return (div, exp[1], ((e1, exp[2]), exp[3], e2))
