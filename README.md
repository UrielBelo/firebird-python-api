# Firebird Python API

~~~python
#Importação da Conexão
from firebird import FirebirdConnection

#Criar Conexão com o banco de Dados
myDb:FirebirdConnection = FirebirdConnection(
    '127.0.0.1',        #Host
    'C:/DATABASE.FDB',  #Caminho
    3050,               #Porta
    'SYSDBA',           #Usuário
    'masterkey',        #Senha
    'WIN1252',          #Charset
)

#Exemplo de Query
result:list = myDb.query('SELECT COLUNA1,COLUNA2 FROM TABELA WHERE COLUNA3 = ?', ("VALOR"))

#Retorna uma lista de dicionários
for x in result:
    print(x['COLUN1'])
    print(x['COLUN2'])

#Exemplo de Insert (Tabela, Dicionário<Nome da Coluna, Valor>)
myDb.insert('TABELA',{
    "COLUNA1":"VALOR1",
    "COLUNA2":"VALOR2"
})

#Exemplo de Update (Tabela, Dicionário<Nome da Coluna, Valores, Condições>)
myDb.update('TABELA',{
    "COLUNA1":"VALOR1",
    "COLUNA2":"VALOR2"
},{
    "COLUNA3":"VALOR3"
})
~~~