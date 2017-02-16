# path

## Current directory path

`os.path.abspath(os.path.dirname(__file__))`

## Add library path.

```py
import sys
import os

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root, "libs"))
```
