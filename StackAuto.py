import sys

# Classe implementada para simular a fita de entrada e a pilha do automato
class Pilha():

  def __init__(self, conteudo):
    self.conteudo = conteudo

  def isEmpty(self):
    if (len(self.conteudo)):
      return 0
    else:
      return 1

  # Retorna o conteudo da pilha / fita
  def content(self):
    return self.conteudo

  # Confere se o conteudo é condizente com o topo da pilha / fita
  def isTop(self, conteudo):
    length = len(conteudo)
    # quantos caracteres irão ser comparados
    return (False) if (len(self.conteudo) < length) else (self.conteudo[0:length] == conteudo)
    # retorna falso, se conteudo da pilha for menor que o conteudo comparado ou diferente dele
  
  # Desempilha valor antigo e empilha o novo independente de ser valor vazio
  def alterTop(self, old, new):
    if (self.isTop(old)):
      self.conteudo = self.conteudo.replace(old, new, 1)
    # desempilha o valor antigo e empilha o novo valor no lugar

  pass

class Transicao():

  # Inicializa a transição
  def __init__(self, transicao, estado, estados, simbVazio):
    data = transicao.split()

    self.estado = estado
    self.novoEstado = data[3]
    self.entrada = "" if(simbVazio == data[1]) else data[1]
    for state in estados:
      if(self.novoEstado == state.getCod()):
        self.novoEstado = state
        break
    self.PValor = "" if(simbVazio == data[2]) else data[2]
    self.novoPValor = "" if(simbVazio == data[4]) else data[4]
    pass

  # Valida a transição de acordo com o topo da pilha e da entrada
  def validacao(self, entrada, pilha):
    if(entrada.isTop(self.entrada)):
      if(pilha.isTop(self.PValor)):
        return True
    return False

  # Executa a transição e retorna o novo estado
  def executa(self, entrada, pilha):
    if(self.validacao(entrada, pilha)):
      entrada.alterTop(self.entrada, '')
      pilha.alterTop(self.PValor, self.novoPValor)
      return self.novoEstado
    return 0
  
  pass

class Estado():

  # inicializa o estado sem suas transições
  def __init__(self, cod, fStates):
    self.cod = cod
    self.final = False
    for fS in fStates:
      if(fS == self.cod):
        self.final = True
        break
    self.transicoes = []
    pass

  # Gera as transições relacionadas ao estado
  def mount(self, transacoes, estados, simbVazio):
    for tr in transacoes:
      if(tr.split()[0] == self.cod):
        self.transicoes.append(Transicao(tr, self, estados, simbVazio))
    pass
  
  # Retorna lista com os indices das transições validas no momento
  def trans(self, entrada, pilha):
    vet = []
    count = 0
    for tr in self.transicoes:
      if (tr.validacao(entrada, pilha)):
        vet.append(count)
      count += 1
    return vet

  # Executa uma transição especifica do estado
  def exeSpec(self, posicao, entrada, pilha):
    if(posicao >= 0 and posicao < len(self.transicoes)):
      return self.transicoes[posicao].executa(entrada, pilha)

  def getCod(self):
    return self.cod
  
  def isFinal(self):
    if(self.final):
      return 1
    return 0

  pass

# Classe implementada para simular a configuração instantanea do automato
class Automato():

  # Inicializa o automato com entrada, pilha e estado inicial / atual
  def __init__(self, entrada, pilha, estado):
    self.entrada = Pilha(entrada)
    self.pilha = Pilha(pilha)
    self.estado = estado
    pass

  # Retorna um vetor com os indices das transições validas no momento
  def transicoes(self):
    return self.estado.trans(self.entrada, self.pilha)

  # Executa uma transição no automato se ainda não estiver em posição de aceitação
  def executa(self, trans):

    # Retorna 2 se aceitar por pilha vazia ou estado final
    if(self.entrada.isEmpty()):
      if(self.estado.isFinal() or self.pilha.isEmpty()):
        return 2
    
    # Retorna 0 se não ouver transições disponíveis
    if(len(trans) == 0):
      return 0
    
    # Executa a primeira transição disponível e altera o estado
    novoEstado = self.estado.exeSpec(trans[0], self.entrada, self.pilha)
    self.estado = novoEstado
    return 1

  # Duplica a configuração atual do automato
  def duplica(self):
    return Automato(self.entrada.content(), self.pilha.content(), self.estado)
  
  # Exibe a configuração instantânia do automato
  def print(self):
    print('Entrada: ', self.entrada.content())
    print('Pilha: ', self.pilha.content())
  
  pass

