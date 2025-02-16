from database import engine
import models

print("Criando tabelas no banco de dados...")
models.Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")