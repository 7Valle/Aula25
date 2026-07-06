# pip install fastparquet

#import pandas as pd
import polars as pl  
from datetime import datetime

ENDERECO_DADOS = './../dados/bolsa_familia/'

try:
    inicio = datetime.now()

    # LENDO PARQUET - LEITURA "PREGUIÇOSA" SCAN_PARQUET


    # Polars 0:00:12.167821
    # scan_parquet gera um plano de execução. Não traz os dados.
    df_scan = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    #print(df_scan) # Printa o plano de execução


    # pré-processamento ...

    # Collect executa o plano, carregando os dados p/ a memória

    df_bolsa_familia = df_scan.collect()
    print(df_bolsa_familia.head())


    final = datetime.now()
    print(f'Tempo de execução de {final - inicio}')

except Exception as e:
    print(f'Erro ao ler parquet {e}')