'''
2 - 
Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.
'''
import sys
from pathlib import Path
import pandas as pd

def main():
    # Parâmetros opcionais: nome do arquivo e separador
    # Uso: python questao2.py [arquivo_saida.csv] [--sep ';']
    out_name = "pessoas.csv"
    sep = ","

    args = sys.argv[1:]
    if args:
        # primeiro arg pode ser o nome do arquivo
        if not args.startswith("--"):
            out_name = args
            args = args[1:]
    if "--sep" in args:
        i = args.index("--sep")
        try:
            sep = args[i + 1]
        except IndexError:
            print("Erro: informe um valor após --sep, ex.: --sep ';'")
            sys.exit(1)

    # Dados de exemplo
    pessoas = [
        {"Nome": "Ana", "Idade": 28, "Cidade": "São Paulo"},
        {"Nome": "Bruno", "Idade": 34, "Cidade": "Rio de Janeiro"},
        {"Nome": "Carla", "Idade": 22, "Cidade": "Belo Horizonte"},
        {"Nome": "Diego", "Idade": 41, "Cidade": "Curitiba"},
        {"Nome": "Eva", "Idade": 30, "Cidade": "Porto Alegre"},
    ]

    df = pd.DataFrame(pessoas, columns=["Nome", "Idade", "Cidade"])
    out_path = Path(out_name)

    # Grava o CSV sem índice; encoding UTF-8 e newline correto no Windows
    df.to_csv(out_path, index=False, sep=sep, encoding="utf-8", lineterminator="\n")


    print(f"Arquivo criado: {out_path.resolve()} (sep='{sep}', colunas: {list(df.columns)})")

    print("\nPré-visualização dos dados:")
    print(df.to_string(index=False))

if __name__ == "__main__":
    main()
