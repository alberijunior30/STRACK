import shutil
import os
from pathlib import Path
from fastapi import HTTPException
from service.resize_service import resize
from service.size_service import size
from service.vhs_service import vhs

upload = Path("save_directory")
upload.mkdir(exist_ok=True)

async def analyze_service(file_stream, filename: str, processing_action: str):
    img = upload / filename

    with img.open("wb") as buffer:
            shutil.copyfileobj(file_stream, buffer)

    if processing_action == "resize":
         return resize(img)
    
    elif processing_action == "size":
        return size(img)
    
    elif processing_action == "vhs":
        return vhs(img)
    
    else:
        os.remove(img)
        return "ação invalida!!!"
        
