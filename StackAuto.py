import sys

class Pilha():

  def __init__(self, conteudo):
    self._conteudo = conteudo

  def isEmpty(self):
    return False if (len(self._conteudo)) else True

  def isTop(self, conteudo):
    length = len(conteudo)
    ## quantos caracteres irão ser comparados
    return (False) if (len(self._conteudo) < length) else (self._conteudo[0:length] == conteudo)
    ## retorna falso, se conteudo da pilha for menor que o conteudo comparado ou diferente dele
  
  def alterTop(self, old, new):
    if (self.isTop(old)):
      self._conteudo = self._conteudo.replace(old, new, 1)
    ## desempilha o valor antigo e empilha o novo valor no lugar

  def print(self):
    print(self._conteudo)
    ## exibe o conteudo da pilha

  pass

class Transicao():

  pass

class Stado():

  pass

class Maquina():

  pass

def lerArquivo(arquivo):

  pass


def main():

  pil = Pilha('ola Mundo')

  print(pil.isTop('ola'))

  pil.alterTop('ola Mund', '')

  pil.print()

if __name__ == "__main__":
  main()