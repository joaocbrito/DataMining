import pandas as pd
import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    input_file = './dataset/AirQualityUCI.csv'  # Importação dos Dados
    df = pd.read_csv(input_file, sep=',', na_values='-200')  

    del(df['Date'])
    del(df['Time'])

    print(df.info())

    for campo in df.columns:  # Percorre a lista das colunas que estão sendo utilizadas
        # Substituindo valores ausentes pela média
        mean = round(df[campo].mean(), 1)
        df[campo].fillna(mean, inplace=True)

    # Gera um arquivo com os todos os dados preenchidos pelo algoritmo
    df.to_csv('./dataset/air-quality-clean.data', index=False)

    # print(df.info())

if __name__ == "__main__":
    main()
