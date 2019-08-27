import sys
print(sys.version)
print(sys.executable)
from pip import _internal
_internal.main(['list'])
