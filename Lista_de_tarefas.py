# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 19:42:42 2022

@author: Everton SSD
"""

def TelaInicial():
    adicionartarefa = '1 - Adicionar Tarefa'
    Listatarefa = '2 - Lista de tarefas'
    DesfazerTarefa = '3 - Desfazer a ultima ação'
    RefazTarefa = '4 - Refaz/Altera a ultima ação'
    Escrevetxt = '5 - Salvar como um arquivo txt'
    print("Por favor selecione a opção que deseja meu nobre:")
    sOpcao = input(f'{adicionartarefa}\n{Listatarefa}\n{DesfazerTarefa}\n{RefazTarefa}\n{Escrevetxt}\n')
    if sOpcao == '1':
        lTarefas.append(input('Digite o que desejar meu nobre:\n'))
        return ApresentarTarefa()
    elif sOpcao == '2':
        if lTarefas == [] or None:
            print('Não há nada na sua lista de tarefa')
            return TelaInicial()
        else:
            for n, tarefas in enumerate(lTarefas):
                print(f'\t{n} - {tarefas}')
            print('\n')
            return TelaInicial()
    elif sOpcao == '3':
        ...
    elif sOpcao == '4':
        ...
    elif sOpcao == '5':
        sNome = input('Digite um título para seu arquivo, caso não queira, aperte ENTER')
        if sNome == None or sNome == '':
            EscreveTxt()
            sOpcao = input('Deseja finalizar por aqui sua lista?\n[Y] | [N]\t')
            if sOpcao.upper() == 'Y':
                print('Gracias :)')
            else:
                return TelaInicial()
        else: 
            EscreveTxt(sNome)
            sOpcao = input('Deseja finalizar por aqui sua lista?\n[Y] | [N]\t')
            if sOpcao.upper() == 'Y':
                print('Gracias :)')
            else:
                return TelaInicial()
def EscreveTxt(Var = 'Lista de Tarefas'):
    with open(f'{Var}' + '.txt', 'w+') as file:
        file.write('Sua lista de tarefas:\n')
        n = 1
        for n, tarefas in enumerate(lTarefas):
            file.write(f'\t{n} - {tarefas}\n')
            
def VoltarTelaInicial():
    sTelaInicial = input('Deseja voltar para tela inicial??\n[Y] | [N]\t')
    if sTelaInicial.upper == 'Y':
        return TelaInicial()
    else:
        sOpcao = input('Deseja realmente finalizar por aqui sua lista de tarefas?\n[Y] | [N]\t')
        if sOpcao.upper() == 'Y':
            print('Ok')
        else:
            return TelaInicial()
def ApresentarTarefa():
    print('\nSua tarefa foi anotada com sucesso :)\nAqui está ela!!:\n')
    print(f'-> {lTarefas[-1]}')
    sdeseja = input('Deseja ver todas tarefas anotadas até agora?\n[Y] | [N]\t')
    if sdeseja.upper() == 'Y':
        print('Sua lista de tarefas:')
        for tarefas in lTarefas:
            print(f'    {tarefas}')
        return TelaInicial() 
    else:
        return TelaInicial()   
def Apresentacao():
    print("Bem vindo a sua lista de tarefas\nEla será anotada e escrita em um bloco de notas no final deste laço")
    print('Vamos começar!!\n')
    return TelaInicial()
    
if __name__ == '__main__':
    lTarefas = []
    sTarefa = ''
    Apresentacao()  