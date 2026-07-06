# pip install fastparquet

#import pandas as pd
import polars as pl  
from datetime import datetime

ENDERECO_DADOS = './../dados/bolsa_familia/'

try:
    inicio = datetime.now()

    # LENDO PARQUET - LEITURA "PREGUIÇOSA" SCAN_PARQUET

    # Métodos que geram o plano de execução (.lazy() e .scan_parquet())
    
    #lazy_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet').lazy()
  
    lazy_bolsa_familia = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    #print(lazy_bolsa_familia) # Imprimindo o plano de execução
    
    lazy_bolsa_familia = lazy_bolsa_familia.select([
        'NOME MUNICÍPIO', 'VALOR PARCELA'
    ])



    lazy_bolsa_familia = lazy_bolsa_familia.group_by(
        'NOME MUNICÍPIO'
    ).agg(
        pl.col('VALOR PARCELA').sum()
    )



    lazy_bolsa_familia = lazy_bolsa_familia.sort(by='VALOR PARCELA', descending=True)

    df_bolsa_familia = lazy_bolsa_familia.collect() # carrega os dados

    print(df_bolsa_familia.head())



    final = datetime.now()
    print(f'Tempo de execução de {final - inicio}')

except Exception as e:
    print(f'Erro ao ler parquet {e}')