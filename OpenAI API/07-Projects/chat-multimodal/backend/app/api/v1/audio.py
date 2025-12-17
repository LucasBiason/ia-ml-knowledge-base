"""
Audio API endpoints for transcription.
"""
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from app.core.database import get_db
from app.services.audio_service import AudioService
from app.middleware.auth import get_current_user_id

router = APIRouter(prefix="/audio", tags=["audio"])


@router.post("/transcribe")
async def transcribe_audio(
    file: UploadFile = File(...),
    language: str = "pt",
    prompt: Optional[str] = None,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    """
    Transcribe audio using Whisper.
    
    Args:
        file: Audio file to transcribe
        language: Language code (pt, en, etc.)
        prompt: Optional context prompt
        db: Database session
        user_id: Current user ID
        
    Returns:
        dict: Transcription result
    """
    # Validate file type
    if not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="File must be an audio file")
    
    # Read audio file
    audio_bytes = await file.read()
    
    # Create file-like object
    import io
    audio_file = io.BytesIO(audio_bytes)
    audio_file.name = file.filename
    
    # Transcribe
    service = AudioService()
    transcription = service.transcribe_audio(audio_file, language, prompt)
    
    return {"transcription": transcription, "filename": file.filename}


@router.post("/translate")
async def translate_audio(
    file: UploadFile = File(...),
    target_language: str = "en",
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    """
    Transcribe and translate audio.
    
    Args:
        file: Audio file
        target_language: Target language
        db: Database session
        user_id: Current user ID
        
    Returns:
        dict: Translated text
    """
    if not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="File must be an audio file")
    
    # Read audio file
    audio_bytes = await file.read()
    
    # Create file-like object
    import io
    audio_file = io.BytesIO(audio_bytes)
    audio_file.name = file.filename
    
    # Translate
    service = AudioService()
    translation = service.translate_audio(audio_file, target_language)
    
    return {"translation": translation, "filename": file.filename}

