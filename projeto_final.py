from abc import ABC, abstractmethod
from datetime import datetime



class Pessoa(ABC):
    @abstractmethod
    def remuneracao(self):
        pass

class Pedreiro():
   
   def __init__(self, nome):
      self.__bonus = 1
      # self.__diaria = 1
      self.qtd_trabalhadores = 0
      self.__nome = nome
      
   
   
   
   def count_trabalhadores(self):
      self.qtd_trabalhadores = int(input('Digite a quantidade de trabalhadores: '))
      if self.qtd_trabalhadores != 0:
         print(f'Temos {self.qtd_trabalhadores} trabalhando nessa obra.')
      elif self.qtd_trabalhadores == 0:
         print('O serviço foi concluido')
      else:
         print('Comando inválido.')
   
   
   @property
   def bonus(self):
      return self.__bonus

   @property
   def nome(self):
      return self.__nome
   
   @bonus.setter
   def bonus(self, bonus):
      try:
         self.__bonus = float(bonus)
      except:
         print('O valor do bonus não é está correto. Por favor insira um valor valido')

   # def adicionar_diaria(self, diaria):
   #    self.__diaria  += diaria
   # def reset_diaria(self):
   #    self.__diaria = 0
   
   
   #    salario_bruto = round((quantidade_horas_trabalhadas + minutos_em_decimal) * valor_por_hora, 2)
   #    ir = round(salario_bruto*11/100, 2)
   #    inss = round(salario_bruto*8/100, 2)

class Diaria:
   def __init__ (self):
      # self.valor = None
      self.inicio = 0
      self.pausa_almoco = 0
      self.fim_almoco = 0
      self.fim_expediente = 0
      self.va_hora = float(input("Digite o quanto você ganha por hora: "))
      self.ho_trabalhadas = int(input("Digite o número de horas trabalhadas no mês: "))
      self.m_trabalhados = int(input("Digite o número de minutos trabalhados no mês (além das horas): "))
      self.minutos_em_decimal = 0
      self.ir = 0
      self.inss = 0
      self.salario_bruto = 0
      self.salario_liquido = 0
      self.diaria = 1
   def iniciar_trabalho(self, inicio_expediente):
      self.inicio = datetime.strptime(inicio_expediente, '%H:%M' )
      
   def saida_almoco(self, saida_almoco):
      self.pausa_almoco = datetime.strptime(saida_almoco, '%H:%M' )

   def volta_almoco(self, volta_almoco):
      self.fim_almoco = datetime.strptime(volta_almoco, '%H:%M' )
   
   def encerrar_trabalho(self, fim_expediente):
      self.fim_expediente = datetime.strptime(fim_expediente, '%H:%M' )
     
         
   def horas_trabalhadas(self):
      alfa = (self.__fim_expediente - self.saida__almoco - self.volta__almoco - self.__inicio_expediente).seconds
      return round((alfa/60/60))
   
   def remuneracao(self):
         if self.diaria > 0:
            self.minutos_em_decimal = round(self.m_trabalhados / 60, 2)

            salario_bruto = round((self.ho_trabalhadas + self.minutos_em_decimal) * self.va_hora, 2)
            self.ir = round(salario_bruto*11/100, 2)
            self.inss = round(salario_bruto*8/100, 2)
            self.sindicato = round(salario_bruto*5/100, 2)
            self.salario_liquido = round(salario_bruto - self.ir -self.inss - self.sindicato, 2)

         print(f" + Salário Bruto : R$", salario_bruto)
         print(f" - IR (11%) : R$", {self.ir})
         print(f" - INSS (8%) : R$", {self.inss})
         print(f" - Sindicato (5%) : R$", {self.sindicato})
         print(f" = Salário Liquido : R$", {self.salario_liquido})
   @property
   def valor_hora(self):
      return self.valor_hora
   def adicionar_diaria(self, diaria):
      self.__diaria  += diaria
   def reset_diaria(self):
      self.__diaria = 0
   

p1 = Pedreiro('Negão do Concreto')

p1.bonus = 1.2
p1.count_trabalhadores()

d1 = Diaria()
d1.iniciar_trabalho('09:00')
d1.saida_almoco('13:00')
d1.volta_almoco('14:15')
d1.encerrar_trabalho('17:00')
#p1.adicionar_diaria() 

d1.remuneracao()