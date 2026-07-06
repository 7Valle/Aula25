#import pandas as pd
import polars as pl  # biblioteca de manipulação de dados em larga escala
from datetime import datetime  # trabalhar com o tempo
import os


ENDERECO_DADOS = './../dados/bolsa_familia/'

try:
    inicio = datetime.now()
    print('Carregando...')

    df_bolsa_familia = None
    lista_arquivos = []

    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)

    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)
        
    # print(lista_arquivos)

    for nome in lista_arquivos:
        print(f'Processando o arquivo {nome}')

        # Pandas  0:05:38.998941 
        # df = pd.read_csv(ENDERECO_DADOS + nome, sep=';', encoding='iso-8859-1')

        # Polars  0:00:39.078643
        df = pl.read_csv(ENDERECO_DADOS + nome, separator=';', encoding='iso-8859-1')

        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])

        del df  # liberar memóira

    
        print(f'Arquivo {nome} processador sucesso!')
        print(df_bolsa_familia.head())

    # print(df_bolsa_familia.columns)
    # print(df_bolsa_familia.shape)


    # Converter a série valor parcela
    df_bolsa_familia = df_bolsa_familia.with_columns(
        pl.col('VALOR PARCELA').str.replace(',','.').cast(pl.Float64)
    )

    print('Iniciando a gravação do arquivo parquet...')
    df_bolsa_familia.write_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    print('\nGravação do arquivo parquet concluída com sucesso!')
    print(df_bolsa_familia.head())
    print(df_bolsa_familia.columns)
    print(df_bolsa_familia.shape)

    final = datetime.now()
    print(f'Tempo de execução de {final - inicio}')

    
except Exception as e:
    print(f'Erro ao obter os dados {e}')