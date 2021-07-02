import pandas as pd
import matplotlib.pyplot as plt

input_file = './Dataset/air-quality-clean.data'  # Importação dos Dados
df = pd.read_csv(input_file, usecols=[
                 'CO(GT)', 'NO2(GT)'])
nitrogenio = df['NO2(GT)'].tolist()
pulso = df['CO(GT)'].tolist()
resultado = df['NO2(GT)'].value_counts(sort=True)
print(resultado)
labels = 'Boa', 'Moderada', 'Ruim'

plt.title('Qualidade do ar CO(GT)')
plt.xlabel('Qualidade do ar')
plt.ylabel('Quantidade')
plt.hist(nitrogenio, 15, rwidth=0.9, edgecolor='black')

plt.show()

plt.title('CO(GT) qualidade do ar')
plt.xlabel('CO(GT)')
plt.ylabel('Quantidade')
plt.hist(pulso, 15, rwidth=0.9, edgecolor='black')

plt.show()

plt.title("NO2(GT)")
plt.pie(resultado, labels=labels, autopct='%1.1f%%')
plt.show()
