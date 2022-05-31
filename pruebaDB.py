import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='sica'
        )

        self.cursor = self.connection.cursor()

        print("conexion correcta")

    def select_user(self, codigo):
        sql = 'SELECT id_codigo, nombre, apellidos, tipo FROM usuarios WHERE id_codigo = {}'.format(codigo)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            
            id= (user[0])
            print(id)
            nombres= (user[1])
            print(nombres)
            apellidos= (user[2])
            print(apellidos)
            tipo= (user[3])
            print(tipo)

            return True
        except:
            print("error, usuario no encontrado")
            return False

    def select_nombres(self, codigo):
        sql = 'SELECT nombre FROM usuarios WHERE id_codigo = {}'.format(codigo)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            
            nombres= (user[0])
            print(nombres)

            return True
        except:
            print("error, usuario no encontrado")
            return False
    
    def select_apellidos(self, codigo):
        sql = 'SELECT apellidos FROM usuarios WHERE id_codigo = {}'.format(codigo)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            
            nombres= (user[0])
            print(nombres)

            return True
        except:
            print("error, usuario no encontrado")
            return False
        
    def select_tipo(self, codigo):
        sql = 'SELECT tipo FROM usuarios WHERE id_codigo = {}'.format(codigo)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
        
            nombres= (user[0])
            print(nombres)

            return True
        except:
            print("error, usuario no encontrado")
            return False

    def select_all_users(self):
        sql = 'SELECT id, codigo, fecha FROM usuarios'

        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()

            for user in users:
                print("Id: ", user[0])
                print("Código: ", user[1])
                print("Fecha: ", user[2])
                print("_____\n")
        except:
            print("error all users")
    
    def uptade_user(self, id, codigo):
        sql = "UPDATE usuarios SET codigo='{}'WHERE id={}".format(codigo, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except:
            print("ERROR IN UPTATE")

    def close(self):
        self.connection.close()


database = Database()


