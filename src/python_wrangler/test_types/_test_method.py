from functools import wraps
import sys
sys.path.extend(["src/python_wrangler"])
from _affirm_error import AffirmError
from _test_type_interface import TestTypeIterface
from _settings import TestTypeSettings

class TestMethod(TestTypeIterface):

    def __init__(self, func, settings: TestTypeSettings) -> None:
        super().__init__(func, settings)

    def __getattr__(self, name):
        return getattr(self._func, name)
    
    def __call__(self, *args, **kwargs):
        return self.test(*args, **kwargs)
    
    def _print_result(self, prefix: str):
        method_path = "::".join(self._function_path)
        print(f"|{prefix}|: {method_path}")

    def test(self, *args, **kwargs):
        try:
            return_value = self._func(self._func, *args, **kwargs)
        except AffirmError as err:
            self._failed(err)
            return None
        else:
            self._success()
        return return_value
    
if __name__ == "__main__":
    pass