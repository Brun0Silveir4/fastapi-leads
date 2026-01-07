# FastAPI + MongoDB + 

Este projeto é uma API REST desenvolvida com **FastAPI**, utilizando **MongoDB** como 
database para persistencia de dados e **Docker** para containerização do banco.

<br>

## Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- MongoDB
- Docker para o DB
- HTTPX

<br>

## 📂 Arquitetura do Projeto

app/
<br/>├── core/           
├── routes/        
├── schemas/        
├── services/       
├── repositories/  
├── external/      
├── main.py

<br>

## Configuração do Ambiente

### 1. Clone o projeto

```bash
git clone https://github.com/Brun0Silveir4/fastapi-leads
```

<br>

### 2. Criar o arquivo `.env` na raiz do projeto.

```env
MONGO_URI=mongodb://localhost:27018
MONGO_DB_NAME=TesteTecnicoLeadsAPI
MONGO_HOST=localhost
MONGO_PORT=27017
```

<br>


### 3. Como iniciar o MongoDB (Docker)

**Suba o MongoDB pela primeira vez**
```bash
docker compose up --build
```

**Para iniciar pela segunda vez**
```bash
docker compose up --d
```

**O MongoDB ficará disponivel em:**
```bash
mongodb://localhost:27018
```

**Parar o docker:**
```bash
docker compose down
```

<br>

### 4. Como rodar a API

**Instale as dependencias**
```bash
pip install fastapi uvicorn motor python-dotenv httpx email-validator
```

**Inicie a aplicação**
```bash
python -m uvicorn app.main:app --reload
```

A aplicação ficará disponivel em `http://localhost:8000/`

<br>

### 5. Testando os endpoints no POSTMAN/Insomnia

**Post `/leads`**
```json
{
  "name": "Name",
  "email": "email@email.com",
  "phone": "11999999999"
}
```

**Listar registros**
- GET `/leads`

**Buscar por ID**
- GET `/leads/{id}`

**Deletar**
- Delete `/leads/{id}`

<br>

## 6. Observações finais

- MongoDB utiliza docker para persistência
- API totalmente assincrona
- Estrutura preparada para escalabilidade