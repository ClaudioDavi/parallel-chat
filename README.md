### Trabalho final de processamento paralelo

Aplicação de Chat com multi threading e sockets

Esta aplicação usa a biblioteca padrão do Python usando python 3.5+

Para rodar basta rodar o server primeiro:

`python server.py -a localhost -p 5432`

depois disso conectar o cliente:

`python client.py -a localhost -p 5432`

O argumento `-a` é para o endereço onde o server está rodando (Você pode verificar na linha de comando do servidor) e o argumento `-p` é para a porta

Para verificar as opções e os defaults basta digitar 

`python server.py -h`
`python client.py -h`
