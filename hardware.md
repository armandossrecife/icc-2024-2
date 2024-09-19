## Introdução ao Hardware: Arquitetura Básica de um Computador

### Introdução
* **O que é hardware?**
    * Componentes físicos de um computador.
    * Tudo o que podemos tocar e ver.
* **Por que estudar hardware?**
    * Compreender como os computadores funcionam internamente.
    * Escolher o hardware adequado para diferentes tarefas.
    * Resolver problemas relacionados ao hardware.

### Arquitetura Básica de um Computador
* **Modelo de Von Neumann:**
    * Modelo conceitual que descreve a organização básica de um computador.
    * Componentes principais:
        * **Unidade Central de Processamento (CPU):** Cérebro do computador, responsável por executar instruções.
        * **Memória:** Armazena dados e instruções.
        * **Dispositivos de entrada:** Permitem a entrada de dados (teclado, mouse, etc.).
        * **Dispositivos de saída:** Apresentam os resultados (monitor, impressora, etc.).
* **Interconexão entre os componentes:**
    * Barramento: conjunto de fios que interligam os componentes.
    * Transferência de dados entre os componentes.

### Componentes Principais
* **Unidade Central de Processamento (CPU):**
    * **Unidade de controle:** Coordena a execução das instruções.
    * **Unidade lógica e aritmética (ULA):** Realiza operações matemáticas e lógicas.
    * **Registradores:** Áreas de memória de alta velocidade utilizadas para armazenar dados temporariamente.
* **Memória:**
    * **Memória RAM:** Memória de acesso aleatório, volátil, utilizada para armazenar dados enquanto o computador está ligado.
    * **Memória ROM:** Memória somente de leitura, não volátil, armazena o firmware do computador.
    * **Memória secundária:** Discos rígidos, SSDs, pen drives, utilizados para armazenar dados de forma permanente.
* **Dispositivos de Entrada e Saída:**
    * **Entrada:** Teclado, mouse, scanner, câmera, microfone.
    * **Saída:** Monitor, impressora, alto-falantes.

### Interação entre os Componentes
* **Ciclo de instrução:**
    * Processo pelo qual a CPU executa uma instrução.
    * Busca da instrução na memória.
    * Decodificação da instrução.
    * Execução da instrução.
* **Transferência de dados:**
    * Entre a CPU e a memória.
    * Entre a CPU e os dispositivos de entrada e saída.
* **Sistema operacional:**
    * Software que gerencia o hardware e fornece uma interface para o usuário.

### Atividades
* **Exercícios:**
    * Identificar os componentes de um computador em uma imagem.
    * Descrever a função de cada componente.
    * Explicar o ciclo de instrução.
* **Simulações:**
    * Utilizar softwares de simulação para visualizar o funcionamento interno de um computador.
* **Projetos:**
    * Montar um computador simples (opcional).

## Detalhando os Componentes Fundamentais de um Computador

### Tipos de Memória

A memória é um componente essencial para o funcionamento de um computador, sendo responsável por armazenar temporariamente os dados e instruções que estão sendo utilizados pelo processador. Os principais tipos de memória são:

* **RAM (Random Access Memory):** É a memória de acesso aleatório, utilizada para armazenar os dados que estão sendo utilizados ativamente pelo processador. A RAM é volátil, ou seja, os dados são perdidos quando o computador é desligado.
    * **Tipos de RAM:** DDR3, DDR4, DDR5 (diferem em velocidade e capacidade).
* **ROM (Read Only Memory):** É a memória de somente leitura, utilizada para armazenar o firmware do computador, como a BIOS. A ROM não é volátil, ou seja, os dados são mantidos mesmo quando o computador é desligado.
* **Cache:** É uma pequena quantidade de memória extremamente rápida, localizada próximo ao processador, utilizada para armazenar os dados e instruções que são acessados com mais frequência. O cache divide-se em:
    * **Cache de nível 1 (L1):** Menor e mais rápido, integrado ao núcleo do processador.
    * **Cache de nível 2 (L2):** Maior e um pouco mais lento, compartilhado por vários núcleos.
    * **Cache de nível 3 (L3):** Maior ainda e mais lento, compartilhado por todos os núcleos.

### Barramento de Sistema

O barramento de sistema é um conjunto de linhas de comunicação que interconectam os diversos componentes de um computador, como o processador, a memória e os dispositivos de entrada e saída.

* **Tipos de barramentos:**
    * **Barramento de dados:** Transporta os dados entre os componentes.
    * **Barramento de endereços:** Especifica o local de memória onde os dados serão armazenados ou recuperados.
    * **Barramento de controle:** Coordena as operações entre os componentes.
* **Largura de banda:** Representa a quantidade de dados que podem ser transferidos por segundo através do barramento, medida em megabytes por segundo (MB/s) ou gigabytes por segundo (GB/s).

### Processadores

O processador, também conhecido como CPU (Central Processing Unit), é o "cérebro" do computador, responsável por executar as instruções dos programas.

* **Arquiteturas:**
    * **CISC (Complex Instruction Set Computer):** Possui um conjunto complexo de instruções, o que exige um hardware mais complexo.
    * **RISC (Reduced Instruction Set Computer):** Possui um conjunto reduzido de instruções simples, o que o torna mais eficiente.
* **Evolução dos processadores:**
    * **Lei de Moore:** A capacidade de processamento dos computadores dobra a cada dois anos.
    * **Multi-core:** Vários núcleos em um único chip, permitindo executar várias tarefas simultaneamente.
    * **Superescalar:** Capacidade de executar múltiplas instruções por ciclo de clock.

### Dispositivos de Armazenamento

Os dispositivos de armazenamento são utilizados para guardar os dados de forma permanente.

* **Discos rígidos (HD):** Armazenam os dados em um disco magnético giratório. São mais baratos, mas mais lentos que os SSDs.
* **SSDs (Solid State Drives):** Utilizam memória flash para armazenar os dados. São mais rápidos, mais resistentes a choques e mais silenciosos que os HDs.
* **Memória flash:** Utilizada em pen drives, cartões de memória e SSDs. É uma memória não volátil que permite a leitura e a escrita de dados em células de memória individuais.

### Interfaces de Entrada e Saída

As interfaces de entrada e saída permitem a comunicação entre o computador e os dispositivos externos.

* **USB (Universal Serial Bus):** Padrão de conexão mais utilizado, permitindo conectar diversos tipos de dispositivos, como teclados, mouses, pen drives e impressoras.
* **SATA (Serial ATA):** Utilizado para conectar discos rígidos e SSDs internos ao computador.
* **PCI (Peripheral Component Interconnect):** Utilizado para conectar placas de expansão ao computador, como placas de vídeo, placas de rede e placas de som.

**Observações:**

* **Outras interfaces:** Além das mencionadas, existem outras interfaces como HDMI, DisplayPort, Thunderbolt, etc., cada uma com suas características e aplicações específicas.
* **Evolução constante:** A tecnologia está em constante evolução, e novos componentes e interfaces são lançados regularmente.
