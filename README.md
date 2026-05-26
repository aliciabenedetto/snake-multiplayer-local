# Snake Multiplayer Local

Projeto desenvolvido para a Atividade 0010, com o objetivo de criar um jogo da cobrinha multiplayer local em Python, utilizando uma arquitetura modular inspirada no projeto Asteroids Singleplayer.

## Objetivo

O objetivo do projeto é implementar um jogo Snake com dois jogadores no mesmo computador, utilizando o teclado como forma de controle. Cada jogador controla uma cobra independente, disputa a comida no mapa e possui sua própria pontuação.

## Tecnologias utilizadas

- Python 3
- Turtle
- Git
- GitHub

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

## Controles do sistema

- P: iniciar partida
- ESPAÇO: reiniciar após Game Over
- Q: sair do jogo

## Mecânicas do jogo

- Dois jogadores locais na mesma arena
- Movimento contínuo das cobras
- Comida gerada aleatoriamente no mapa
- Crescimento da cobra ao comer
- Pontuação individual
- Colisão com o próprio corpo
- Colisão com o corpo do adversário
- Sistema de Game Over
- Tela inicial interativa
- Tela de reinício da partida
- Efeitos sonoros
- Aumento gradual da velocidade da partida
- Sistema de teleporte nas bordas do mapa (wrap-around)

## Condições de vitória e derrota

### Vitória

- Cada comida coletada vale 10 pontos.
- O primeiro jogador que atingir 50 pontos vence a partida.

### Derrota

A rodada termina quando ocorre:

- colisão com o próprio corpo;
- colisão com o corpo do adversário.

### Teleporte nas bordas

O jogo utiliza um sistema de wrap-around. Quando a cobra ultrapassa um limite da tela, ela reaparece automaticamente no lado oposto do mapa.

## Arquitetura do projeto

O projeto foi organizado de forma modular para separar responsabilidades, seguindo uma estrutura semelhante à utilizada em jogos como Asteroids Singleplayer.

A arquitetura foi dividida em:

- gerenciamento do jogo;
- entidades;
- colisões;
- pontuação;
- configurações;
- entrada do jogador;
- renderização da interface.

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
├── sound.py
├── README.md
│
├── docs/
└── assets/
```
## Execute o jogo:
```text
python main.py
```
