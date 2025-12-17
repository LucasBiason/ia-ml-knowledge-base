"""
Vision API endpoints for image analysis.
"""
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
import base64

from app.core.database import get_db
from app.services.vision_service import VisionService
from app.middleware.auth import get_current_user_id

router = APIRouter(prefix="/vision", tags=["vision"])


@router.post("/analyze")
async def analyze_image(
    file: UploadFile = File(...),
    prompt: str = "Descreva esta imagem em detalhes.",
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    """
    Analyze an image using GPT-4 Vision.
    
    Args:
        file: Image file to analyze
        prompt: Prompt for analysis
        db: Database session
        user_id: Current user ID
        
    Returns:
        dict: Analysis result
    """
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    # Read and encode image
    image_bytes = await file.read()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")
    
    # Analyze
    service = VisionService()
    analysis = service.analyze_image(image_base64, prompt)
    
    return {"analysis": analysis, "filename": file.filename}


@router.post("/ocr")
async def extract_text(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    """
    Extract text from image (OCR).
    
    Args:
        file: Image file
        db: Database session
        user_id: Current user ID
        
    Returns:
        dict: Extracted text
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    # Read and encode image
    image_bytes = await file.read()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")
    
    # Extract text
    service = VisionService()
    text = service.extract_text_from_image(image_base64)
    
    return {"text": text, "filename": file.filename}

