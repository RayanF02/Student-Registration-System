# Student Registration System

This project is a Python-based Student Registration System that allows users to manage students, courses, and registration data using text files. The application demonstrates core programming concepts such as file handling, dictionaries, exception handling, and data management.

## Features

- Register new students
- Remove students from the system
- Add courses to existing students
- Display student course information
- Track repeated courses
- Display remaining courses until graduation
- Save updated data to files

## Concepts Used

This project demonstrates several important Python concepts, including:

- Dictionaries
- Functions
- File handling
- Exception handling
- Input validation
- Loops and conditionals
- Data persistence

## File Structure

The program uses two text files:

### `courses.txt`

Stores:
- Course IDs
- Course titles
- Prerequisites

### `students.txt`

Stores:
- Student IDs
- Student names
- Completed courses

## How It Works

When the program starts:

1. Course data is loaded from `courses.txt`
2. Student data is loaded from `students.txt`

Users can then:
- View student courses
- Register students in courses
- Add new students
- Remove students
- View repeated courses

When exiting with saving enabled, all updated student data is written back to `students.txt`.

## Custom Exceptions

The program includes custom exceptions:

- `StudentExistsError`
- `StudentNotExistsError`

These help improve error handling and program reliability.

## How to Run

From the project folder:

```bash
python src/main.py
```

## Future Improvements

Possible future improvements include:

- Graphical User Interface (GUI)
- Database integration
- Search functionality
- Sorting and filtering students
