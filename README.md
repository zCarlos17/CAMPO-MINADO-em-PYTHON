# 💣 Campo Minado em Python

Um jogo clássico de Campo Minado (Minesweeper) feito totalmente em Python, jogado direto no terminal, com **menu interativo** e **configurações personalizáveis** de tamanho e número de minas.

---

## 🧠 Sobre o Projeto

Este projeto foi desenvolvido para praticar:

* **Lógica de programação**
* Manipulação de **matrizes**
* **Recursividade**
* **Controle de fluxo** em Python

O jogo é executado diretamente no terminal e oferece uma interface **interativa**.

---

## ⚙️ Funcionalidades Detalhadas

### 🎮 Menu Interativo

O jogo apresenta um menu interativo com **4 opções** principais:

1.  **Iniciar Jogo**
2.  **Configurações**
3.  **Reiniciar**
4.  **Sair**

### ⚙️ Configurações Personalizadas

O jogador pode personalizar a experiência definindo:

* **Tamanho do campo**: De 3x3 até 10x10.
* **Número de minas**: Até 50% da área total do campo.

### 💥 Jogo Completo

A mecânica do jogo inclui:

* Sistema de **abertura de células**.
* **Propagação automática** de células vazias (`[0]`) por meio de recursividade.
* **Marcação e desmarcação** de minas (`[M]`).
* Verificação **automática de vitória** e derrota.

### 🧩 Funções Principais

O código é estruturado em torno das seguintes funções-chave:

* `definir_mapa()`
* `definir_minas()`
* `gerar_minas()`
* `mostrar_campo()`
* `abrir_celula()`
* `propagacao_abertura()`
* `marcar_mina()`
* `verificar_vitoria()`
* `reiniciar_jogo()`

---

## ▶️ Como Jogar

### 1. Pré-requisitos

#### 🖥️ Pré-requisitos

* **Python 3.x** instalado.

### 2. Execução do Programa

Execute o programa a partir do terminal:
python campo_minado.py

### 3. Passos do Jogo

1.  **Configurar**: No menu inicial, escolha **2 → Configurações** para:
    * Definir o tamanho do mapa (**máx. 10x10**).
    * Definir a quantidade de minas (**máx. 50% da área**).
2.  **Iniciar**: Escolha **1 → Iniciar jogo**.
3.  **Jogar**: Durante a partida, você terá as seguintes ações:
    * Escolha **1** para **abrir** uma posição.
    * Escolha **2** para **marcar/desmarcar** uma mina.
    * Escolha **3** para sair do jogo.

### 🎯 Objetivo

* **Abra todas as células** que não contêm minas!
* A **vitória** ocorre quando todas as células seguras forem abertas.

---

## 🎨 Exemplo de Execução (Terminal)
=============================================================  
                  C A M P O  M I N A D O  
|| 1 - Iniciar Jogo  
|| 2 - Configurações  
|| 3 - Reiniciar  
|| 4 - Sair  
|| Opção: 1  
|| AÇÃO: ABRIR POSIÇÃO  
|| Digite a linha: 2  
|| Digite a coluna: 3  
---

## 🧱 Estrutura do Código

O código é dividido em blocos bem organizados para facilitar a leitura e manutenção:

* **⚙️ Funções Auxiliares**:
    * Criação e exibição do mapa.
    * Geração de minas e cálculo de vizinhos.
    * Exibição das células.
* **💣 Funções Principais**:
    * Abrir célula (com abertura recursiva de áreas seguras).
    * Marcar/Desmarcar minas.
    * Verificar condições de vitória ou derrota.
* **🔁 Loop Principal**:
    * Menu inicial e controle de fluxo.
    * Reinício e encerramento do jogo.

---

## 🧑‍💻 Autor e Licença

### 👤 Autor

* **Carlos**
* 📍 Projeto pessoal de aprendizado em Python.
* 💬 Sinta-se à vontade para **contribuir**, melhorar o código ou deixar sugestões!

### 🏁 Licença

* Este projeto é de **uso livre** para fins educacionais e pessoais.
* Distribuído sob a **licença MIT**.
