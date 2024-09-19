import re

class Livro:
  def __init__(self, titulo: str, autor: str, exemplares: int):
    self.titulo = titulo
    self.autor = autor
    self.exemplares = exemplares

  def diminuirExem(self):
    self.exemplares -= 1

  def aumentarExem(self):
    self.exemplares += 1

  def __str__(self):
    return f'{self.titulo}, {self.autor}, {self.exemplares}'

class Leitor():
  def __init__(self, id_leitor: int, nome: str, livros_emprestados: list):
    self.id_leitor = id_leitor
    self.nome = nome
    self.livros_emprestados = livros_emprestados

  def adcLivro(self, Livro):
    self.livros_emprestados.append(Livro.titulo)

  def remLivro(self, Livro):
    self.livros_emprestados.remove(Livro.titulo)

  def __str__(self):
    if len(self.livros_emprestados) == 0:
      livros_str = 'Nenhum'
    else:
      livros_str = ', '.join(self.livros_emprestados)
    return f'ID: {self.id_leitor}, Nome: {self.nome}, Livros Possuídos: {livros_str}'


class Biblioteca:
  def __init__(self, estante, leitores):
    self.estante = estante
    self.leitores = leitores

  def adcLeitor(self, Leitor):
    self.leitores[Leitor.id_leitor] = Leitor

  def remLeitor(self, id):
    del self.leitores[id]

  def adcLivroEstante(self, Livro):
    self.estante[Livro.titulo] = Livro
    if Livro.exemplares >= 1:
      print()

  def remLivroEstante(self, titulo):
      del self.estante[titulo]

  def emprestarLivro(self, id_leitor, titulo_livro):
    leitor = self.leitores.get(id_leitor)
    livro = self.estante.get(titulo_livro)
    Leitor.adcLivro(leitor, livro)
    livro.diminuirExem()

  def devolverLivro(self, id_leitor, titulo_livro):
    leitor = self.leitores.get(id_leitor)
    livro = self.estante.get(titulo_livro)
    leitor.remLivro(livro)
    livro.aumentarExem()

  def leitoresDisplay(self):
    orderDict = dict(sorted(self.leitores.items()))
    for Leitor in orderDict.values():
      print(Leitor)

  def estanteDisplay(self):
    for Livro in self.estante.values():
      print(Livro)

  def checkDisp(self):
    disp = {}
    for Livro in self.estante:
      livrocheck = self.estante[Livro]
      if livrocheck.exemplares >= 1:
        disp[f'{livrocheck.titulo}'] = livrocheck
    return disp

  def checkEmpres(self):
    leitoresCLivros = {}
    for Leitor in self.leitores.values():
      if len(Leitor.livros_emprestados) >= 1:
        leitoresCLivros[Leitor.id_leitor] = Leitor
    return leitoresCLivros

  def __str__(self):
    return f'Estante: {self.estante}\nLeitores:{self.leitores}'

def getN(n): #PEGA UMA ENTRADA E VALIDA, PARAMETRO 'n' É O RANGE LIMITE
  while True:
    esc = input('Selecione uma opção: ')
    try:
      num = int(esc)
      if num > n or num == 0:
        print(f"[ERRO] não existe a opção {num}!")
      else:
        return num
    except ValueError:
      print('[ERRO] Por favor, insira um número válido.')

def getId():  #PEGA E VALIDA O ID
  while True:
    id = input('Digite o ID do usuário desejado: ')
    try:
      id = int(id)
      if id > 0:
        return id
      else:
        print('[ERRO] O ID do deve ser positivo!')
    except ValueError:
      print('[ERRO] Entrada inválida. Insira um ID válido!')

def getTitulo():  #PEGA E VALIDA O TITULO
  while True:
    titulo = input(str('Digite o titulo do livro: ')).strip()
    if titulo == '':
      print('[ERRO] Campo vazio!')
    elif len(titulo) > 115:
      print('[ERRO] Limite de 115 caracteres excedido!')
    else:
      return titulo

def getAutor():
  while True:
    autor = input(str('Digite o autor do livro: ')).strip()
    if autor == '':
      print('[ERRO] Campo vazio!')
    elif len(autor) > 30:
      print('[ERRO] Limite de 30 caracteres excedido!')
    else:
      return autor

