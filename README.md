# Projeto STRACK

# Como Rodar o Projeto:

## Pré-requisitos
Antes de começar, certifique-se de ter os seguintes itens instalados na sua máquina:

- **Python 3.11+** (caso esteja usando FastAPI) 
- **virtualenv** (para gerenciar dependências)  

---

##  Passos para Rodar o Projeto


###  Crie e ative um ambiente virtual:
```bash
python -m venv venv
windows:
.\venv\Scripts\activate

linux/mac:
source venv/Scripts/activate  


```
### Instale as dependências:
```bash
pip install -r requirements.txt 
```

###  Rode o servidor:
```bash
uvicorn app.main:app --reload
```
API disponível em `http://127.0.0.1:8000`. 
Swagger -> `http://127.0.0.1:8000/docs`
