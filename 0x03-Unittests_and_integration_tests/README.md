🧪 Testing Project Overview
This project demonstrates the differences and applications of unit testing and integration testing in Python using the unittest framework.

📌 Learning Objectives
By the end of this project, you will be able to explain:

The difference between unit tests and integration tests.

How to use common testing patterns like mocking, parameterization, and fixtures.

🧰 Tools and Requirements
Python version: 3.7

Test Framework: unittest

Code Style: pycodestyle (version 2.5)

OS Environment: Ubuntu 18.04 LTS

All files must:

Be executable

End with a new line

Start with #!/usr/bin/env python3

Have proper module, class, and function docstrings

Include type annotations

📂 Files
utils.py: Contains helper functions like access_nested_map.

client.py: Client-related logic to test.

fixtures.py: Contains test data or static responses used in integration tests.

test_utils.py: Contains unit tests, particularly for utils.py.

🧪 Testing Instructions
To run your tests:

bash
Copy
Edit
$ python -m unittest path/to/test_file.py
📚 Resources
unittest documentation

unittest.mock

parameterized

Memoization in Python