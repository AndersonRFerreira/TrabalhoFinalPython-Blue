from relogioPonto import UsuarioPonto, RelogioPonto
from abc import ABC, abstractmethod #importa a biblioteca abstrata do python
from datetime import datetime #importa a biblioteca datetime
from os import system
system('cls')

class Pessoa(): #a calsse pessoa recebe a classe abstrata
    class Pessoa:
      @abstractmethod # É um método de criação ou construtores que aceitam objetos da mesma classe ou interface que uma classe atual.
      def remuneracao(self): #função remuneração
        pass          #Método de definição de bloco, para interpretação de código do python.



# nome = str(input('Digite um nome: '))
# idade = int(input('Digite a idade: '))
# cpf = input('Digite o cpf: ')

class Pedreiro(Pessoa): #Um exemplo da classe autônoma.
   
   def __init__(self):#Função criada com método especial que sempre é executado quando criamos uma instância de um objeto .
      self.__bonus = 1      #Self parâmetro utilizado para invocar o objeto.
      self.qtd_trabalhadores = 0 #Objeto que lista a quantidade de trabalhadores.
      # self.__nome = nome = input('Digite o nome do Trabalhador: ') #Objeto que lista o nome do trabalhador.
      
   
   
   
   def count_trabalhadores(self): #função que define a quantidade de trabalhadores
        
            self.qtd_trabalhadores = int(input('Quantos profissionais irão atuar: '))# Esse objeto recebe um input perguntando quantos trbalhadores há no local.
            print()
            if self.qtd_trabalhadores != 0: #Laço condicional, onde, se a quantidade de trabalhadores for diferente de 0 ele me traz o print abaixo.
               print()
               print(f'Profissionais atuando. {self.qtd_trabalhadores}.') #Mostre na tela quantos trabalhadores estão atuando no serviço.
               print()
            elif self.qtd_trabalhadores <= 0:#Enquanto a quantidade de trabalhadores for igual a 0
               print()
               print('O serviço foi concluido')#Diga que o serviço ja foi concluido.
               print()
            else:
               print()
               print('Comando inválido.')# Se digitar um número não compatível com a condição retorne número inválido.
               
   @property #Método que se refencia a um atributo.
   def bonus(self): #função definir bonus, relativo as horas extras.
      return self.__bonus #Retorne para mim o objeto listado

   @property #Método que se refencia a um atributo.
   def nome(self): #função nome
      return self.__nome #Me retorne o objeto nome.
   
   @bonus.setter #Usei para fazer uma ligação feita com meu @property.
   def bonus(self, bonus):#função bonus, referente as horas extras trabalhadas.
      try:#Ele vai tentar pegar o parâmetro bonus, e convertê-lo para flot
         self.__bonus = float(bonus)#O try vai fazer o tratamento para que o self.bonus vire um float mesmo ele sendo um float.
      except:#qualquer execeção, ou seja, qualquer coisa que acontecer diferente do que o try pede, ele irá retornar o print abaixo.
         print('O valor do bonus não é está correto. Por favor insira um valor valido')

nome = str(input('Nome do trabalhador: '))
idade = int(input('Digite a idade: '))
cpf = input('Digite o cpf: ')
print()
contratante = str(input('Nome do contratante: '))
cpf2 = input('Digite o cpf: ')
class Diaria: #classe diária
   def __init__ (self):#Função criada com método especial que sempre é executado quando criamos uma instância de um objeto .
      self.nome = nome
      self.idade = idade
      self.cpf = cpf
      self.contratante = contratante
      self.cpf2 = cpf2
      self.inicio = 0
      self.pausa_almoco = 0
      self.fim_almoco = 0
      self.fim_expediente = 0
      self.va_hora = float(input("Digite o quanto ele ganha por hora: "))
      print()
      self.ho_trabalhadas = int(input("Quantidade de horas trabalhadas no mês: "))
      print()
      self.m_trabalhados = int(input("Quantidade minutos trabalhados no mês (hora extra): "))
      self.minutos_em_decimal = 0
      self.ir = 0
      self.inss = 0
      self.salario_bruto = 0
      self.salario_liquido = 0
      self.diaria = 1
   def iniciar_trabalho(self, inicio_expediente): #função que define o íncio da jornada de trabalho.
      self.inicio = datetime.strptime(inicio_expediente, '%H:%M' )
      
   def saida_almoco(self, saida_almoco):#função que define o horário de almoço
      self.pausa_almoco = datetime.strptime(saida_almoco, '%H:%M' )

   def volta_almoco(self, volta_almoco):#função que define o fim do horário de almoço.
      self.fim_almoco = datetime.strptime(volta_almoco, '%H:%M' )
   
   def encerrar_trabalho(self, fim_expediente):# função que define o fim do expediente. 
      self.fim_expediente = datetime.strptime(fim_expediente, '%H:%M' )
     
         
   def horas_trabalhadas(self):#função que irá calcular as horas trabalhadas.
      alfa = (self.__fim_expediente - self.saida__almoco - self.volta__almoco - self.__inicio_expediente).seconds
      return round((alfa/60/60))
   
   def remuneracao(self):# função que fará todo o calculo do salário, incluindo as taxas e as impimindo um holerith como parecido com uma nota fiscal paulista
         if self.diaria > 0:
            self.minutos_em_decimal = round(self.m_trabalhados / 60, 2)

            salario_bruto = round((self.ho_trabalhadas + self.minutos_em_decimal) * self.va_hora, 2)
            self.ir = round(salario_bruto*11/100, 2)
            self.inss = round(salario_bruto*8/100, 2)
            self.sindicato = round(salario_bruto*5/100, 2)
            self.salario_liquido = round(salario_bruto - self.ir -self.inss - self.sindicato, 2)
         print()
         print('Holerith')
         print()
         print(f'Dados do contratante')
         print(f'{self.contratante} portador do cpf {self.cpf2}')
         print()
         print('Dados do contratado')
         print(f'{self.nome} idade {self.idade} portador do cpf {self.cpf}')
         print('Nos dados abaxo contém, as informações sobre os descontos na sua folha de pagamento.')
         print()
         print(f'Total de horas trabalhadas = {self.ho_trabalhadas}')
         print(f" + Salário Bruto : R$", salario_bruto)
         print(f" - IR (11%) : R$", {self.ir})
         print(f" - INSS (8%) : R$", {self.inss})
         print(f" - Sindicato (5%) : R$", {self.sindicato})
         print(f" = Salário Liquido : R$", {self.salario_liquido})
         print()
         print('A informação contida neste documento é para uso único e exclusivo da pessoa a quem se destina.')
         print()
   @property
   def valor_hora(self):
      return self.valor_hora
   def adicionar_diaria(self, diaria):
      self.__diaria  += diaria
   def reset_diaria(self):
      self.__diaria = 0
   

p1 = Pedreiro()

p1.bonus = 1.2
p1.count_trabalhadores()

d1 = Diaria()
d1.iniciar_trabalho('09:00')
d1.saida_almoco('13:00')
d1.volta_almoco('14:15')
d1.encerrar_trabalho('17:00')


d1.remuneracao()