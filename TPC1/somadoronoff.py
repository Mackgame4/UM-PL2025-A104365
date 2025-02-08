import sys

ON_STR = 'on'
OFF_STR = 'off'
EQUALS_STR = '='

def somadoronoff(l):
    isOn = False
    soma = 0
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
            if isOn:
                soma += valor
        elif l[i:].startswith(ON_STR):
            isOn = True
            i += len(ON_STR)
        elif l[i:].startswith(OFF_STR):
            isOn = False
            i += len(OFF_STR)
        elif l[i:].startswith(EQUALS_STR):
            i += len(EQUALS_STR)
            print(soma)
            #soma = 0 # dont reset the sum
        else:
            i += 1

def main():
    for l in sys.stdin:
        l = l.lower() # put all characters in lower case to check with the strings variables
        somadoronoff(l)

if __name__ == '__main__':
    main()