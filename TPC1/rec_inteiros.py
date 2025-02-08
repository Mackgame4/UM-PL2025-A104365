import sys

def rec_inteiros(l):
    res = []
    i = 0
    while i < len(l):
        valor = 0
        sinal = 1
        if l[i] == '-':
            sinal = -1
            i += 1
        if l[i] in '0123456789':
            while l[i] in '0123456789':
                valor = valor * 10 + int(l[i])
                i += 1
            valor *= sinal
            res.append(valor)
        else:
            i += 1
    return res

def main():
    for l in sys.stdin:
        inteiros = rec_inteiros(l)
        print(inteiros)

if __name__ == '__main__':
    main()