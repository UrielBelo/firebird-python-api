import fdb

class FirebirdConnection:
    host:str
    path:str
    port:int
    user:str
    pswo:str
    enco:str

    connection:fdb.Connection

    def __init__(self,host:str,path:str,port:int,user:str,pswo:str,enco:str) -> None:
        self.host = host
        self.path = path
        self.port = port
        self.user = user
        self.pswo = pswo
        self.enco = enco
        self.connection = fdb.connect(
            dsn=host + ':' + path,
            port=port,
            user=user,
            password=pswo,
            charset=enco,
            fb_library_name='C:/Program Files/Firebird/Firebird_2_5/bin/fbclient.dll',
            )
    
    def query(self,query:str,params:tuple):
        cursor:fdb.Cursor = self.connection.cursor()
        cursor.execute(query,params)

        result:list = cursor.fetchallmap()

        return result
    
    def exec(self,query:str,params:tuple):
        cursor:fdb.Cursor = self.connection.cursor()
        cursor.execute(query,params)

    def insert(self,table:str,registers:dict):
        columns:list = registers.keys()
        values:list = registers.values()
        quotes:list = []
        for c in values:
            quotes.append('?')

        columnsList:str = ','.join(columns)
        quotesList:str = ','.join(quotes)

        finalQuery:str  = 'INSERT INTO {}({}) VALUES({})'.format(table,columnsList,quotesList)
        self.exec(finalQuery,tuple(values))

    def update(self,table:str,register:dict,where:dict):
        columnsRegister:list = register.keys()
        valuesRegister:list = register.values()

        columnsWhere:list = where.keys()
        valuesWhere:list = where.values()

        updatesList:list = []
        for x in columnsRegister:
            updatesList.append('{} = ?'.format(x))
        updateListString:str = ','.join(updatesList)

        whereString:str = ''
        counterRow:int = 0
        for x in columnsWhere:
            if(counterRow == 0):
                whereString += ' WHERE '
            else:
                whereString += ' AND '
            whereString += '{} = ?'.format(x)
            counterRow += 1

        finalQuery:str = 'UPDATE {} SET {} {}'.format(table,updateListString,whereString)

        finalTuple:tuple = tuple(list(valuesRegister) + list(valuesWhere))
        self.exec(finalQuery,finalTuple)