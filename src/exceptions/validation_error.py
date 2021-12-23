class ValidationError(Exception):
    def __init__(self, message: str = 'Erro de Validação'):
        self.message = message
        super().__init__(self.message)
