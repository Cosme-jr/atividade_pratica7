# Atividades de Python: CSV, JSON e Estatísticas com Pandas

Repositório com quatro exercícios práticos:
- Questão 1: calcula média e desvio padrão de tempos de execução a partir de logs (CSV/TXT). 
- Questão 2: cria um CSV com as colunas Nome, Idade e Cidade.
- Questão 3: lê um CSV e exibe dados no console (tabela e linha a linha).
- Questão 4: lê e escreve JSON com suporte a acentos (UTF-8). 

## Requisitos
- Python 3.10+ e pip. 
- pandas (instalar via `pip install -r requirements.txt`, se disponível).

## Ambiente virtual (venv)
Crie e ative um ambiente virtual para isolar dependências:
python -m venv venv

PowerShell
.\venv\Scripts\Activate.ps1

CMD
.\venv\Scripts\activate.bat

Referência oficial do venv e guias de ativação em Windows/PowerShell. 

## Estrutura sugerida
atividade_pratica7/

questao1.py

questao2.py

questao3.py

questao4.py

Boas práticas de organização e uso de ambientes virtuais em projetos Python.

## Execução

### Questão 1 — Estatísticas de logs
- CSV (vírgula):  
  `python questao1.py logs.csv`  
- TXT (um valor por linha):  
  `python questao1.py logs.txt`  
- CSV com ponto e vírgula:  
  `python questao1.py logs.csv --sep ";"`  
Leitura com `pandas.read_csv` e cálculos com `Series.mean()` e `Series.std(ddof=1)`. 

### Questão 2 — Gerar CSV de pessoas
- Padrão (gera `pessoas.csv` com vírgula):  
  `python questao2.py`  
- Personalizado (nome e separador):  
  `python questao2.py pessoas.csv --sep ";"`  
Escrita com `DataFrame.to_csv(..., index=False, lineterminator="\n")`. ]

### Questão 3 — Ler CSV e exibir
- Vírgula:  
  `python questao3.py pessoas.csv`  
- Ponto e vírgula:  
  `python questao3.py pessoas.csv --sep ";"`  
Leitura com `pandas.read_csv` e exibição com `DataFrame.to_string()` para não truncar a saída. 

### Questão 4 — JSON (ler/escrever)
- Padrão (cria `pessoa.json` e depois lê):  
  `python questao4.py`  
- Customizar nome:  
  `python questao4.py dados_pessoa.json`  
Uso de `json.dump(..., ensure_ascii=False, indent=2)` e `json.load(...)` (UTF-8).

## .gitignore e versionamento
Crie `.gitignore` na raiz para manter o repo limpo:


pessoas.csv # gerado na Questão 2 (opcional manter)

logs.csv # exemplo para Questão 1 (opcional manter)

venv/ # ignorado pelo Git

venv/
pycache/
*.pyc
.vscode/
.idea/
build/
dist/
*.egg-info/
data/
datasets/

Ignorar venv e artefatos gerados é prática recomendada; mantenha apenas amostras pequenas de dados. 

## Requirements
Gere e use `requirements.txt` para reproduzir o ambiente:

pip freeze > requirements.txt

Em outra máquina:
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

Fluxo recomendado na documentação do pip e guias introdutórios. 

## Fluxo Git básico
git init

git add .

git commit -m "Atividades: CSV/JSON e estatísticas"

git branch -M main

git remote add origin https://github.com/SEU_USUARIO/SEU_REPO.git

git push -u origin main