def lerArquivo (arquivo):
  arq = open(arquivo, 'r')
  conteudo = arq.read().split('\n')

  simbVazio = conteudo[2].split()[0]
  #print(simbVazio)
  pilhaInit = conteudo[3].split()[0]
  #print(pilhaInit)
  conjEstados = conteudo[4].split()
  #print(conjEstados)
  iniEstado = conteudo[5].split()[0]
  #print(iniEstado)
  finEstados = conteudo[6].split()
  #print(finEstados)
  transicoes = conteudo[7:]
  if(transicoes[-1] == ''):
    transicoes.pop()
  #print(transicoes)
  arq.close()
  return [simbVazio, pilhaInit, conjEstados, iniEstado, finEstados, transicoes]

def main(arquivo, entrada):

  # Le o arquivo e retorna os dados
  estrutura = lerArquivo(arquivo)

  # Separa os dados lidos do arquivo
  simbVazio = estrutura[0]
  pilhaInit = estrutura[1]
  conjEstados = estrutura[2]
  estadoInicial = estrutura[3]
  estadosFinais = estrutura[4]
  transicoes = estrutura[5]

  estados = []

  # Gera os estados
  for states in estrutura[2]:
    estados.append(Estado(states, estadosFinais))
    # Se for igual ao estado inicial atribui a variavel
    if(estadoInicial == states):
      estadoIni = estados[-1]
  
  # Monta os estados com as transições
  for estado in estados:
    estado.mount(transicoes, estados, simbVazio)

  automatos = []
  
  # Gera a configuração inicial do automato
  automatos.append(Automato(entrada, pilhaInit, estadoIni))

  # Variáveis auxiliares
  concluido = 0
  tam = 1

  # Executa o(s) automato(s) até encontrar um resultado
  while(concluido == 0 and tam > 0):
    concluido = 1
    tam = len(automatos)
    i = 0 # indice de trabalho
    while (i < tam):
      # Recebe um vetor com os indices das transições validas para o momento
      trans = automatos[i].transicoes()
      if(len(trans) > 1):
        # Duplica o automato, executa a duplicata e adiciona ela ao vetor de automatos
        for j in range (1, len(trans)):
          aux = automatos[i].duplica()
          res = aux.executa(trans[j:])
          automatos.append(aux)
      res = automatos[i].executa(trans)
      # Analisa a saida da execução, finaliza a execução atual se necessario,
      # finaliza o processo de executar os automatos
      # ou simplesmente continua
      if(res == 2):
        concluido = 1
        break

      elif(res == 1):
        concluido = 0
      
      else:
        concluido = 0
        if(tam > 1):
          automatos.pop(i)
          i -= 1
          tam -= 1
        else:
          concluido = 1
          break
      i += 1
  
  # Retorna uma saida para o usuario de acordo com o resultado das execuções
  if(res == 2):
    print(0)
    automatos[i].print()
  
  elif(res == 0):
    print(1)
    automatos[0].print()
  
  else:
    automatos[0].print()




if __name__ == "__main__":
  # cancela a execução se o numero de argumentos não for correto
  if(len(sys.argv) != 3):
    print("Parametros insuficientes. Informe o nome do arquivo de entrada e a palavra de entrada")
    sys.exit(1)
  main(sys.argv[1], sys.argv[2])