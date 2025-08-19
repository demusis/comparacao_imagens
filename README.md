# Análise de Diferença Computacional entre Imagens

Este script em Python realiza uma análise de diferença computacional para identificar e visualizar divergências entre dois arquivos de imagem digital. A ferramenta foi desenvolvida para auxiliar em atividades de perícia digital e análise de autenticidade de imagens, sendo especialmente útil para verificar se uma imagem é um reprocessamento (e.g., recompressão, reescalonamento) de outra.

## Funcionalidades

  - **Comparação Pixel a Pixel:** Executa uma subtração matemática entre os valores de cada pixel das duas imagens para encontrar as diferenças exatas.
  - **Suporte a Imagens de Dimensões Distintas:** Detecta automaticamente se as imagens possuem tamanhos diferentes e redimensiona a imagem maior para equipará-la à menor, utilizando o filtro de alta qualidade `LANCZOS` para minimizar distorções.
  - **Realce Visual das Diferenças:** Amplifica matematicamente o resultado da diferença para que discrepâncias sutis, muitas vezes imperceptíveis a olho nu, tornem-se facilmente visíveis.
  - **Exportação Segura:** Salva o mapa de divergências resultante em formato PNG, um formato sem perdas, para garantir que a própria análise não introduza novos artefatos de compressão.

## Pré-requisitos

  - Python 3.6+
  - Biblioteca Pillow (PIL Fork)

## Instalação

Para instalar a biblioteca Pillow, execute o seguinte comando no seu terminal ou prompt de comando:

```bash
pip install Pillow
```

## Modo de Uso

1.  Salve o script (`analise_imagem.py`, por exemplo) em um diretório de sua preferência.

2.  Coloque os dois arquivos de imagem que deseja comparar no mesmo diretório do script.

3.  Abra o arquivo do script em um editor de texto e modifique as variáveis dentro do bloco `if __name__ == "__main__":` para que correspondam aos nomes dos seus arquivos:

    ```python
    # Imagem 1 (original ou reprocessada)
    arquivo_imagem_1 = "imagem_A.jpg" 

    # Imagem 2 (original ou reprocessada)
    arquivo_imagem_2 = "imagem_B.jpg" 

    # Nome do arquivo de saída que conterá a análise
    arquivo_resultado = "resultado_analise.png"
    ```

4.  Abra um terminal, navegue até o diretório onde salvou os arquivos e execute o script:

    ```bash
    python analise_imagem.py
    ```

## Interpretando o Resultado

O script gera uma imagem que funciona como um **mapa visual das diferenças**. A interpretação segue a seguinte lógica:

  - **Áreas Pretas/Escuras:** Indicam regiões onde os pixels das duas imagens são idênticos ou possuem alta similaridade.
  - **Áreas Claras/Coloridas:** Indicam regiões onde os pixels são diferentes. A intensidade do brilho é diretamente proporcional à magnitude dessa diferença.

Um resultado com poucas ou nenhuma área preta, exibindo uma "textura" ruidosa em toda a sua extensão, sugere uma **alteração global**, como uma nova compressão em formato JPEG ou um redimensionamento.

## Detalhes Técnicos

  - **Método de Comparação:** Análise de Diferença via subtração de matrizes de pixels (`ImageChops.difference`).
  - **Filtro de Reamostragem:** `Image.Resampling.LANCZOS` para redimensionamento de alta qualidade.
  - **Método de Realce:** Amplificação do brilho da imagem de diferença (`ImageEnhance.Brightness`).
