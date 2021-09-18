from collections.abc import MutableSequence

class TypedList:
    "Creates a class which creates instances of a typed list"
    
    def __new__(cls, typ):
        if not isinstance(typ, type):
            raise TypeError("a class type is required")
        
        class TypedListImpl(MutableSequence):
            __doc__ = f"A list which only accepts values of type '{typ.__name__}'"
            
            def __init__(self, sequence=[]):
                self._type = typ
                self._data = [self._type_check(v) for v in sequence]
                
            def _type_check(self, value):
                if not isinstance(value, self._type):
                    raise TypeError("value must be of type '%s'" % self._type.__name__)
                return value
                
            def __setitem__(self, index, value):
                self._type_check(value)
                self._data[index] = value
                
            def __getitem__(self, index) -> typ:
                return self._data[index]
                
            def __delitem__(self, index):
                del self._data[index]
                
            def __contains__(self, value):
                #Check the simple case first
                if not isinstance(value, self._type):
                    return False
                return value in self._data
                
            def __len__(self):
                return len(self._data)
                
            def clear(self):
                self._data.clear()
                
            def insert(self, index, value):
                self._type_check(value)
                self._data.insert(index, value)
                
            def __str__(self):
                return str(self._data)
                
            def __repr__(self):
                return f"<TypedList '{self._type.__name__}', {self._data}>"
                
        return TypedListImpl
        
__all__ = ["TypedList"]
