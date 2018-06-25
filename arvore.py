# -*- coding:utf-8 -*-

class ArvoreDecisao:

    def __init__(self, nome_atributo = '', valor_atributo = '', filhos = []):
        self.pai = None
        self.nome_atributo = nome_atributo
        self.valor_atributo = valor_atributo
        self.filhos = filhos

        for filho in self.filhos:
            filho.pai = self

    def __str__(self):
        return self.nome_atributo


# Mostra a árvore
def printArvore(arvore, nivel=0):
    print  '<' + str(arvore.nome_atributo) + '>'
    for filho in arvore.filhos:
        print '        ' * nivel + '|' + str(filho.valor_atributo) + '|' + '________',
        printArvore(filho, nivel+1)