def getExem():
  while True:
    exem = input('Digite a quantidade de exemplares: ')
    try:
      exem = int(exem)
      if exem >= 0:
        return exem
      elif exem > 999:
        print('[ERRO] Limite de 999 exemplares excedido!')
      else:
        print('[ERRO] A quantidade não pode ser negativa!')
    except ValueError:
      print('[ERRO] Entrada inválida. Insira uma quantidade válida')

def getNome():
  while True:
    nome =  input(str('Digite o nome do usuario: ')).strip()
    if bool(re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', nome)) == True:
      return nome
    elif nome == '':
      print('[ERRO] Campo vazio!')
    else:
      print('[ERRO] Entrada inválida. digite apenas letras e espaços!')

print('Bem vindo a biblioteca!!!')
menu ='''[MENU DE INTERAÇÃO]
[1] LIVROS
[2] LEITORES
[3] EMPRÉSTIMO / DEVOLUÇÃO
[4] SAIR'''
menuLivro ='''[LIVROS]
[1] VER
[2] ADICIONAR
[3] REMOVER
[4] VOLTAR'''
menuLeitores ='''[LEITORES]
[1] VER
[2] ADICIONAR
[3] REMOVER
[4] VOLTAR'''
menuAcoes ='''[DEVOLUÇÃO / EMPRÉSTIMO]
[1] EMPRÉSTIMO
[2] DEVOLUÇÃO
[3] SAIR'''

minhaBiblioteca = Biblioteca({},{})
Vitor = Leitor(1, 'Vitor', [])
Lucas = Leitor(2, 'Lucas', [])
DomCasmurro = Livro('Dom Casmurro', 'Machado de Assis', 3)
Diario = Livro('Diario de um Banana', 'Desconhecido', 3)
minhaBiblioteca.adcLeitor(Vitor)
minhaBiblioteca.adcLeitor(Lucas)
minhaBiblioteca.adcLivroEstante(DomCasmurro)
minhaBiblioteca.adcLivroEstante(Diario)
while True:
  print(menu)
  userInput =  getN(4)
  match userInput:
    case 1:  #MENU DE LIVROS
      while True:
        print(menuLivro)
        userInput = getN(4)
        match userInput:
          case 1:  #MENU DE LIVROS - VISUALIZAR LIVROS
            if len(minhaBiblioteca.estante) == 0:
              print('Não tem livros cadastrados!')
            else:
              print('TITULO / AUTOR / EXEMPLARES')
              minhaBiblioteca.estanteDisplay()

          case 2:  #MENU DE LIVROS -  ADICIONAR LIVROS
            titulo = getTitulo()
            autor = getAutor()
            exemplares = getExem()
            livro = Livro(titulo, autor, exemplares)
            minhaBiblioteca.adcLivroEstante(livro)

          case 3:  #MENU DE LIVROS - REMOVER LIVROS
            if len(minhaBiblioteca.estante) == 0:
              print('Não possui livros para serem removidos!')
            else:
              print('TITULO / AUTOR / EXEMPLARES')
              minhaBiblioteca.estanteDisplay()
              titulo = getTitulo()
              if titulo in minhaBiblioteca.estante:
                userInput = input(f'Tem certeza que deseja deletar o livro {titulo} ? [S/N]: ').upper()
                while userInput not in ['S','N']:
                    userInput = input(f'[ERRO] Tem certeza que deseja deletar o livro {titulo} ? [S/N]: ').upper()
                if userInput == 'S':
                  minhaBiblioteca.remLivroEstante(titulo)
                  print(f'Livro {titulo} deletado com sucesso!')
                elif userInput == 'N':
                  print('Ação cancelada!')
              else:
                print('Este livro não existe!')
          case 4:  #MENU DE LIVROS - SAIR MENU
            break

    case 2:  #MENU LEITORES
      while True:
        print(menuLeitores)
        userInput = getN(4)
        match userInput:
          case 1:  #MENU LEITORES - VISUALIZAR LEITORES
            if len(minhaBiblioteca.leitores) == 0:
              print('Não tem leitores cadastrados!')
            else:
              print('ID / NOME / LIVROS POSSUÍDOS')
              minhaBiblioteca.leitoresDisplay()

          case 2:  #MENU LEITORES - ADCIONAR LEITORES
            nome = getNome()
            if len(minhaBiblioteca.leitores) == 0:
              id = 1
            else:
              idList = sorted(minhaBiblioteca.leitores.keys())
              id = idList[-1] + 1
            livros_emprestados = []
            leitor = Leitor(id, nome, livros_emprestados)
            minhaBiblioteca.adcLeitor(leitor)
            print(f'O leitor {nome} cadastrado com sucesso, seu ID é: {id}')

          case 3:  #MENU LEITORES - REMOVER LEITORES
            if len(minhaBiblioteca.leitores) == 0:
              print('Não possui leitores para serem removidos!')
            else:
              print('ID / NOME / LIVROS POSSUÍDOS')
              minhaBiblioteca.leitoresDisplay()
              id = getId()
              if id in minhaBiblioteca.leitores:
                userInput = input(f'Tem certeza que deseja remover o leitor de ID {id} ? [S/N]: ').upper()
                while userInput not in ['S','N']:
                    userInput = input(f'[ERRO] Tem certeza que deseja remover o usuário {id} ? [S/N]: ').upper()
                if userInput == 'S':
                  leitorRem = minhaBiblioteca.leitores[id]
                  leitorRemLista =  leitorRem.livros_emprestados
                  for livroStr in leitorRemLista:
                    livroObj = minhaBiblioteca.estante[livroStr]
                    livroObj.aumentarExem()
                  minhaBiblioteca.remLeitor(id)

                  print(f'Leitor de ID {id} removido com sucesso!')
                elif userInput == 'N':
                  print('Ação cancelada!')
              else:
                print(f'O usuário de id {id} não existe!')
          case 4:
            break

    case 3:  #MENU EMPRÉSTIMO / DEVOLUÇÃO
      if len(minhaBiblioteca.estante) == 0:
        print('Você não tem livros cadastrados para isso!')
      elif len(minhaBiblioteca.checkDisp()) == 0:
          print('Você não tem livros disponiveis para isso')
      elif len(minhaBiblioteca.leitores) == 0:
        print('Você não tem leitores cadastrados para isso')
      else:
          print(menuAcoes)
          userInput = getN(3)
          match userInput:
            case 1:  #EMPRESTAR LIVRO
              disp = minhaBiblioteca.checkDisp()
              print('LIVROS DISPONVEIS:')
              print('TITULO / AUTOR / EXEMPLARES')
              for Livro in disp.values():
                print(Livro)
              titulo = getTitulo()
              while titulo not in disp:
                print('Este livro não existe ou não está disponivel!')
                titulo = getTitulo()
              print('ID / NOME / LIVROS POSSUÍDOS')
              minhaBiblioteca.leitoresDisplay()
              id = getId()
              while id not in minhaBiblioteca.leitores:
                print('Este usuário não existe!')
                id = getId()
              leitor = minhaBiblioteca.leitores[id]
              if titulo in leitor.livros_emprestados:
                print("O usuário já possui este livro!")
              else:
                minhaBiblioteca.emprestarLivro(id, titulo)
                print(f'O Livro: {titulo} foi emprestado com sucesso para o leitor de id: {id}')
            case 2:  #DEVOLVER LIVRO
              Empres = minhaBiblioteca.checkEmpres()
              if len(Empres) == 0:
                print('Não possui nenhum livro emprestado para devolução!')
              else:
                print('ID / NOME / LIVROS POSSUÍDOS')
                for Leitor in Empres.values():
                  print(Leitor)
                id = getId()
                while id not in Empres:
                  print('Este usuário não existe ou não possui livros emprestados!')
                  id = getId()
                leitorDevol = minhaBiblioteca.leitores[id]
                print(f'Livros que o usuário {leitorDevol.nome} possui:')
                for Livro in leitorDevol.livros_emprestados:
                  print(Livro)
                titulo = getTitulo()
                while titulo not in leitorDevol.livros_emprestados:
                  print('O usuário não possui esse livro, tente novamente!')
                  titulo = getTitulo()
                minhaBiblioteca.devolverLivro(id, titulo)
                print('O livro foi devolvido com sucesso!')
    case 4:
      print('PROGRAMA FINALIZADO...')
      break
