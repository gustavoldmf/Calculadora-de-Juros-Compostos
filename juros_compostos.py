# Arquivo para criação de Gráficos simples
# com as bibliotecas numpy e matplotlib.pyplot

import numpy as np
import matplotlib.pyplot as plt

#defines
INT_TEMPO = 6
INTERVALOS = 6

# Declaração das variáveis globais
t = 0
Total_investido = 0
Juros_total = 0
lista = [None]
it = 0


#a função x calcula o aporte mensal de acordo com a quantidade de meses avaliados 
def x_n(aporte_mensal):
    return aporte_mensal

# Função que calcula o rendimento utilizando juros compostos por meio 
# de uma recurção
def y_n(  valor_inicial, taxa,aporte_mensal,n):
    valor_final = 0
    if(n==0):
        return valor_inicial

    valor_final = (1+(taxa/100))*y_n( valor_inicial, taxa,aporte_mensal,n-1) + x_n(aporte_mensal)
    return valor_final

def Calcula_Total_Mensal(valor_inicial,taxa, aporte, num_meses):
    global lista
    global t
    t = np.linspace(0, num_meses, num_meses+1)
    it = range(num_meses+1)
    lista = [None]*(num_meses+1)

    for item in it:
        lista[item] = y_n(valor_inicial,taxa,aporte,item)

#função que obtem o total de Dinheiro aplicado e juros de rendimento
def Resultado_investimento(num_meses,aporte_mensal):
    global Juros_total
    global Total_investido
    Total_investido = num_meses*aporte_mensal
    Juros_total = lista[num_meses] - Total_investido
    return 0


print("Seja bem vindo ao meu protótipo de Calculadora de Juros\n")
print("Aqui é possível fazer um projeção financeira com capital inicial, aportes mensais e rentabilidade\n")
print("Após preencher os dados será calculado o total investido, juros acumulados e um gráfico evolutivo\n")

entrada = [None]*4
entrada[0] = int(input("Digite o valor inicial: "))
entrada[1] = int(input("Digite a rentabidade do investimento em porcento por mes: "))
entrada[2] = int(input("Digite o valor dos aportes mensais: "))
entrada[3] = int(input("Digite durante quantos meses o dinheiro será investido: "))


Calcula_Total_Mensal(entrada[0],entrada[1],entrada[2],entrada[3])
Resultado_investimento(12,200)

print(f"\n\nTotal de Dinheiro Aplicado: R${Total_investido:.2f}",f"\nJuros Totais: R${Juros_total:.2f}")
print(f"Valor Final da Reserva: R${(Total_investido+Juros_total):.2f}")


# Criar os gráficos
plt.figure(figsize=[10,10])

# Gráfico de sinal_x e sinal_y
sinal_x = t
sinal_y = lista
teste = plt.stem(sinal_x, sinal_y, basefmt=" ")
plt.title('Investimento')
plt.xlabel('Tempo em meses')
plt.ylabel('Valor')

plt.axhline(0, color='black',linewidth=0.5, ls='--')  # Linha do eixo x
plt.axvline(0, color='black',linewidth=0.5, ls='--')  # Linha do eixo y

# Ajustar layout e mostrar o gráfico
plt.tight_layout()
plt.show()


