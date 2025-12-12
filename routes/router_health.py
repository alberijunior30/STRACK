from fastapi import APIRouter, HTTPException
from pathlib import Path
from fastapi.responses import FileResponse
import mimetypes
import os

router = APIRouter()

image_dir = Path("processed_image")
extension = [".jpeg", ".jpg", ".png"]

@router.get("/{img_name}", description="Buscar Imagem")
async def get_image(img_name: str):

    found_address = None
    final_img_name = None

    address = image_dir / img_name
    if address.is_file():
        found_address = address
        final_img_name = img_name
    else:
        for ext in extension:
            temp_img_name = img_name + ext 
            temp_address = image_dir / temp_img_name
            
            if temp_address.is_file():
                found_address = temp_address
                final_img_name = temp_img_name
                break
        
    if not found_address:
        raise HTTPException(
            status_code=404, 
            detail=f"Imagem '{img_name}' não encontrada."
        )

    mime_type, _ = mimetypes.guess_type(final_img_name)
    if not mime_type:
        mime_type = 'application/octet-stream'

    return FileResponse(
        path=found_address,
        filename=final_img_name,
        media_type=mime_type
    )