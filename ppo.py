'''Crie uma classe utilizando os conceitos de POO das aulas passadas.
Para criar sua classe, pense em uma entidade do mundo real que possa ser representada de maneira simples e objetiva. 
Por exemplo, uma classe "Pessoa" poderia ter atributos como nome, idade e endereço, e métodos como cumprimentar e se movimentar.
Já uma classe "Animal" poderia ter atributos como espécie, peso e altura, e métodos como andar e dormir.'''


class Pessoa:
    def __init__ (self, nome, idade, endereço):
        self.nome = nome 
        self.idade = idade
        self.endereço = endereço
    
    def cumprimentar(self):
        '''Pessoa um cumprimentou a pessoa dois'''
        return F'{primeira_pessoa.nome} cumprimentou {segunda_pessoa.nome}'
    def abraçar(self):
        '''Pessoa um abraçou a pessoa dois'''
        return F'{primeira_pessoa.nome} abraçou {segunda_pessoa.nome}'
    def correr(self):
        '''Começaram uma corrida'''
        return F'{primeira_pessoa.nome} correu junto com {segunda_pessoa.nome}'

nome1 = input('Digite o nome da primeira pessoa: ').capitalize()
idade1 = input('Digite a idade da primeira pessoa: ')
endereço1 = input('Digite o endereço da primeira pessoa: ').capitalize()

primeira_pessoa = Pessoa(nome1, idade1, endereço1 )

nome2 = input('Digite o nome da segunda pessoa: ').capitalize()
idade2 = input('Digite a idade da segunda pessoa: ')
endereço2 = input('Digite o endereço da segunda pessoa: ').capitalize()

segunda_pessoa = Pessoa(nome2, idade2, endereço2)


continuar = True

while continuar:
    escolha = input('Selecione qual ação deseja realizar. Tecle 1 para cumprimentar, 2 para abraçar, 3 para correr e 4 para finalizar o aplicativo: ')
    if escolha == '1':
        print(primeira_pessoa.correr())
    elif escolha == '2':
        print(primeira_pessoa.abraçar())
    elif escolha == '3':
        print(primeira_pessoa.cumprimentar())
    else:
        continuar = False 
        print('O aplicativo foi finalizado com sucesso. ')

'''print(primeira_pessoa.correr())
print(primeira_pessoa.abraçar())
print(primeira_pessoa.cumprimentar()) '''
