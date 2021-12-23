class ServerError(Exception):
    def __init__(self, message: str = 'Erro Interno no servidor'):
        self.message = message
        super().__init__(self.message)
