class InvalidUuidException(Exception):
    def __init__(self, error = 'ID  must be a invalid UUID') -> None:
        super().__init__(error)