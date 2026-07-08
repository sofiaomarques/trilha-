class Livro:
    def __init__(self, titulo, autor, paginas, paginas_lidas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.paginas_lidas = paginas_lidas

    def ler (self, quantidade):
        self.paginas_lidas += quantidade

    def progresso(self):
        print( f"Porcentagem lida: {self.paginas_lidas/self.paginas*100}%")
        




class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base 
    def calcular_salario(self):
        return self.salario_base


class Gerente(Funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)
    def calcular_salario(self):
        print(self.salario_base+1000)
        return


class Vendedor(Funcionario):
    def __init__ (self,nome, salario_base, vendas):
         super().__init__(nome, salario_base)
         self.vendas = vendas 
    def calcular_salario(self):
        return self.salario_base+ self.vendas*0.1


f1 = Gerente("Sofia", 40000)
#print(f"A gerente {f1.nome} recebe R${f1.calcular_salario()}.")
#print(f1.calcular_salario())
f1.calcular_salario()



f2 = Vendedor("Todaro", 150, 67)
#print(f"O vendedor {f2.nome} recebe R${f2.calcular_salario()}.")
print(f2.calcular_salario())







