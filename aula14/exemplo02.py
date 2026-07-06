# pip install fastparquet

#import pandas as pd
import polars as pl  
from datetime import datetime

ENDERECO_DADOS = './../dados/bolsa_familia/'

try:
    inicio = datetime.now()


    # Lendo Parquet - Leitura Direta
    # Pandas 0:00:24:20
    #df_bolsa_familia = pd.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    # Polars 0:00:07.77
    df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')


    print(df_bolsa_familia.head())
    final = datetime.now()
    print(f'Tempo de execução de {final - inicio}')

except Exception as e:
    print(f'Erro ao ler parquet {e}')