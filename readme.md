# isinstance type
實作一個辨別 class 或 fuction 中的 argument type 的裝飾器
## 使用方式：
```python=
from dataclasses import dataclass

@isinstance_type
@dataclass
class demo_class:
    name:str
    age:int

person1=demo_class('Jacky','34') #錯誤例子，age:str
```
## output:
```python=
AssertionError: age must be <class 'int'>
```

