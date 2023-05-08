import requests
from typing import Dict, Any, Union
from .typing import PaymentCreated, PaymentData, APIError, PaymentInfo, WithdrawInfo, BalanceInfo, WithdrawResult


class RukassaAPI:
    base_url = 'https://lk.rukassa.pro/api/v1/'

    def __init__(self, token: str, shop_id: int):
        self.token = token
        self.shop_id = shop_id

    def create_payment(self, payment_data: PaymentData, method: str = None, data: Dict = None) -> Union[Dict, APIError]:
        url = self.base_url + 'create'
        payload = {
            "shop_id": self.shop_id,
            "order_id": payment_data.order_id,
            "amount": payment_data.amount,
            "token": self.token,
            "method": method,
            "data": data
        }
        response = requests.post(url, json=payload)
        if response.ok:
            return PaymentCreated(**response.json())
        else:
            return APIError(response.status_code, response.text)

    def get_payment_info(self, id: int) -> Union[PaymentInfo, APIError]:
        url = self.base_url + 'getPayInfo'
        payload = {
            "id": id,
            "shop_id": self.shop_id,
            "token": self.token
        }
        response = requests.post(url, json=payload)
        if response.ok:
            return PaymentInfo(**response.json())
        else:
            return APIError(response.status_code, response.text)

    def get_withdraw_info(self, id: int) -> Union[WithdrawInfo, APIError]:
        url = self.base_url + 'getWithdrawInfo'
        payload = {
            "id": id,
            "shop_id": self.shop_id,
            "token": self.token
        }
        response = requests.post(url, json=payload)
        if response.ok:
            return WithdrawInfo(**response.json())
        else:
            return APIError(response.status_code, response.text)

    def get_balance(self, email: str, password: str) -> Union[BalanceInfo, APIError]:
        url = self.base_url + 'getBalance'
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(url, json=payload)
        if response.ok:
            return BalanceInfo(**response.json())
        else:
            return APIError(response.status_code, response.text)

    def create_withdraw(self, email: str, password: str, way: str, wallet: str, amount: float,
                        from_: str = None, who_fee: int = None) -> Union[WithdrawResult, APIError]:
        url = self.base_url + 'createWithdraw'
        payload = {
            "email": email,
            "password": password,
            "way": way,
            "wallet": wallet,
            "amount": amount,
            "from": from_,
            "who_fee": who_fee
        }
        response = requests.post(url, json=payload)
        if response.ok:
            return WithdrawResult(**response.json())
        else:
            return APIError(response.status_code, response.text)
