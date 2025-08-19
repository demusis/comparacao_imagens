# -*- coding: utf-8 -*-

from PIL import Image, ImageChops, ImageEnhance
import os

def analisar_diferenca_imagens_avancado(caminho_imagem_a: str, caminho_imagem_b: str, caminho_saida: str, fator_realce: float = 20.0):
    """
    Realiza uma análise de diferença avançada entre duas imagens, suportando
    arquivos com dimensões diferentes.

    O script redimensiona a imagem maior para as dimensões da menor antes da
    comparação, utilizando um filtro de alta qualidade (LANCZOS) para
    minimizar distorções.

    Args:
        caminho_imagem_a (str): O caminho para a primeira imagem.
        caminho_imagem_b (str): O caminho para a segunda imagem.
        caminho_saida (str): O caminho onde a imagem com o resultado será salva.
        fator_realce (float): Fator para aumentar o brilho das diferenças.
    
    Returns:
        bool: True se a análise foi bem-sucedida, False caso contrário.
    """
    try:
        # Validação dos caminhos de entrada
        if not os.path.exists(caminho_imagem_a):
            print(f"Erro: O arquivo da imagem A não foi encontrado em '{caminho_imagem_a}'")
            return False
        if not os.path.exists(caminho_imagem_b):
            print(f"Erro: O arquivo da imagem B não foi encontrado em '{caminho_imagem_b}'")
            return False

        # Abrir as imagens
        imagem_a = Image.open(caminho_imagem_a).convert('RGB')
        imagem_b = Image.open(caminho_imagem_b).convert('RGB')

        # --- LÓGICA DE REDIMENSIONAMENTO ---
        if imagem_a.size != imagem_b.size:
            print("Aviso: As imagens possuem dimensões diferentes. Realizando redimensionamento para comparação.")
            print(f"  - Dimensões Originais A: {imagem_a.size}")
            print(f"  - Dimensões Originais B: {imagem_b.size}")
            
            # Identifica qual imagem é maior com base na área total de pixels
            size_a = imagem_a.width * imagem_a.height
            size_b = imagem_b.width * imagem_b.height

            if size_a > size_b:
                print(f"  - Redimensionando Imagem A para as dimensões da Imagem B ({imagem_b.size}).")
                imagem_a = imagem_a.resize(imagem_b.size, Image.Resampling.LANCZOS)
            else:
                print(f"  - Redimensionando Imagem B para as dimensões da Imagem A ({imagem_a.size}).")
                imagem_b = imagem_b.resize(imagem_a.size, Image.Resampling.LANCZOS)

        # Calcular a diferença absoluta entre as imagens (agora com o mesmo tamanho)
        imagem_diferenca = ImageChops.difference(imagem_a, imagem_b)

        # Realçar o resultado para que diferenças sutis se tornem visíveis
        realce = ImageEnhance.Brightness(imagem_diferenca)
        imagem_realcada = realce.enhance(fator_realce)
        
        # Salvar a imagem de resultado em formato PNG
        imagem_realcada.save(caminho_saida, 'PNG')

        print(f"\nAnálise concluída com sucesso. O resultado foi salvo em: '{caminho_saida}'")
        return True

    except Exception as e:
        print(f"Ocorreu um erro inesperado durante a análise: {e}")
        return False

# --- BLOCO DE EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    # --- CONFIGURE OS CAMINHOS AQUI ---
    # Substitua com os nomes dos seus arquivos de imagem.
    
    # Imagem 1 (original ou reprocessada)
    arquivo_imagem_1 = "IMG_20250212_125820763 - FOTO DROGA 01.jpg" 
    
    # Imagem 2 (original ou reprocessada)
    arquivo_imagem_2 = "imagem_extraida.jpg" 
    
    # Nome do arquivo de saída que conterá a análise
    arquivo_resultado = "resultado_analise_diferenca_escalonada.png"

    # Chama a função de análise
    analisar_diferenca_imagens_avancado(
        caminho_imagem_a=arquivo_imagem_1,
        caminho_imagem_b=arquivo_imagem_2,
        caminho_saida=arquivo_resultado
    )