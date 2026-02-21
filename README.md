# 🚀 Jogo de Nave (Asteroids Clone)

Um jogo clássico no estilo *Asteroids*, desenvolvido totalmente em Python utilizando a biblioteca **Pygame**. O objetivo é sobreviver no espaço sideral destruindo asteroides que se dividem em pedaços menores quando atingidos!

Este projeto foi construído focando nos conceitos de **Programação Orientada a Objetos (POO)** e **Matemática de Vetores 2D** para a física de movimentação e colisão.

## 🌟 Funcionalidades

* **Física Espacial:** Movimentação fluida baseada em vetores (aceleração, rotação e velocidade).
* **Sistema de Disparo:** Mecânica de tiro com tempo de recarga (*cooldown*) para evitar disparos infinitos.
* **Dinâmica de Asteroides:** Asteroides grandes se dividem em dois asteroides menores com velocidades e ângulos aleatórios ao serem destruídos.
* **Detecção de Colisão:** Sistema de colisão circular preciso (raios de distância) entre o jogador, os tiros e os asteroides.

## 🎮 Controles do Jogo

* **W** - Acelera a nave para frente
* **S** - Move a nave para trás
* **A** - Gira a nave para a esquerda
* **D** - Gira a nave para a direita
* **ESPAÇO** - Dispara um tiro a laser

## 💻 Como rodar o projeto localmente

**Pré-requisitos:** Você precisa ter o [Python 3](https://www.python.org/downloads/) instalado na sua máquina.

1. Clone este repositório:
   ```bash
   git clone [https://github.com/SeuUsuario/JogoNave.git](https://github.com/SeuUsuario/JogoNave.git)# JogoNave
2.Entre na pasta do projeto
  
         cd JogoNave
  
3. Crie um ambiente virtual

         python -m venv .venv
         source .venv/bin/activate  # No Linux/Mac
         ou .venv\Scripts\activate no Windows

5. Instale as dependências

         pip install pygame

7. Inicie um jogo

         python main.py

🛠️ Tecnologias Utilizadas
   
      Python 3.13
      Pygame 2.6

  
