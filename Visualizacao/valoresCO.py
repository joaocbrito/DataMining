import pandas as pd
import statistics
import matplotlib.pyplot as plt

input_file = './Dataset/air-quality-clean.data'  # Importação dos Dados
df = pd.read_csv(input_file)
columns = list(df.columns)

coLista = df['CO(GT)'].tolist()
coListaOrdenado = sorted(df['CO(GT)'].tolist())

coMedia = df['CO(GT)'].mean()
coModa = df['CO(GT)'].mode()
coMediana = statistics.median(coLista)
coPontoMedio = (
    coListaOrdenado[0] + coListaOrdenado[len(coListaOrdenado)-1])/2

print("Tendência Central de monóxido de carbono (CO)")
print("Média = " + str(coMedia))
print("Moda = " + str(coModa[0]))
print("Mediana = " + str(coMediana))
print("Ponto Médio = " + str(coPontoMedio))

coAmplitude = coListaOrdenado[len(
    coListaOrdenado)-1] - coListaOrdenado[0]
coDesvioPadrao = statistics.pstdev(coLista)
coVariancia = statistics.pvariance(coLista)
coCoeficienteVariacao = (coDesvioPadrao/coMedia)*100

print("\nMedidas de dispersão de monóxido de carbono (CO)")
print("Amplitude = " + str(coAmplitude))
print("Desvio Padrão = " + str(coDesvioPadrao))
print("Variância = " + str(coVariancia))
print("Coeficiente de Variação = " +
      str(round(coCoeficienteVariacao, 2)) + "%\n")

co = df['CO(GT)']
co_descri = co.describe()

q1 = co_descri['25%']
mediana = co_descri['50%']
q2 = co_descri['75%']

s_q1 = "{0:.2f}".format(q1)
s_mediana = "{0:.2f}".format(mediana)
s_q2 = "{0:.2f}".format(q2)

font_1 = {'family': 'serif', 'color': 'darkred', 'size': '14'}

plt.figure(figsize=(6, 7))
plt.boxplot(co)
plt.title('Boxplot Air')
plt.text(1, q1, s_q1, fontdict=font_1)
plt.text(1, mediana, s_mediana, fontdict=font_1)
plt.text(1, q2, s_q2, fontdict=font_1)
plt.ylabel('Air')
plt.show()
