# Como rodar o projeto?

Requisitos: Node instalado na máquina + mysql

1 - clonar o repositório em seu local de preferência <br>
2 - rodar <b>npm i</b> para instalar a node_modules <br>
3 - copiar o .env.example e renomear para .env ex: <br> ![image](https://user-images.githubusercontent.com/61751830/230465725-2c14ee50-4214-49da-804f-693d3b58eabd.png) <br>
4 - criar conexão no mysql conforme os dados que foram passado no arquivo .env <br>
5 - executar o <b>sql_script.sql</b> para criação do banco de dados e tabela(adaptando para o nome que for usar no DB) <br>
6 - utilizando o comando <b>npm start</b> ja será possivel ter o backend rodando em localhost, na porta em que foi selecionada(no meu caso utilizei a porta 8000)



# Endpoints

GET <a>http://localhost:8000/artigos</a> : Retorna todos os artigos, em ordem do mais recente ao mais velho. ex: <br>
![image](https://user-images.githubusercontent.com/61751830/230467472-6f3492dc-eb4f-483e-99f2-c09d1732fccb.png)
<br>
GET <a>http://localhost:8000/artigos/:category</a> : Filtro para retorna de todos os artigos de uma categoria especifica. ex: <br>
![image](https://user-images.githubusercontent.com/61751830/230468568-c7195088-1aa7-4618-8868-80517212ecb3.png)<br>
![image](https://user-images.githubusercontent.com/61751830/230467789-4cd65fc3-cd7b-4205-bb64-302db2fced54.png)
<br>
GET <a>http://localhost:8000/artigos/title/:title</a> : Retorno de artigos pela busca de palavras/carácteres no titulo. ex: <br>
![image](https://user-images.githubusercontent.com/61751830/230468414-a869a4b2-7a83-4394-bbac-ebb78438b971.png)<br>
![image](https://user-images.githubusercontent.com/61751830/230468347-12d19980-d4b6-4801-8441-04ae40a5192f.png)

# Rodando o scprit python
<br>
Para rodar o script utilizei a IDE spyder <br>
<br>
Existem 2 alterações a serem feitas:<br>
<br>
1 - Caso tenha alterado o numero da porta que o servidor estará rodando alterar a linha 15 <br>
![image](https://user-images.githubusercontent.com/61751830/230469662-309b5d66-ac7c-4331-bcc3-6bb82e55c484.png) <br>
<br>
2 - Alterar a linha 67 para gerar o arquivo CSV na pasta em que preferir(caso mantenha deste jeito haverá erro)<br>
![image](https://user-images.githubusercontent.com/61751830/230470138-95547844-f9ba-4ded-a344-21e1b4cc8a26.png)

