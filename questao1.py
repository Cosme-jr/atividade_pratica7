import sys
from pathlib import Path
import pandas as pd

def infer_time_column(cols):
    """Detecta a coluna de tempo por nomes comuns."""
    candidates = [
        "tempo_execucao_ms", "tempo_execucao_s",
        "duration_ms", "duration_s",
        "tempo", "time"
    ]
    cols_lower = {c.lower(): c for c in cols}
    for c in candidates:
        if c in cols_lower:
            return cols_lower[c]
    return None

def load_times_from_csv(path: Path, sep=None):
    # Lê CSV; se sep não for informado, deixa o pandas inferir.
    read_kwargs = {}
    if sep is not None:
        read_kwargs["sep"] = sep
    df = pd.read_csv(path, **read_kwargs)
    col = infer_time_column(df.columns)
    if not col:
        raise ValueError(f"Não encontrei coluna de tempo nas colunas: {list(df.columns)}")
    s = pd.to_numeric(df[col], errors="coerce").dropna()
    # Normaliza para segundos se a coluna terminar com _ms.
    if col.lower().endswith("_ms"):
        s = s / 1000.0
    return s

def load_times_from_txt(path: Path):
    # Cada linha deve conter um valor de tempo (ex.: "120", "150ms" ou "1.5s").
    vals = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            clean = line.lower().replace("ms", "").replace("s", "")
            try:
                vals.append(float(clean))
            except ValueError:
                # Ignora linhas inválidas
                pass
    return pd.Series(vals, name="tempo_execucao_s")

def main():
    if len(sys.argv) < 2:
        print("Uso: python questao1.py <caminho_arquivo_log> [--sep ';']")
        sys.exit(1)

    sep = None
    args = sys.argv[1:]

    if "--sep" in args:
        i = args.index("--sep")
        try:
            sep = args[i + 1]
        except IndexError:
            print("Erro: informe um valor após --sep, ex.: --sep ';'")
            sys.exit(1)

    if not args:
        print("Uso: python questao1.py <caminho_arquivo_log> [--sep ';']")
        sys.exit(1)

    path = Path(args[0])
    if not path.exists():
        print(f"Arquivo não encontrado: {path}")
        sys.exit(1)

    if path.suffix.lower() == ".csv":
        tempos = load_times_from_csv(path, sep=sep)
    else:
        tempos = load_times_from_txt(path)

    if tempos.empty:
        print("Nenhum tempo válido encontrado no arquivo.")
        sys.exit(1)

    media = tempos.mean()
    desvio = tempos.std(ddof=1)
    print(f"Registros válidos: {len(tempos)}")
    print(f"Média (s): {media:.2f}")
    print(f"Desvio padrão (s): {desvio:.2f}")


if __name__ == "__main__":
    main()
