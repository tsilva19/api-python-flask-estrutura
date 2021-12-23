class NotFoundError(Exception):
    def __init__(self, message: str = 'Recurso não Encontrado'):
        self.message = message
        super().__init__(self.message)
