# Object-Oriented-Project: Painting Gallery Program

## Overview

This project was created for an Object-Oriented Programming assignment and demonstrates the use of classes, inheritance, polymorphism, method overriding, encapsulation, and UML design in Python.

The program allows users to create different types of paintings and store them in a gallery. Users can choose from three painting categories:

- PortraitPainting
- LandscapePainting
- AbstractPainting

Each painting type inherits common attributes and methods from the `Painting` superclass while also providing its own specialized behavior.

---

## Features

### Superclass: Painting
The `Painting` superclass contains common information shared by all paintings:

- Title
- Medium
- Hours
- Minutes
- Complexity Level

Methods:
- `describePainting()`
- `estimateDifficulty()`
- `isLongProject()`
- `getTotalMinutes()`
- `__str__()`

---

### Subclasses

#### PortraitPainting
Additional Attribute:
- `subject_name`

Additional Method:
- `identifySubject()`

#### LandscapePainting
Additional Attribute:
- `location`

Additional Method:
- `describeLocation()`

#### AbstractPainting
Additional Attribute:
- `theme`

Additional Method:
- `interpretTheme()`

Each subclass overrides the `describePainting()` method to demonstrate polymorphism.

---

## Object-Oriented Concepts Demonstrated

- Classes and Objects
- Constructors (`__init__`)
- Inheritance
- Polymorphism
- Method Overriding
- Encapsulation
- UML Design
- Input Validation

---

## How to Run

1. Ensure both files are in the same folder:
   - `objects_Painting.py`
   - `main_Painting.py`

2. Open a terminal in the project directory.

3. Run the program:

```bash   
python main_Painting.py
