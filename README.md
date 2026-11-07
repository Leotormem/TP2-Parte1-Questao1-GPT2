# TP2 — Parte 1, Questão 1: Geração de Texto com GPT-2

## Descrição

Este projeto foi desenvolvido para a disciplina Desenvolvimento de Data-Driven Apps com Python.

O objetivo é criar uma API utilizando FastAPI e o modelo GPT-2 da Hugging Face para gerar continuações de texto a partir de frases enviadas pelo usuário.

A aplicação recebe uma frase em formato JSON, processa a entrada utilizando o modelo GPT-2 e retorna o texto gerado.

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- Hugging Face Transformers
- PyTorch
- Pydantic

## Estrutura do projeto

```text
parte1_questao1_gpt2/
├── main.py
├── models.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalação e execução

**1. Criar o ambiente virtual**

```powershell
python -m venv .venv
```

**2. Ativar o ambiente virtual no Windows**

```powershell
.\.venv\Scripts\Activate.ps1
```

**3. Instalar as dependências**

```powershell
python -m pip install -r requirements.txt
```

**4. Iniciar a aplicação**

```powershell
python -m uvicorn main:app --reload
```

O modelo GPT-2 será baixado automaticamente na primeira execução, caso ainda não esteja disponível no cache local.

## Como utilizar

Acesse a documentação da API:

http://127.0.0.1:8000/docs

Abra a rota `POST /generate`, clique em **Try it out** e envie um JSON como este:

```json
{
  "text": "Python is one of the most popular programming languages because"
}
```

A API retorna um JSON contendo a frase enviada e o texto gerado pelo GPT-2.

## Testes realizados

Foram realizados testes utilizando o Swagger UI com frases relacionadas a inteligência artificial, programação Python e educação.

Nos testes confirmados, a API retornou o código HTTP 200 e uma continuação de texto gerada pelo modelo.

## Observações

O GPT-2 gera texto com base em padrões aprendidos durante o treinamento. As respostas podem variar entre execuções e nem sempre apresentam coerência ou informações corretas.

A aplicação utiliza o modelo `openai-community/gpt2`, executado localmente em CPU.

## Autor

Leonardo Luiz Tormem