"""
Vision service for image analysis.
"""
import base64
from typing import Optional
from openai import OpenAI

from app.core.openai_client import get_openai_client


class VisionService:
    """Service for vision/image operations."""
    
    def __init__(self):
        self.client: OpenAI = get_openai_client()
    
    def analyze_image(
        self,
        image_base64: str,
        prompt: str = "Descreva esta imagem em detalhes.",
        model: str = "gpt-4-vision-preview"
    ) -> str:
        """
        Analyze an image using GPT-4 Vision.
        
        Args:
            image_base64: Base64 encoded image
            prompt: Prompt for analysis
            model: Model to use
            
        Returns:
            str: Analysis result
        """
        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_base64}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=300
        )
        
        return response.choices[0].message.content
    
    def extract_text_from_image(
        self,
        image_base64: str
    ) -> str:
        """
        Extract text from image (OCR).
        
        Args:
            image_base64: Base64 encoded image
            
        Returns:
            str: Extracted text
        """
        prompt = "Extraia todo o texto visível nesta imagem. Retorne apenas o texto, sem formatação adicional."
        return await self.analyze_image(image_base64, prompt)

