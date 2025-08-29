import sys
from pathlib import Path
import pandas as pd

def main():
    if len(sys.argv) < 2:
        print("Uso: python questao3.py <arquivo_csv> [--sep ';']")
        sys.exit(1)

    args = sys.argv[1:]
    sep = ","
    # parsing simples de --sep
    if "--sep" in args:
        i = args.index("--sep")
        try:
            sep = args[i + 1]
        except IndexError:
            print("Erro: informe um valor após --sep, ex.: --sep ';'")
            sys.exit(1)
        del args[i:i + 2]

    if not args:
        print("Uso: python questao3.py <arquivo_csv> [--sep ';']")
        sys.exit(1)

    csv_path = Path(args [0])
    if not csv_path.exists():
        print(f"Arquivo não encontrado: {csv_path}")
        sys.exit(1)

    # Lê o CSV respeitando o separador informado
    df = pd.read_csv(csv_path, sep=sep)

    # Exibe como tabela completa (sem cortar linhas/colunas)
    print("Conteúdo do CSV (tabela):")
    print(df.to_string(index=False))

    # Exibe linha a linha
    print("\nRegistros:")
    for _, row in df.iterrows():
        print(f"Nome: {row['Nome']}, Idade: {row['Idade']}, Cidade: {row['Cidade']}")

if __name__ == "__main__":
    main()
