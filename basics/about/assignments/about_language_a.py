"""
* Assignment: About Environment
* Complexity: easy
* Lines of code: 0 lines
* Time: 3 min

English:
    1. Create file `about_env.py`
    2. Run file in your IDE
    3. Where Python is installed?
    4. Are you using "venv"?
    5. Make sure, `venv` is not `None`
    6. Run doctests - all must succeed

Polish:
    1. Stwórz plik `about_env.py`
    2. Uruchom plik w swoim IDE
    3. Gdzie Python jest zainstalowany?
    4. Czy korzystasz z "venv"?
    5. Upewnij się, że `venv` nie jest `None`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert python_executable
    >>> assert python_version
"""

import sys
import os


python_executable = sys.executable
python_version = tuple(sys.version_info)
venv = os.getenv("VIRTUAL_ENV")

# Solution
python_executable = sys.executable
python_version = tuple(sys.version_info)
venv = os.getenv("VIRTUAL_ENV")
