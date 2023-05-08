from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class PaymentCreated:
    id: int
    url: str

@dataclass
class PaymentData:
    shop_id: int
    order_id: int
    amount: float
    token: str
    method: str
    data: Dict

@dataclass
class PaymentInfo:
    id: int
    order_id: int
    amount: float
    status: str
    data: Dict

@dataclass
class WithdrawInfo:
    id: int
    amount: float
    fee: float
    way: str
    who_fee: str
    status: str

@dataclass
class BalanceInfo:
    balance: float

@dataclass
class WithdrawResult:
    id: int
    status: str

@dataclass
class APIError(Exception):
    def __init__(self, error_code: int, message: str):
        self.error_code = error_code
        self.message = message

    def __str__(self):
        return f"{self.error_code}: {self.message}"

    @classmethod
    def create(cls, error_code: int, message: str):
        if error_code == 100:
            return ValueNotReceived(message)
        elif error_code == 200:
            return StoreOrPaymentNotFound(message)
        elif error_code == 300:
            return MerchantNotVerified(message)
        else:
            return OtherError(message)

    def __subclasshook__(self, subclass):
        return issubclass(subclass, APIError)

@dataclass
class ValueNotReceived(APIError):
    def __init__(self, message: str):
        super().__init__(100, message)
    
    def __str__(self):
        return f"{self.error_code}: {self.message}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.error_code}, {self.message})"

    def __subclasshook__(self, subclass):
        return issubclass(subclass, ValueNotReceived)

@dataclass
class StoreOrPaymentNotFound(APIError):
    def __init__(self, message: str):
        super().__init__(200, message)
    
    def __str__(self):
        return f"{self.error_code}: {self.message}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.error_code}, {self.message})"

    def __subclasshook__(self, subclass):
        return issubclass(subclass, StoreOrPaymentNotFound)

@dataclass
class MerchantNotVerified(APIError):
    def __init__(self, message: str):
        super().__init__(300, message)

    def __str__(self):
        return f"{self.error_code}: {self.message}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.error_code}, {self.message})"

    def __subclasshook__(self, subclass):
        return issubclass(subclass, MerchantNotVerified)

@dataclass
class OtherError(APIError):
    def __init__(self, message: str):
        super().__init__(400, message)

    def __str__(self):
        return f"{self.error_code}: {self.message}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.error_code}, {self.message})"

    def __subclasshook__(self, subclass):
        return issubclass(subclass, OtherError)
