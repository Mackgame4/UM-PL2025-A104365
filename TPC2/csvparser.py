from tcolors import Back, Fore

"""
def read_csv():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'obras.csv')
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
"""

class Obra:
    def __init__(self, nome, desc, anoCriacao, periodo, compositor, duracao, _id):
        self.nome = nome
        self.desc = desc
        self.anoCriacao = anoCriacao
        self.periodo = periodo
        self.compositor = compositor
        self.duracao = duracao
        self._id = _id

def split_line(line):
    fields = []
    constructed_string = ""
    inside_quotes = False
    for char in line:
        if char == '"':
            inside_quotes = not inside_quotes
        elif char == ';' and not inside_quotes:
            fields.append(constructed_string.strip())
            constructed_string = ""
        else:
            constructed_string += char
    fields.append(constructed_string.strip())
    return fields

def read_csv(file_path):
    data = []
    buffer = ""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]: # Skip the header
            line = line.strip()
            if not line:
                continue
            buffer += line + " "
            fields = split_line(buffer.strip())
            if len(fields) == 7: # All fields were read
                data.append(Obra(*fields))
                buffer = ""
        return data

def inverter_nome(compositor):
    if ',' in compositor:
        partes = compositor.split(',')
        return f"{partes[1].strip()} {partes[0].strip()}"
    return compositor

def obter_compositores(obras):
    # Extrair os nomes dos compositores e ordenar alfabeticamente
    return sorted(set(inverter_nome(obra.compositor) for obra in obras), key=lambda x: x.split()[-1])

def contar_obras_por_periodo(obras):
    # Contar o número de obras por período
    periodo_count = {}
    for obra in obras:
        if obra.periodo not in periodo_count:
            periodo_count[obra.periodo] = 0
        periodo_count[obra.periodo] += 1
    return periodo_count

def obras_por_periodo(obras):
    # Agrupar as obras por período
    obras_dict = {}
    for obra in obras:
        if obra.periodo not in obras_dict:
            obras_dict[obra.periodo] = []
        obras_dict[obra.periodo].append(obra.nome)
    return obras_dict

def menu():
    print(Back.BLUE + "Menu" + Back.RESET)
    print(Fore.YELLOW + "1. " + Fore.RESET + "Listagem ordenada dos compositores musicais")
    print(Fore.YELLOW + "2. " + Fore.RESET + "Distribuição das obras por período")
    print(Fore.YELLOW + "3. " + Fore.RESET + "Listagem das obras por período")
    print(Fore.YELLOW + "0. " + Fore.RESET + "Sair")
    option = input(Fore.YELLOW + "Escolha uma opção: " + Fore.RESET)
    return option

def main():
    dados = read_csv('obras.csv')
    while True:
        option = menu()
        if option == "1":
            print(Back.BLUE + "Compositores ordenados alfabeticamente:" + Back.RESET)
            compositores = obter_compositores(dados)
            for compositor in compositores:
                print(compositor)
        elif option == "2":
            print(Back.BLUE + "Distribuição das obras por período:" + Back.RESET)
            periodo_count = contar_obras_por_periodo(dados)
            for periodo, count in periodo_count.items():
                print(f"{periodo}: {count} obras")
        elif option == "3":
            print(Back.BLUE + "Obras por período:" + Back.RESET)
            obras_dict = obras_por_periodo(dados)
            for periodo, obras in obras_dict.items():
                print(f"{periodo}:")
                for obra in obras:
                    print(f"  - {obra}")
        elif option == "0":
            print(Fore.RED + "Saindo..." + Fore.RESET)
            break
        else:
            print(Back.RED + "[ERROR]" + Back.RESET + " " + Fore.RED + "Opção inválida! Tente novamente." + Fore.RESET)

if __name__ == "__main__":
    main()