## pyRukassa
This is a Python wrapper for the Rukassa API.

## Installation

```bash
pip install git+https://github.com/kavinari/pyRukassa
```

## Usage

```python
from rukassa import RukassaAPI, ValueNotReceived

api = RukassaAPI(token='your_token', shop_id=123)
# Exception
try:
  payment_info = api.get_payment_info()
except ValueNotReceived as error:
  print(error.message)
# Create payment
create_payment = api.create_payment(order_id=456, amount=100, method='card', data={})
print(create_payment)

# Get payment info
payment_info = api.get_payment_info(payment_id=789)
print(payment_info)

# Get withdraw info
withdraw_info = api.get_withdraw_info(withdraw_id=123)
print(withdraw_info)

# Get balance
balance = api.get_balance(email='your_email', password='your_password')
print(balance)
  
# Create withdraw
withdraw_result = api.create_withdraw(email='your_email', password='your_password', way='way', wallet='wallet',
amount=100, from_='from', who_fee=1)
print(withdraw_result)
```

## API Reference

### RukassaAPI

#### `__init__(self, token: str, shop_id: int)`

Constructor for `RukassaAPI` wrapper class.

##### Parameters:

- `token` (str): API token provided by Rukassa.
- `shop_id` (int): Shop ID provided by Rukassa.

#### `create_payment(self, payment_data: PaymentData, method: str = None, data: Dict = None) -> Union[Dict, APIError]`

Create payment.

##### Parameters:

- `payment_data` (PaymentData): Payment data object.
- `method` (str): Payment method. Optional.
- `data` (Dict): Payment data. Optional.

##### Returns:

- Union[Dict, APIError]: Payment info or API error.

#### `get_payment_info(self, id: int) -> Union[PaymentInfo, APIError]`

Get payment info.

##### Parameters:

- `id` (int): Payment ID.

##### Returns:

- Union[PaymentInfo, APIError]: Payment info or API error.

#### `get_withdraw_info(self, id: int) -> Union[WithdrawInfo, APIError]`

Get withdraw info.

##### Parameters:

- `id` (int): Withdraw ID.

##### Returns:

- Union[WithdrawInfo, APIError]: Withdraw info or API error.

#### `get_balance(self, email: str, password: str) -> Union[BalanceInfo, APIError]`

Get balance.

##### Parameters:

- `email` (str): User email.
- `password` (str): User password.

##### Returns:

- Union[BalanceInfo, APIError]: Balance info or API error.

#### `create_withdraw(self, email: str, password: str, way: str, wallet: str, amount: float, from_: str = None, who_fee: int = None) -> Union[WithdrawResult, APIError]`

Create withdraw.

##### Parameters:

- `email` (str): User email.
- `password` (str): User password.
- `way` (str): Withdraw way.
- `wallet` (str): Withdraw wallet.
- `amount` (float): Withdraw amount.
- `from_` (str): Withdraw from. Optional.
- `who_fee` (int): Withdraw who fee. Optional.

##### Returns:

- Union[WithdrawResult, APIError]: Withdraw result or API error.

### PaymentData

Payment data object.

#### Parameters:

- `order_id` (int): Order ID.
- `amount` (float): Payment amount.
- `method` (str): Payment method. Optional.
- `data` (Dict): Payment data. Optional.

### PaymentInfo

Payment info object.

#### Parameters:

- `id` (int): Payment ID.
- `order_id` (int): Order ID.
- `amount` (float): Payment amount.
- `status` (str): Payment status.
- `data` (Dict): Payment data.

### WithdrawInfo

Withdraw info object.

#### Parameters:

- `id` (int): Withdraw ID.
- `amount` (float): Withdraw amount.
- `fee` (float): Withdraw fee.
- `way` (str): Withdraw way.
- `who_fee` (str): Withdraw who fee.
- `status` (str): Withdraw status.

### BalanceInfo

Balance info object.

#### Parameters:

- `balance` (float): User balance.

### WithdrawResult

Withdraw result object.

#### Parameters:

- `id` (int): Withdraw ID.
- `status` (str): Withdraw status.

### APIError

API error object.

#### Parameters:

- `error_code` (int): Error code.
- `message` (str): Error message.

