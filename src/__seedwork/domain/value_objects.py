from dataclasses import dataclass, field
import uuid

from __seedwork.domain.exceptions import InvalidUuidException

@dataclass()
class UniqueEntityId:
    
    id: str = field(default_factory = lambda: str(uuid.uuid4()))
    
    def __post_init__(self):
        if isinstance(self.id, uuid.UUID):
            self.id = str(self.id)
        else:
            self.id = self.id
        self.__validate()
        
    def __validate(self):
        try:
            uuid.UUID(self.id)
        except ValueError as ex:
            raise InvalidUuidException() from ex
        