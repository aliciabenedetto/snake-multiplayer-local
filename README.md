# Snake Multiplayer Local

Projeto desenvolvido para a Atividade 0010, com o objetivo de criar um jogo da cobrinha multiplayer local em Python, utilizando uma arquitetura modular inspirada no projeto Asteroids Singleplayer.

## Objetivo

O objetivo do projeto é implementar um jogo Snake com dois jogadores no mesmo computador, utilizando o teclado como forma de controle. Cada jogador controla uma cobra independente, disputa a comida no mapa e possui sua própria pontuação.

## Tecnologias utilizadas

- Python 3
- Turtle

## Controles

### Jogador 1

- W: mover para cima
- A: mover para esquerda
- S: mover para baixo
- D: mover para direita

### Jogador 2

- Seta para cima: mover para cima
- Seta para esquerda: mover para esquerda
- Seta para baixo: mover para baixo
- Seta para direita: mover para direita

## Mecânicas do jogo

- Dois jogadores locais na mesma arena
- Movimento contínuo das cobras
- Comida gerada aleatoriamente no mapa
- Crescimento da cobra ao comer
- Pontuação individual
- Colisão com as bordas
- Colisão com o próprio corpo
- Colisão com o adversário
- Reset individual do jogador que perde
- Aumento gradual da velocidade da partida

## Arquitetura do projeto

O projeto foi organizado de forma modular para separar responsabilidades, seguindo uma estrutura semelhante à utilizada em jogos como Asteroids Singleplayer.

## Estrutura de arquivos

```text
snake-multiplayer-local/
│
├── main.py
├── settings.py
├── game.py
├── snake.py
├── food.py
├── collision.py
├── score.py
├── README.md
│
├── docs/
└── assets/
```
## Como executar
```text
python main.py
```