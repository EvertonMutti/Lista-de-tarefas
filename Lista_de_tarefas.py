# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 19:42:42 2022

@author: Everton SSD
"""
from DegueMutti import VerificaInt, StringToNumber

def TelaInicial():
    adicionartarefa = '1 - Adicionar Tarefa'
    Listatarefa = '2 - Lista de tarefas'
    DesfazerTarefa = '3 - Desfazer a ultima Tarefa'
    RefazTarefa = '4 - Refaz a ultima Tarefa'
    Escrevetxt = '5 - Salvar como um arquivo txt'
    print("Por favor selecione a opção que deseja meu nobre:")
    sOpcao = input(f'{adicionartarefa}\n{Listatarefa}\n{DesfazerTarefa}\n{RefazTarefa}\n{Escrevetxt}\n')
    if VerificaInt(StringToNumber(sOpcao)):
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
            Desfaz(lTarefas, lListaTemp)
            return TelaInicial()
        elif sOpcao == '4':
            refaz(lTarefas, lListaTemp)
            return TelaInicial()
        elif sOpcao == '5':
            sNome = input('Digite um título para seu arquivo, caso não queira, aperte ENTER')
            if sNome == None or sNome == '':
                if EscreveTxt():
                    sOpcao = input('Deseja finalizar por aqui sua lista?\n[Y] | [N]\t')
                    if sOpcao.upper() == 'Y':
                        print('Gracias :)')
                    else:
                        return TelaInicial()
                else:
                    print('Infelizmente ocorreu uma falha na criação de seu arquivo, mil desculpas.')
                    return TelaInicial()
            else: 
                if EscreveTxt(sNome):
                    sOpcao = input('Deseja finalizar por aqui sua lista?\n[Y] | [N]\t')
                    if sOpcao.upper() == 'Y':
                        print('Gracias :)')
                    else:
                        return TelaInicial()
                else:
                    print('Infelizmente ocorreu uma falha na criação de seu arquivo, mil desculpas.')
                    return TelaInicial()
    else:
        print('Comando não identificado, por favor Digite apenas números')
        return TelaInicial()
            
def refaz(Lista, l2):
    if l2 == []:
        print('Não há nenhuma tarefa para ser refeita :)')
    else:
        listaTemp = l2.pop()
        Lista.append(listaTemp)
    
def Desfaz(lista, l2):
    if lista == []:
        print('Não há nenhuma tarefa para ser desfeita')
    else:
        listatemp = lista.pop()
        l2.append(listatemp)
    
def EscreveTxt(Var = 'Lista de Tarefas'):
    with open(f'{Var}' + '.txt', 'w+') as file:
        file.write('Sua lista de tarefas:\n')
        n = 1
        for n, tarefas in enumerate(lTarefas):
             if file.write(f'\t{n} - {tarefas}\n'):
                 return True
             else:
                 return False
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
    lListaTemp = []
    sTarefa = ''
    Apresentacao()  