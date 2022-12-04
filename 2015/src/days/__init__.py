import os

# List all .py files in this directory
__all__ = [f[:-3] for f in os.listdir(os.path.dirname(__file__))
              if f.endswith('.py') and f != '__init__.py' and f != 'day.py']

__all__.sort()

# Import all .py files in this directory
for module in __all__:
    exec(f'from . import {module}')
