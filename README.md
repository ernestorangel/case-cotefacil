# case-cotefacil

Nesse repositório vocês encontrarão as minhas soluções para as questões propostas no case da Cote Fácil.

O case foi proposto no dia 11/10/2023 para ser entregue inicialmente até o dia 18/10/2023.

## Questão 1

**Resolvida parcialmente como pedido.** :warning:

O projeto foi iniciado usando o startproject do próprio Scrapy.

Dessa forma, para executar basta estar no diretório questao1/compreagora e executar o comando abaixo:

```
scrapy crawl products
```

_Obs.: Ao invés de trazer as informações no terminal, faz o output de um arquivo json com os arquivos capturados separados por categoria._

## Questão 2

**Resolvida exatamente como pedido.** :heavy_check_mark:

O projeto foi iniciado usando o startproject do próprio Scrapy.

Nesse caso, no entanto, foi utilizado o Docker para disponibilizar a montagem da imagem.

Basta buildar a imagem a partir do diretório em que se encontra o Dockerfile (questao2/pedidoeletronico), com o seguindo comando:

```
docker build -t <nome-da-imagem> .
```

E aí é possível, em seguida, usar o comando:

```
docker run <nome-da-imagem> <numero-do-pedido>
```

_Para que essa implementação se tornasse funcional, no entando, foi necessário a utilização de um script bash_

## Questão 3

**Não resolvida** :x:

_Após diversas tentativas foi percebido que o site e as credenciais passadas provavelmente não estão corretas._

## Questão 4

**Resolvida exatamente como pedido.** :heavy_check_mark:

Para abrir o arquivo .jar, que é o empacotamento do Java, foi utilizado o decompiler.

Após visualizar os arquivos escritos em Java foi possível obter um Host, Usuario e Senha para conexão com FTP.

Ao conectar, havia um arquivo .txt e As informações extraidas do arquivo estão no arquivo de texto Questao4.txt

_obs.: ao conectar também percebi a existência de uma pasta vazia junto ao arquivo mencionado acima_

## Questão 5

**Resolvida exatamente como pedido.** :heavy_check_mark:

No repostiório da questao5 se encontra no arquivo main.py a implementação de uma árvore binária.

Essa estrutura de dados armazena os dados em nós que possuem um nó esquerdo e um nó direito, ambos filhos. Nos nós esquerdos se armazena os valores menores que o nó pai, e no nó direito os valores maiores ou iguais.

Foi implementado apenas os métodos de inserção, remoção, busca e travessia em ordem.

Além disso, existem alguns testes unitários simples para comprovar o funcionamento dos métodos implementados.

Para rodar o os testes basta estar na pasta da questao5 e executar:

```
python main.py
```

## Questão 6

**Resolvida exatamente como pedido.** :heavy_check_mark:

Foi utilizado o Selenium para manipular o Chrome e percorrer as paginas procurando pelas frases e , ao final, ir a pagina de detalhes e extrair o restante das informações.

Para executar basta entrar na pasta da questao6 e executar:

```
python main.py <nome-do-autor>
```

## Questão 7

**Resolvida exatamente como pedido.** :heavy_check_mark:

Na pasta da questao7 existe um arquivo Questao7.txt com a resposta da questão.
