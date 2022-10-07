{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "afadb104",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Stack:\n",
    "    def __init__(self):\n",
    "        self.itens = []\n",
    "        \n",
    "    def is_empty(self):\n",
    "        return self.itens == []\n",
    "    \n",
    "    def pop(self):\n",
    "        return self.itens.pop()\n",
    "    \n",
    "    def push(self, item):\n",
    "        self.itens.append(item)\n",
    "        \n",
    "    def peek(self):\n",
    "        return self.itens[len(self.itens) - 1]\n",
    "    \n",
    "    def size(self):\n",
    "        return len(self.itens)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db1a8a58",
   "metadata": {},
   "outputs": [],
   "source": [
    "(0,5) Escreva um programa para ler uma frase e imprimi-la com as letras das \n",
    "palavras invertidas. Exemplo: a frase “a pilha do gato” deve sair “a ahlip od \n",
    "otag”."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "7f71bdce",
   "metadata": {},
   "outputs": [],
   "source": [
    "def palavra_invertida(palavra):\n",
    "    \n",
    "    op_palavra = Stack()\n",
    "    \n",
    "    valores = [] # vai receber as letras retiradas da pilha\n",
    "   \n",
    "    token_list = palavra.split()\n",
    "    \n",
    "    for token in token_list:\n",
    "        \n",
    "        if token >= 'ABCDEFGHIJKLMNOPQRSTUVXYW':\n",
    "            op_palavra.push(token)\n",
    "            # print(op_palavra)\n",
    "        else:\n",
    "            valores.append(op_palavra.pop())\n",
    "            break\n",
    "        \n",
    "            \n",
    "    while not op_palavra.is_empty():\n",
    "        valores.append(op_palavra.pop())\n",
    "        #print(valores)\n",
    "        \n",
    "    return \"\\n\".join(valores) # "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "a4b84fb9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a\n",
      "m\n",
      "o\n",
      "r\n"
     ]
    }
   ],
   "source": [
    "print(palavra_invertida(\"r o m a\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cbef61a7",
   "metadata": {},
   "source": [
    "(0,25) Escreva um programa que usa Pilha para verificar se uma dada cadeia decaracteres é ou não palíndroma. Por exemplo: “subinoonibus” é palíndroma."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b9d59cd7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def palavra_palindroma(palavra):\n",
    "    palavra_teste = Stack()\n",
    "    token_list = palavra.split()\n",
    "    \n",
    "    for i in token_list:\n",
    "        if i in 'abcdefghijklmnopqrstuvwxyz':\n",
    "            palavra_teste.push(i)\n",
    "            print(i)\n",
    "        \n",
    "        while (not palavra_teste.is_empty() and (palavra[::-1] == palavra_teste)):\n",
    "            print(True)\n",
    "        print('Desculpa, essa palavra não é palindroma') # mostra primeiro que não é palindroma\n",
    "        # até confirmar a palavra completamente\n",
    "    return palavra == palavra[::-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "5263477a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Desculpa, essa palavra não é palindroma\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "print(palavra_palindroma(\"gato\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7c225631",
   "metadata": {},
   "source": [
    "(0,25) Mostre a situação da Pilha P, inicialmente vazia, após a execução de cadauma das operações a seguir:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1db28069",
   "metadata": {},
   "outputs": [],
   "source": [
    "p.push('a') # adiciona 'a' na pilha\n",
    "p.push('b') # adiciona 'b' na pilha\n",
    "p.push('c') # adiciona 'c' na pilha\n",
    "p.push(p.peek()) # adiciona 'c' na pilha\n",
    "p.push('d') # adiciona 'd' na pilha\n",
    "p.pop() # remove 'd' da pilha\n",
    "p.pop() # remove 'c' da pilha\n",
    "\n",
    "# Portanto p = [a, b, c]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
