
from fastapi import FastAPI, HTTPException
from transformers import pipeline

from models import TextRequest, TextResponse


app = FastAPI(
    title="TP2 - Questão 1 - GPT-2",
    description="API para geração de texto com FastAPI e Hugging Face",
    version="1.0.0"
)

# Carrega o modelo uma única vez
generator = pipeline(
    "text-generation",
    model="openai-community/gpt2",
    device=-1
)


@app.post("/generate", response_model=TextResponse)
def generate_text(request: TextRequest):
    try:
        result = generator(
            request.text,
            max_new_tokens=50,
            do_sample=True,
            temperature=0.7,
            pad_token_id=generator.tokenizer.eos_token_id
        )

        return {
            "input_text": request.text,
            "generated_text": result[0]["generated_text"]
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Erro ao gerar o texto."
        )
