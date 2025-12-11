from fastapi import APIRouter, HTTPException, Query
from pathlib import Path
from fastapi.responses import FileResponse

router = APIRouter()

image_dir = Path("processed_image")

@router.get("/", description="Buscar Imagem")
async def health(img_name:str = Query(..., description="Digite o nome da imagem igual da que foi enviada")):

    address = image_dir/img_name

    if not address.is_file():

            raise HTTPException(status_code=404, detail=f"Imagem '{img_name}' não encontrada.")

    return FileResponse(
        path=address,
        filename=img_name,
        media_type='image/jpeg'
    )   