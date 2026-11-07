
from pydantic import BaseModel, Field


class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Frase de entrada para o GPT-2"
    )


class TextResponse(BaseModel):
    input_text: str
    generated_text: str
