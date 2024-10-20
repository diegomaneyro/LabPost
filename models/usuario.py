class Usuario:    
    """
    Clase para representar un usuario.

    Atributos:
    -----------
    id_usuario : int
        ID del usuario.
    username : str
        Nombre de usuario.
    password : str
        Contraseña del usuario.
    """
    def __init__(self,id_usuario= None, username = None, password = None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password
    """
        Inicializa un nuevo usuario.

        Parámetros:
        -----------
        id_usuario : int, opcional
            ID del usuario (por defecto None).
        username : str, opcional
            Nombre de usuario (por defecto None).
        password : str, opcional
            Contraseña del usuario (por defecto None).
    """

    def __str__(self):
        return f'Id_usuario: {self._id_usuario}, username: {self._username}, password: {self._password}'

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password
