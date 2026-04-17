from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4

# Definindo o modelo de dados para os itens
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    on_offer: bool = False

# Criando a aplicação FastAPI
app = FastAPI()
# Armazenamento em memória para os itens
items = {}

# Rota para criar um novo item (POST)
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    item_id = uuid4()
    items[item_id] = item
    return item

# Rota para listar todos os itens (GET)
@app.get("/items/", response_model=dict)
async def read_items():
    return items

# Rota para obter um item específico por ID (GET)
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: UUID):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

# Rota para atualizar um item existente (PUT)
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: UUID, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return item

# Rota para deletar um item por ID (DELETE)
@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: UUID):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items.pop(item_id)