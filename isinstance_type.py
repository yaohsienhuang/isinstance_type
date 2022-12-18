from dataclasses import dataclass

def isinstance_type(obj):
    def inner(*args, **kwargs):
        if kwargs:
            for k,v in kwargs.items():
                assert isinstance(v,obj.__annotations__[k]) , f'{k} must be {obj.__annotations__[k]}'
        if args:
            for i in range(len(args)):
                k=list(obj.__annotations__.keys())[i]
                assert isinstance(args[i],obj.__annotations__[k]) , f'{k} must be {obj.__annotations__[k]}'
        instance=obj(*args, **kwargs)
        return instance
    return inner
    
@isinstance_type
@dataclass
class demo_class:
    name:str
    age:int

@isinstance_type
def demo_func(name:str,age:int):
    print(f'{name} is {age} years old.')

if __name__ == '__main__':
    
    person1=demo_class('Jacky','34')
    print(f'{person1.name} is {person1.age} years old.')
    
    person1=demo_func('Sean','33')
    