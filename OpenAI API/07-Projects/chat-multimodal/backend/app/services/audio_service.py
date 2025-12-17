"""
Audio service for transcription.
"""
from openai import OpenAI
from app.core.openai_client import get_openai_client


class AudioService:
    """Service for audio operations."""
    
    def __init__(self):
        self.client: OpenAI = get_openai_client()
    
    def transcribe_audio(
        self,
        audio_file,
        language: str = "pt",
        prompt: Optional[str] = None
    ) -> str:
        """
        Transcribe audio using Whisper.
        
        Args:
            audio_file: Audio file object
            language: Language code (pt, en, etc.)
            prompt: Optional context prompt
            
        Returns:
            str: Transcription text
        """
        transcription = self.client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language=language,
            prompt=prompt
        )
        
        return transcription.text
    
    def translate_audio(
        self,
        audio_file,
        target_language: str = "en"
    ) -> str:
        """
        Transcribe and translate audio.
        
        Args:
            audio_file: Audio file object
            target_language: Target language for translation
            
        Returns:
            str: Translated text
        """
        translation = self.client.audio.translations.create(
            model="whisper-1",
            file=audio_file
        )
        
        return translation.text

