import cv2
import numpy as np


class Trabalho_02(object):
    # Faz referência a imagem no diretório onde ela se encontra.
    image = cv2.imread('imagens/pecasLego.jpg')

    '''
    Função responsável por aplicar a máscara de Thresholding na imagem.
    :imagem - Imagem que será realizado o thresholding.
    :min - Limite mínimo do thresholding.
    :maz - Limite máximo do thresholding.
    
    :return Retorna a imagem com o thresholding já aplicado.
    '''

    def criaImagem(imagem, min, max):
        # Converte a imagem para o padrão de cores HSV
        img_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV);

        # Define os limites da máscara
        lower = np.array([min, 0, 0]);
        upper = np.array([max, 255, 255]);

        # Cria a máscara de acordo com os limites atribuidos.
        mask = cv2.inRange(img_hsv, lower, upper);

        # Retorna a imagem aplicando a máscara.
        return cv2.bitwise_and(imagem, imagem, mask=mask);

    """
    Função responsável por realizar a operação booleana OU em duas imagens.
    :imagem1 - Primeira imagem, a quase será aplicada a operação.
    :imagem2 - Segunda imagem, a quase será aplicada a operação.
    :return Retorna a imagem da operação booleana OU.
    """

    def juntaImagens(imagem1, imagem2):
        # Retorna uma imagem com a operação booleana OU realizada.
        return cv2.bitwise_or(imagem1, imagem2);

    # Exibe o resultado em da operação booleada.
    cv2.imshow('Imagem-Resultado', juntaImagens(criaImagem(image, 95, 115), criaImagem(image, 55, 67)));

    # Aguarda uma tecla para que a imagem seja fechada.
    cv2.waitKey(0);
