from typing import Generic, Optional, TypeVar
from uuid import UUID
from pydantic import BaseModel
from abc import ABC, abstractmethod

T = TypeVar('T', bound=BaseModel)


class ResouceSample(BaseModel):
    user: str


class NbResourceAbstract(ABC, Generic[T]):
    """
    redis map
    | key's name                  | content           |
    | --------------------------- | ----------------- |
    | {resource_name}-{id}        | {Resource Object} |
    | {resource_name}-name-{name} | {resouce_name}_id |
    | --------------------------- | ----------------- |
    """
    @abstractmethod
    def load_table_to_redis(self) -> None:
        pass

    @abstractmethod
    def get(self, id: Optional[UUID] = None, name: Optional[str] = None) -> Optional[T]:
        pass

    @abstractmethod
    def get_resource_from_redis_by_id(self, id: UUID) -> Optional[T]:
        pass
   
    @abstractmethod
    def get_id_from_redis_by_name(self, name: str) -> Optional[T]:
        pass
    
    @abstractmethod
    def get_resource_from_db_by_id(self, id: UUID) -> Optional[T]:
        pass

    @abstractmethod
    def get_resource_from_db_by_name(self, id: UUID) -> Optional[T]:
        pass

    @abstractmethod
    def set(self, obj: T) -> T:
        pass
    
class NbResouceService(NbResourceAbstract[ResouceSample]):
    pass
