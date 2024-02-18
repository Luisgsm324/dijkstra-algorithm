# Algoritmo de Dijkstra (E.W. Dijkstra)

O projeto "Algoritmo de Dijkstra" foi desenvolvido inteiramente com a utilização da linguagem Python e de bibliotecas para interface gráfica e visualização de grafos, sendo elas: NetworkX, Matplotlib, Tkinter e Pillow. O algoritmo de Dijkstra foi criado pelo cientista holandês Edsger Dijkstra em 1956 e foi publicado em 1959. O algoritmo busca solucionar um problema de encontrar o caminho mais perto ou o de menor custo entre nós de um grafo. O algoritmo funciona da seguinte forma: Escolhemos um nó inicial ou de origem, passa por cada nó do grafo, registrando a menor distância de cada um e marcando como "visitado", o processo termina até que todos os nós sejam marcados como visitados e sejam registradas os menores caminhos a partir do nó de origem.

## Contexto:

O metrô de Tokyo, localizado no Japão, possui aproximadamente 290 estações espalhadas por toda a cidade, contendo diversas linhas que se conectam, permitindo que sejam traçadas várias rotas de uma estação para outra. Dito isso, o programa foi criado utilizando o "Algoritmo de Dijkstra" para determinar o menor trajeto a ser percorrido (tendo em conta apenas a distância, desconsiderando aspectos como tempo de espera) entre as estações para que se alcance o destino final pretendido. Para que o objetivo fosse atendido, utilizamos uma base de dados em formato JSON, que contém informações sobre as linhas, estações e suas respectivas conexões do sistema de metrô da capital japonesa até o ano de 2017. Sendo mais específico, esse banco de informações continham as seguintes informações: códigos das estações e seus nomes tanto no alfabeto japonês quanto no latino, as conexões entre as estações, especificando sobre a forma como é possível chegar (caminhada ou pelo próprio metrô) e a distância entre elas e os nomes da linhas (A, C, E, F...).

## Execução:

Para a execução do código, é necessário:

1. Ter o python instalado em sua máquina

2. Instalar as dependências:
```bash
pip install networkx matplotlib pillow
```

3. Iniciar o projeto
```bash
python main.py
```

## Integrantes do projeto e suas responsabilidades:

[Luís Moreira (lfsgm)](https://github.com/Luisgsm324) - Construção do Algoritmo de Dijkstra e criação da Interface Gráfica.

[Vitor Mendonça (vhmq)](https://github.com/VitorMendonca62) - Criação da estrutura e do visualizar de Grafos. 

## Desenvolvimento do projeto: 

O desenvolvimento do projeto foi organizado em divisão de tarefas, estabelecemos algumas atividades como: Criação da estrutura de dados (Grafo), Formatação das informações do banco de dados para o grafo, Construção do Algoritmo de Dijkstra, Criação do Visualizador de Grafos e Implementação da Interface Gráfica. Com o andamento da construção do programa, buscamos estabelecer uma linha direta de comunicação para a cooperação nas tarefas estabelecidas para ambos, fator que permitiu a correção de problemas e sugestões para a melhoria do projeto. Durante o desenvolvimento, utilizamos a principal ferramenta de controle de versões de software, que seria o GitHub, permitindo que as versões criadas fossem registradas e facilitava a visualização.

## Ferramentas, Bibliotecas e Frameworks utilizados: 

Utilizamos as bibliotecas NetworkX e Matplotlib para visualizar o grafo completo de todas as estações e também o caminho menos custoso para chegar em alguma estação final.Usamos também as bibliotecas Tkinter e Pillow para a interface gráfica, onde a Tkinter era responsável pela interface em si e o Pillow para processamento de imagens.


## Galeria de imagens do projeto:

<img src="https://cdn.discordapp.com/attachments/1138644058898694149/1208864943776989194/image.png?ex=65e4d636&is=65d26136&hm=df2272a2c3f033ec28f1a1a7a321322b98dcf1c322af1a4825df9c6ff93e5d75&">

<img src="https://media.discordapp.net/attachments/1138644058898694149/1208864997804089424/image.png?ex=65e4d643&is=65d26143&hm=0edaa6103dc9940e93e84496eec087660f15d058985f768b8a4046597331a50b&=&format=webp&quality=lossless&width=1165&height=655">

<img src="https://media.discordapp.net/attachments/1138644058898694149/1208865055131566090/image.png?ex=65e4d650&is=65d26150&hm=a18bcb5385df9c4aa60717f19875ddff7b41530e0592c422ed0eb50a525e682f&=&format=webp&quality=lossless&width=1167&height=655">

<img src="https://media.discordapp.net/attachments/1138644058898694149/1208865127894614056/image.png?ex=65e4d662&is=65d26162&hm=be788097c24265ca20cb76ed74196aa852a7fcec38a7a33e0e7fb52c2f0ac276&=&format=webp&quality=lossless&width=825&height=463">




