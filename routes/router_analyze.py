from fastapi import APIRouter, UploadFile, File, Query
from pathlib import Path
from service.processing_service import analyze_service

router = APIRouter()

upload = Path("save_directory")
upload.mkdir(exist_ok=True)

@router.post("/processing_action", description="Enviar Imagem")
async def analyze(
        upload_file: UploadFile = File(...),
        processing_action: str = Query(..., description="Ação a ser realizada (ex:size, resize, hsv  )")
    ):
        process = await analyze_service(
            file_stream=upload_file.file,
            filename=upload_file.filename,
            processing_action=processing_action
            )        
        return process
        
