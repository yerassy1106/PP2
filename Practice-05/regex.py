import re

def run_exercises():
    # 1. 'a' followed by zero or more 'b's
    # Pattern: a followed by b repeated 0+ times (*)
    def task_1(text):
        return bool(re.search(r'ab*', text))

    # 2. 'a' followed by two to three 'b's
    # Pattern: a followed by b repeated 2 to 3 times {2,3}
    def task_2(text):
        return bool(re.search(r'ab{2,3}', text))

    # 3. Sequences of lowercase letters joined with an underscore
    # Pattern: lowercase+, underscore, lowercase+
    def task_3(text):
        return re.findall(r'[a-z]+_[a-z]+', text)

    # 4. One uppercase letter followed by lowercase letters
    # Pattern: Upper followed by 1 or more lowers
    def task_4(text):
        return re.findall(r'[A-Z][a-z]+', text)

    # 5. 'a' followed by anything, ending in 'b'
    # Pattern: a, then any chars (.*), ending with b ($)
    def task_5(text):
        return bool(re.search(r'a.*b$', text))

    # 6. Replace space, comma, or dot with a colon
    def task_6(text):
        return re.sub(r'[ ,.]', ':', text)

    # 7. Snake case to Camel case
    # Logic: Find _ + letter, capitalize the letter, remove _
    def task_7(text):
        return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), text)

    # 8. Split a string at uppercase letters
    def task_8(text):
        return re.findall(r'[A-Z][^A-Z]*', text)

    # 9. Insert spaces between words starting with capital letters
    def task_9(text):
        return re.sub(r'(\w)([A-Z])', r'\1 \2', text)

    # 10. Camel case to Snake case
    def task_10(text):
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

    # --- Testing the results ---
    print(f"1. Match 'ab*': {task_1('abbb')}")
    print(f"2. Match 'ab{{2,3}}': {task_2('ab')}")
    print(f"3. Lowercase underscore: {task_3('hello_world and python_regex')}")
    print(f"4. Upper followed by lower: {task_4('Apple Banana orange Cherry')}")
    print(f"5. 'a' anything 'b': {task_5('active')}")
    print(f"6. Replace separators: {task_6('Python,exercises.are fun')}")
    print(f"7. Snake to Camel: {task_7('this_is_snake_case')}")
    print(f"8. Split at Upper: {task_8('SplitAtUppercaseLetters')}")
    print(f"9. Spaces between Capitals: {task_9('WordCapitalWord')}")
    print(f"10. Camel to Snake: {task_10('CamelCaseToSnakeCase')}")

if __name__ == "__main__":
    run_exercises()
#```
