
from dataclasses import dataclass
from typing import Any, List, Optional, Type, TypeVar, Generic


DataT = TypeVar('DataT')

class CustomResponse:
    def __init__(self, data, message: Optional[str] = None, total: Optional[int] = None):
        self.data = data
        if message is not None:
            self.message = message
        if total is not None:
            self.total = total