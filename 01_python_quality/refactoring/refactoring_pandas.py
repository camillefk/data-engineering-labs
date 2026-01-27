### script_antigo.py
#import pandas as pd

### Lê o arquivo (caminho chumbado no código)
#df = pd.read_csv('vendas_brutas.csv')

### Remove linhas vazias na coluna 'valor'
#df = df.dropna(subset=['valor'])

### Calcula imposto de 15% (regra de negócio misturada)
#df['imposto'] = df['valor'] * 0.15

### Filtra apenas vendas altas
#df_final = df[df['valor'] > 1000]

### Salva
#df_final.to_csv('vendas_processadas.csv', index=False)
#print("Processamento concluído.")


#----REFATORAÇÃO----#


import pandas as pd
from typing import Optional
import os

#1. Primeiro eu tenho que definir a Exceção Customizada (To criando meu próprio erro, ajudando meu código a entender exatamente o que violou a regra de dados. Mais organizado assim).
class DataValidationError(Exception): 
    
    pass

#2. Função de carregamento
def load_data(filepath: str) -> pd.DataFrame:
    """Aqui to carregando os dados de um arquivo CSV.
    Args:
        filepath (str): O caminho para o arquivo CSV.
    Returns:
        pd.DataFrame: O DataFrame carregado contendo os dados brutos.
    Raises:
        FileNotFoundError: Se o arquivo não for encontrado no caminho especificado.
    """
    if not os.path.exists(filepath): 
        raise FileNotFoundError(f"O arquivo '{filepath}' não foi encontrado.")
    
    return pd.read_csv(filepath)

#3. Função Pura de transformação (Lógica Core)
def process_sales_data(df: pd.DataFrame, min_value: float= 1000.0) -> pd.DataFrame: 
    """Aqui processa os dados de vendas, vai limpa, calcular imposto e filtrar.
    Esta é uma função pura, ela não vai alterar o df original que foi recebido como argumento,
    mas retornar um novo df transformado. (^3^) ('-')

    Args:
        df (pd.DataFrame): DataFrame contendo colunas 'valor'.
        min_value (float): Valor mínimo para filtragem. Padrão é 1000.0.

    Returns:
        pd.DataFrame: Novo DataFrame processado com a coluna 'imposto'.

    Raises:
        DataValidationError: Se a coluna obrigatória 'valor' não existir.
    """
    #Validação de Schema (simples)
    required_cols = {'valor'} 
    if not required_cols.issubset(df.columns):
        missing = required_cols - set(df.columns)
        raise DataValidationError(f"Colunas obrigatórias ausentes: {missing}")
    
    #Aqui eu evito mutação do original
    df_processed = df.copy()

    #Limpezazinha
    df_processed = df_processed.dropna(subset=['valor'])

    #Regra de negóci0: cálculo do imposto de 15%
    TAX_RATE = 0.15
    df_processed['imposto'] = df_processed['valor'] * TAX_RATE
    #Eu limpei (tirei os valores nulos da coluna 'valor') salvei o resultado em df_processed e agora peguei a coluna 'valor' e multipliquei por 0.15 para ter o resultado dos impostos, salvando na coluna que criei chamada 'imposto'.

    #Filtragem
    df_processed = df_processed[df_processed['valor'] > min_value]
    
    return df_processed

#4. Função de Salvamento (efeito colateral)
def save_data(df: pd.DataFrame, output_path: str) -> None:
    """Salva o DataFrame processado em um arquivo CSV.
    Args:
        df (pd.DataFrame): O DataFrame a ser salvo.
        output_path (str): O caminho de destino.
    """
    df.to_csv(output_path, index=False)
    print(f"Dados salvos com sucesso em: {output_path}")

#5. Orquestração (main)
def main():
    INPUT_FILE = 'vendas_brutas.csv'
    OUTPUT_FILE = 'vendas_processadas.csv'

    # Criei um csv fictício apenas para testar o código
    try:
        pd.DataFrame({'id': [1, 2, 3], 'valor': [500.0, 1500.0, None]}).to_csv(INPUT_FILE, index=False)
    except Exception:
        pass

    try:
        
        print("Iniciando processamento...")
        
        raw_df = load_data(INPUT_FILE)
        
        # Aqui o erro customizado se o CSV estiver errado
        clean_df = process_sales_data(raw_df, min_value=1000.0)
        
        save_data(clean_df, OUTPUT_FILE)
        
    except DataValidationError as e:
        print(f"ERRO DE DADOS: {e}")
    except FileNotFoundError as e:
        print(f"ERRO DE ARQUIVO: {e}")
    except Exception as e:
        print(f"ERRO INESPERADO: {e}")

if __name__ == "__main__":
    main()