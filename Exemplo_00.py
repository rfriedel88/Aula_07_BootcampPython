## Criando Funções em Python

print ("Esse é meu print")



def soma(valor_1:float,valor_2:float)->float:
    """
    Uma função simples que recebe dois valores float e retorna a soma deles.
    parâmetros: Valor_1, Valor_2
    retorno: float com a soma dos valores
    """
    resultado_soma= valor_1 + valor_2
    return resultado_soma



Valor3=soma(1,2)
print(Valor3)
