from datetime import datetime
import json
import os

lista_funcionarios = []

def ler_valor_nao_vazio(nome_variavel):
    valor_lido = input(f'Entre com o valor para {nome_variavel} do funcionario: ')
    while valor_lido == '':
        print(f'O valor para {nome_variavel} não pode ser vazio!')
        valor_lido = input(f'Entre com o valor para {nome_variavel} do funcionario: ')
    return valor_lido

def verifica_data_valida(data_texto):
    try:
        data_valida = datetime.strptime(data_texto, "%d/%m/%Y")
        return True
    except:
        return False

def ler_data_valida(nome_data):
    dataString = input(f"Entre com a data de {nome_data} do contrato: ")
    while not verifica_data_valida(dataString):
        print('Data inválida!')
        dataString = input(f"Entre com a data de {nome_data} do contrato: ")
    data = datetime.strptime(dataString, "%d/%m/%Y")
    return data

def listar_funcionarios(lista):
    if not lista:
        print("Nenhum funcionário cadastrado.")
    for i, funcionario in enumerate(lista):
        print(f"===== {i+1} =====")
        imprimir_funcionario(funcionario)

def deletar_funcionario(lista):
    listar_funcionarios(lista)
    try:
        x = int(input('Digite o numero do funcionário que quer demitir: ')) - 1
        if 0 <= x < len(lista):
            lista.pop(x)
            print("Funcionário removido com sucesso!")
        else:
            print("Número de funcionário inválido.")
    except ValueError:
        print("Digite um número válido.")

def editar_funcionario(lista):
    listar_funcionarios(lista)
    try:
        editX = int(input("Qual funcionário deseja editar? ")) - 1
        if 0 <= editX < len(lista):
            editY = input("O que deseja editar?\n 1- Nome\n 2- Data inicial\n 3- Data final\n 4- Cargo\n ")
            if editY == "1":
                novo_nome = ler_valor_nao_vazio('nome')
                lista[editX]['nome'] = novo_nome 
            elif editY == "2":
                nova_dataI = ler_data_valida('entrada')
                lista[editX]['dataEntrada'] = nova_dataI.strftime('%d/%m/%Y')
            elif editY == "3":
                nova_dataF = ler_data_valida('saída')
                lista[editX]['dataSaida'] = nova_dataF.strftime('%d/%m/%Y')
            elif editY == "4":
                novo_cargo = ler_valor_nao_vazio('cargo')
                lista[editX]['cargo'] = novo_cargo
            else:
                print("Opção inválida.")
            print("Dados alterados com sucesso")
            salvar_json(lista)
        else:
            print("Número de funcionário inválido.")
    except ValueError:
        print("Digite um número válido.")

def ler_funcionario():
    nome = ler_valor_nao_vazio('nome')
    dataEntrada = ler_data_valida('entrada') 
    dataSaida = ler_data_valida('saída')
    cargo = ler_valor_nao_vazio('nome do cargo')

    funcionario = {
            'nome': nome,
            'dataEntrada': dataEntrada.strftime('%d/%m/%Y'),
            'dataSaida': dataSaida.strftime('%d/%m/%Y'),
            'cargo': cargo
        }

    return funcionario

def ler_json():
    if os.path.exists('funcionarios.json'):
        with open('funcionarios.json', 'r') as meu_arquivo:
            return json.load(meu_arquivo)
    return []  

def salvar_json(lista_funcionarios):
    with open("funcionarios.json", "w") as meu_arquivo:
        lista_json = json.dumps(lista_funcionarios, indent=4)
        meu_arquivo.write(lista_json)

def imprimir_funcionario(funcionario):
    print(f"Nome:\t\t{funcionario['nome']}")
    print(f"Entrada:\t{funcionario['dataEntrada']}")
    print(f"Saída:\t\t{funcionario['dataSaida']}")
    print(f"Cargo:\t\t{funcionario['cargo']}")
    
lista_funcionarios = ler_json()

while True:
    menu = input("1- Adicionar funcionário \n2- Ver funcionários \n3- Remover funcionário \n4- Editar funcionário \n5- Sair\n")
    if menu == '1':
        funcionario_1 = ler_funcionario()
        lista_funcionarios.append(funcionario_1)
        salvar_json(lista_funcionarios)
        imprimir_funcionario(funcionario_1)
        
    elif menu == '2':
        listar_funcionarios(lista_funcionarios)

    elif menu == "3":
        deletar_funcionario(lista_funcionarios)

    elif menu == "4":
        editar_funcionario(lista_funcionarios)

    elif menu == "5":
        salvar_json(lista_funcionarios)
        break
