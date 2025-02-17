import sys

ON_STR = 'on'
OFF_STR = 'off'
EQUALS_STR = '='

isOn = True # Start ON by default
soma = 0

def somadoronoff(l):
    global isOn, soma # Use global variables
    i = 0
    while i < len(l):
        valor = 0
        sinal = 1
        if l[i] == '-': # Read signal
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
            print(f">> {soma}")
        else:
            i += 1

def main():
    for l in sys.stdin:
        l = l.lower()
        somadoronoff(l)

if __name__ == '__main__':
    main()
