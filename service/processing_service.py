import shutil
from pathlib import Path
from fastapi import HTTPException

upload = Path("save_directory")
upload.mkdir(exist_ok=True)

async def analyze_service(file_stream, filename: str, processing_action: str):
    img = upload/filename
    if img.exists():
        raise HTTPException(status_code=409, detail=f"Imagem '{filename}' já existe. RENOMEI")
    else:
        with img.open("wb") as buffer:
            shutil.copyfileobj(file_stream, buffer)

                
        return {
            "status": "sucesso",
            "message": "Imagem salva com sucesso.",
            "filename": filename,
            "path": str(img),
            "process": str(processing_action)
            }