"""
Exercicio 3: Criacao de Mascara via Codigo (Pillow)
Referencia: Tutorial 03 - Edicao de Imagens

Este script demonstra como criar uma mascara de transparencia programaticamente utilizando 
a biblioteca Pillow. A mascara e essencial para o processo de Inpainting (edicao de imagens).

Pontos principais:
1. Manipulacao de canais de transparencia (Alpha).
2. Criacao de formas geometricas para definir a area de edicao.
3. Salvamento em formato PNG compativel com a API da OpenAI.
"""

from PIL import Image, ImageDraw
from pathlib import Path

def criar_mascara_circular(dimensao=1024, raio=200):
    # Criar uma imagem preta (totalmente opaca no contexto da API)
    # A API interpreta transparencia como a area a ser pintada.
    # No entanto, uma pratica comum e usar uma imagem onde o canal alpha e 0 nas areas a editar.
    
    # Criar imagem RGBA (Red, Green, Blue, Alpha)
    # Inicialmente toda opaca (Alpha = 255)
    mask = Image.new("RGBA", (dimensao, dimensao), (0, 0, 0, 255))
    draw = ImageDraw.Draw(mask)
    
    # Definir o centro
    centro = dimensao // 2
    
    # Desenhar um circulo transparente (Alpha = 0) no centro
    esquerda_superior = (centro - raio, centro - raio)
    direita_inferior = (centro + raio, centro + raio)
    
    draw.ellipse([esquerda_superior, direita_inferior], fill=(0, 0, 0, 0))
    
    # Salvar a mascara
    assets_dir = Path('../assets')
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = assets_dir / "lab_mask_circular.png"
    mask.save(output_path)
    print(f"Mascara circular gerada com sucesso em: {output_path}")

if __name__ == "__main__":
    criar_mascara_circular()

