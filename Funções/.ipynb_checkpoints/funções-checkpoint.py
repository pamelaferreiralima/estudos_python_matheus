{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Sintaxe de uma função"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "35.49"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def my_function(x, y, z=1.5):\n",
    "    if z > 1:\n",
    "        return z * (x + y)\n",
    "    else:\n",
    "        return z / (x + y)\n",
    "    \n",
    "my_function(3.14,7,3.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def function(x):\n",
    "    x *= x/2\n",
    "    return x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(function(4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def func():\n",
    "    a = []\n",
    "    for i in range(5):\n",
    "        a.append(i)\n",
    "# após a função ser finalizada a lista a é destruída. (local)        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = []\n",
    "def func():\n",
    "    for i in range(5):\n",
    "        a.append(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def bind_a_variable():\n",
    "    global a\n",
    "    a = []\n",
    "\n",
    "bind_a_variable()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Devolvendo diversos valores "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def f():\n",
    "    a = 5\n",
    "    b = 6\n",
    "    c = 7\n",
    "    return {'a': a, 'b': b, 'c': c} # essa técnica pode vir a ser útil"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'a': 5, 'b': 6, 'c': 7}"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "states = ['Alabama', 'Geogia!', 'Georgia', 'geogira', 'FlORida', 'south carolina###', 'West virginia?']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_string(strings):\n",
    "    result = []\n",
    "    \n",
    "    for value in strings:\n",
    "        value = value.strip()\n",
    "        value = re.sub('[!#?]','', value)\n",
    "        value = value.title()\n",
    "        result.append(value)\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Alabama',\n",
       " 'Geogia',\n",
       " 'Georgia',\n",
       " 'Geogira',\n",
       " 'Florida',\n",
       " 'South Carolina',\n",
       " 'West Virginia']"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clean_string(states)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Como é bom estudar MAC0110!'"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = '\\n \\t \\v\\f Como é bom estudar MAC0110! \\n\\t\\n\\v'\n",
    "s_limpa = s.strip()\n",
    "s_limpa"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\n \\t \\x0b\\x0c Como é bom estudar MAC0110! \\n\\t\\n\\x0b'"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome To My World\n"
     ]
    }
   ],
   "source": [
    "txt = \"Welcome to my world\"\n",
    "x = txt.title()\n",
    "print(x)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Podemos criar uma função para remover em um conjunto particular\n",
    "\n",
    "def remove_punctuation(value):\n",
    "    return re.sub('[!#?]', '', value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "clean_ops = [str.strip, remove_punctuation, str.title]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_string(strings, ops):\n",
    "    result = []\n",
    "    for value in strings:\n",
    "        for function in ops:\n",
    "            value = function(value)\n",
    "        result.append(value)\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Alabama',\n",
       " 'Geogia',\n",
       " 'Georgia',\n",
       " 'Geogira',\n",
       " 'Florida',\n",
       " 'South Carolina',\n",
       " 'West Virginia']"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clean_string(states, clean_ops)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Alabama\n",
      "Geogia\n",
      "Georgia\n",
      "geogira\n",
      "FlORida\n",
      "south carolina\n",
      "West virginia\n"
     ]
    }
   ],
   "source": [
    "for x in map(remove_punctuation, states):\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Funções Anônimas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "32"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def short_function(x):\n",
    "    return x * 2\n",
    "short_function(16)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "32"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "equiv_anon = lambda x: x * 2\n",
    "equiv_anon(16)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "def apply_to_list(some_list, f):\n",
    "    return [f(x) for x in some_list]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "ints = [ 4, 0, 1, 5, 6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[8, 0, 2, 10, 12]"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "apply_to_list(ints, lambda x:x*2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[8, 0, 2, 10, 12]"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[x * 2 for x in ints]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[x ** 2 for x in range(11)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['aaaa', 'foo', 'abab', 'bar', 'card']"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Ordernar uma coleção de strings de acordo com o numero de letras distintas em cada string:\n",
    "\n",
    "strings = ['foo', 'card', 'bar', 'aaaa', 'abab']\n",
    "\n",
    "strings.sort(key=lambda x: len(set(list(x))))\n",
    "strings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
  },
  "vscode": {
   "interpreter": {
    "hash": "369f2c481f4da34e4445cda3fffd2e751bd1c4d706f27375911949ba6bb62e1c"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
