# Python RegEx Exercises

## 1. Match 'a' followed by zero or more 'b'

```python
import re

pattern = r"ab*"
text = "abbb"
print(bool(re.match(pattern, text)))
```

## 2. Match 'a' followed by two to three 'b'

```python
pattern = r"ab{2,3}"
text = "abbb"
print(bool(re.match(pattern, text)))
```

## 3. Find sequences of lowercase letters joined with underscore

```python
text = "hello_world test_string example_text"
pattern = r"[a-z]+_[a-z]+"

print(re.findall(pattern, text))
```

## 4. Find sequences of one uppercase letter followed by lowercase letters

```python
text = "Hello World Python Regex"
pattern = r"[A-Z][a-z]+"

print(re.findall(pattern, text))
```

## 5. Match 'a' followed by anything ending in 'b'

```python
pattern = r"a.*b"
text = "axxxb"

print(bool(re.match(pattern, text)))
```

## 6. Replace space, comma or dot with colon

```python
text = "Hello, world. Python is fun"

result = re.sub(r"[ ,\.]", ":", text)
print(result)
```

## 7. Convert snake_case to camelCase

```python
def snake_to_camel(text):
    return re.sub(r"_([a-z])", lambda m: m.group(1).upper(), text)

print(snake_to_camel("hello_world_python"))
```

## 8. Split string at uppercase letters

```python
text = "HelloWorldPython"

result = re.split(r"(?=[A-Z])", text)
print(result)
```

## 9. Insert spaces between words starting with capital letters

```python
text = "HelloWorldPython"

result = re.sub(r"([A-Z])", r" \1", text).strip()
print(result)
```

## 10. Convert camelCase to snake_case

```python
def camel_to_snake(text):
    return re.sub(r"([A-Z])", r"_\1", text).lower()

print(camel_to_snake("helloWorldPython"))
```
