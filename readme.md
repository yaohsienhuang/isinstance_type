# isinstance type
實作一個辨別 class 或 fuction 中 的argument type 的裝飾器
## 使用方式：
```python=
from dataclasses import dataclass

@isinstance_type
@dataclass
class demo_class:
    name:str
    age:int

person1=demo_class('Jacky','34')
```
## output:
```python=
AssertionError: age must be <class 'int'>
```

