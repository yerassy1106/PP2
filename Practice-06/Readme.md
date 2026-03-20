# Practice 6: Python File Handling and Built-in Functions

This repository contains completed exercises for Practice 6, focusing on file system operations and functional programming tools in Python.

## 📁 Project Structure

Practice6/
├── file_handling/
│   ├── read_files.py         # Reading files using read(), readline(), and readlines()
│   ├── write_files.py        # Demonstrating 'w' (write) and 'a' (append) modes
│   └── copy_delete_files.py  # File operations using os and shutil
├── directory_management/
│   ├── create_list_dirs.py   # Working with os.makedirs and listing files
│   └── move_files.py         # Moving and renaming files
├── builtin_functions/
│   ├── map_filter_reduce.py  # Functional programming examples
│   └── enumerate_zip_examples.py # Paired iteration and type conversion
└── README.md

---

## 🛠️ Key Concepts Covered

### 1. File Handling
- **Context Managers:** Using `with open(...)` to ensure files are closed properly.
- **Modes:** - `r`: Read (default).
  - `w`: Write (overwrites).
  - `a`: Append (adds to the end).
- **Operations:** Copying and deleting files safely by checking `os.path.exists()`.

### 2. Directory Management
- **Recursive Creation:** Using `os.makedirs(..., exist_ok=True)` to create nested paths.
- **Filtering:** Using list comprehensions and `.endswith()` to find specific file types.

### 3. Built-in Functions
- **map()**: Applying a function to all items in a list.
- **filter()**: Extracting items that meet a specific condition.
- **reduce()**: Cumulatively performing operations (from `functools`).
- **zip() & enumerate()**: Efficient tools for loops and data pairing.

---

## 🚀 How to Run
1. Clone the repository.
2. Navigate to the specific folder.
3. Run scripts using:
   ```bash
   python filename.py
   