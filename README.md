# projeto-IA-lousaDigital

Este é um projeto simples de desenho usando a webcam, onde você pode desenhar na tela utilizando os dedos das mãos. O código faz uso da biblioteca cv2 (OpenCV) para capturar o vídeo e processar a imagem, da biblioteca cvzone para detecção de mãos e gestos, além de outras bibliotecas auxiliares. O projeto permite mudar a cor do desenho, desenhar na tela com o movimento das mãos e salvar a imagem gerada.

## Requisitos
Antes de executar o código, você precisa instalar as bibliotecas necessárias. Utilize o seguinte comando para instalar as dependências:

    pip install opencv-python cvzone numpy
  
Como funciona
- **1. Captura de vídeo**
O código começa capturando o vídeo em tempo real da webcam (resolução 1280x720), utilizando o cv2.VideoCapture. A partir daí, ele processa cada frame da captura para detectar as mãos.

- **2. Detecção de mãos**
A biblioteca cvzone é usada para detectar a posição das mãos e dos dedos. A função HandDetector é responsável por localizar as mãos e identificar os pontos de referência das articulações dos dedos.

- **3. Desenho**
O desenho é feito utilizando o movimento do dedo indicador. Quando o código detecta o dedo indicador levantado (apenas o indicador), ele desenha um círculo no local do dedo. Ao mover o dedo, o código continua desenhando linhas que conectam os pontos mais recentes.

- **4. Troca de cor**
Trocar a cor do desenho pressionando as teclas numéricas:

Pressione 1 para escolher a cor vermelha
Pressione 2 para escolher a cor verde
Pressione 3 para escolher a cor azul
Pressione 4 para escolher a cor amarela

- **5. Limpeza do desenho**
Quando o usuário mostrar 3 dedos, o desenho é apagado, e a lista de pontos desenhados é limpa.

- **6. Salvar a imagem**
Você pode salvar a imagem desenhada pressionando a tecla S. O arquivo será salvo com um nome único baseado no timestamp atual (data e hora).

- **7. Fechar o programa**
Para fechar o programa, basta pressionar a tecla ESC.

----

## Como executar

Clone o repositório ou baixe os arquivos.
Execute o script em um ambiente Python com as dependências instaladas.
O aplicativo da webcam será iniciado, e você poderá desenhar com as mãos.

### Exemplos de Comandos de Teclado:
- **Pressionar 1:** Cor vermelha.
- **Pressionar 2:** Cor verde.
- **Pressionar 3:** Cor azul.
- **Pressionar 4:** Cor amarela.
- **Pressionar S:** Salvar a imagem gerada.
Pressionar ESC: Fechar o aplicativo.
