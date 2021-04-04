
from pathlib import Path

p = Path('.', 'bot', 'resources')
print([x for x in p.iterdir()])
