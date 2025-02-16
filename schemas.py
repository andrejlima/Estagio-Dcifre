from pydantic import BaseModel, EmailStr, ConfigDict
from typing import List

class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: str

class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    empresa_id: int 

class ObrigacaoAcessoriaResponse(ObrigacaoAcessoriaBase):
    id: int
    empresa_id: int

    model_config = ConfigDict(from_attributes=True) 

class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: EmailStr
    telefone: str

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaResponse(EmpresaBase):
    id: int
    obrigacoes: List[ObrigacaoAcessoriaResponse] = [] 

    model_config = ConfigDict(from_attributes=True) 