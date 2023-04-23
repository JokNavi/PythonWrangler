import sys
import types


class AffirmIsFalse(BaseException):
    # Exception raised if the result of the affirm function is False.
    def __init__(self, message="Affirm retured False!"):
        self.message = message
        self.value = False


def raise_twice(err: AffirmIsFalse):
    try:
        raise err
    except AffirmIsFalse:
        traceback = sys.exc_info()[2]
        back_frame = traceback.tb_frame.f_back.f_back  # each .f_back skips one call
        back_tb = types.TracebackType(tb_next=None,
                                      tb_frame=back_frame,
                                      tb_lasti=back_frame.f_lasti,
                                      tb_lineno=back_frame.f_lineno)
        raise err.with_traceback(back_tb)

# function test decorator
def test(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            if wrapper.verbose:
                print(f"|OK|: {func.__name__}")
        except AffirmIsFalse as err:
            if wrapper.verbose:
                print(f"|ER|: {func.__name__}")
            if wrapper.crash_on_false:
                raise_twice(err)
    wrapper.crash_on_false = True
    wrapper.verbose = True
    return wrapper


def affirm_ne(item, item2, error_message="Affirm_ne returned False."):
    try:
        assert item != item2
    except AssertionError:
        raise_twice(AffirmIsFalse(error_message))


def affirm_eq(item, item2, error_message="Affirm_eq returned False."):
    try:
        assert item == item2
    except AssertionError:
        raise_twice(AffirmIsFalse(error_message))


def affirm(item, error_message="Affirm returned False."):
    try:
        assert item
    except AssertionError:
        raise_twice(AffirmIsFalse(error_message))


if __name__ == "__main__":
    affirm(False)
