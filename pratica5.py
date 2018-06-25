# -*- coding:utf-8 -*-

import arvore
import numpy as np
import math

# Retorna um novo conjunto de dados com todos os elementos daquele tipo
def getAtributos(data, coluna, valor):
    atributos = []
    for linha in data:
        if linha[coluna] == valor:
            atributos.append(linha)

    return np.array(atributos)

#Calcula a entropia de um atributo
def calcularEntropia(data, coluna_atributo, valores_atributo, coluna_classe, valores_classe ):
    valor_atributo = []
    ocorrencias = []
    tamanho = float(len(data))

    for valor in valores_classe:
        ocorrencias.append(getAtributos(data, coluna_classe, valor))

    for valor in valores_atributo:
        probrabilidades = []
        atributo = getAtributos(data,coluna_atributo, valor)
        probOcorrencia = len(atributo)/tamanho
        probrabilidades.append(probOcorrencia)
        for elemento in ocorrencias:
            tamanho_atributo = float(len(atributo))
            if tamanho_atributo != 0:
                qtd_ocorre = len(getAtributos(elemento, coluna_atributo, valor))
                probrabilidades.append(qtd_ocorre/tamanho_atributo)
            else:
                pass
        valor_atributo.append(tuple(probrabilidades))

    entropia = 0
    for elemento in valor_atributo:
        somaElemento = 0
        for i in range(1,len(elemento)):
            if elemento[i] != 0:
                somaElemento += elemento[i]*math.log(elemento[i], 2)
        entropia += elemento[0]*somaElemento
    return -entropia

# Faz uma verificação para saber se é folha 
def isFolha(data, coluna):
    a_inicial = data[0,coluna]
    folha = True
    for linha in data:
        if linha[coluna] != a_inicial:
            return not folha
    return a_inicial

# Construindo a árvore
def construirArvore(data, colunaClasse, valoresClasse, valoresAtributos, atributos, valorAtributo=None):
    entropias = []
    folha = isFolha(data, colunaClasse)
    if folha:
        return arvore.ArvoreDecisao(nome_atributo=valoresClasse[folha], valor_atributo=valorAtributo)

    for i in atributos:
        entropias.append(calcularEntropia(data, i, valoresAtributos[i], colunaClasse, valoresClasse))

    coluna_atributo = entropias.index(min(entropias))
    filhos = []
    for valor in valoresAtributos[coluna_atributo]:
        dados = getAtributos(data, coluna_atributo, valor)
        if dados.size != 0:
            f = construirArvore(dados, colunaClasse, valoresClasse, valoresAtributos, atributos, valor)
            filhos.append(f)

    return arvore.ArvoreDecisao(nome_atributo=atributos[coluna_atributo], valor_atributo=valorAtributo, filhos=filhos)

# Função principal
def main():
    data = np.genfromtxt("frutas", delimiter=",")
    # Referente a classe RISCO
    colunaClasse = 4
    #Valores possíveis da classe para classificação
    valoresClasse = {-1: "Baixo", 1: "Alto"}
    #Para cada atributo define sua quantidade e seus valores possiveis
    valoresAtributos = [[-1,1], [-1,0,1], [-1,1], [-1,1]]
    atributos = {0 : 'CASCA', 1 : 'COR', 2 : 'TAMANHO', 3 : 'POLPA'}

    arvore_decisao = construirArvore(data, colunaClasse, valoresClasse, valoresAtributos, atributos)
    arvore.printArvore(arvore_decisao)

if __name__ == "__main__":
    main()





