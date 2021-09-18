# TypedList
A way to created Typed Lists in Python

Example uses:

```python
IntList = TypedList(int)
list1 = IntList()
list1.append(1)
list1.append(2)
list1.append(3)
print(list1)
list1.append("Hello") #This will raise an error
```

```python
StrList = TypedList(str)
s = StrList(["Hello", "World"])
print(1 in s)
print("World" in s)
s.append("Goodbye")
print(s)
```
