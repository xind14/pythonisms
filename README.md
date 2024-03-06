# Lab: Class 42 - Pythonisms

## Author: Xin Deng

### Links and Resources

- chatGPT
- [Class 42 Demo](https://github.com/codefellows/seattle-code-python-401d24/tree/main/class-42/demo)


### Overview - Pythonisms

The Pythonisms lab explores the elegant features of Python that distinguish a mere "programmer who uses Python" from a true "Pythonista." A Pythonista can leverage Python's specific features to accomplish tasks in a simpler and more straightforward manner.

#### Version 1.0

Build 1.0 Feature Tasks

1. Use iterators/generators on a custom collection to:
    - Enable usage in a for loop.
    - Allow usage in a list comprehension.
    - Provide the ability to convert to a list or other collection type.
2. Create a decorator to add behavior to a function, such as:
    - Calculating the time spent in the function.
3. Use dunder methods to make code more readable and elegant, including:
    - Allowing two custom data structures to be considered equal.
    - Providing the ability for a custom data structure to be considered truthy/falsy.

### Findings

1. From my understanding iterators internally creates an iterator to go through each item in a sequence of something. It makes traversing things easier

2. Generators provide readable code to create iterators. 

3. Dunders are just special methods to define class behavior.

4. I need more examples of how these can be used in code when we create actual projects like how could they have been used in the cookie stand api and admin labs? 

5. I still have trouble creating tests. I think it's my weakest point and need gpt help every time. 


### How to Initialize/Run Application

python3 -m venv .venv

source .venv/bin/activate

### How to test

pytest -k main.py