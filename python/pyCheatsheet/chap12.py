from dataclasses import dataclass
from typing import Any

@dataclass
class Number:
  val: int = 0

obj = Number(2)
print(obj.val)

