# dataclasses
使用装饰器给类添加通用方法

+ dataclass
+ asdict
+ astuple
+ ...



```python
@dataclass
class InventoryItem:
'''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```
