import pypatt

def match_basic(value):
    with match(value):
        with True:
            return 'True'
        with 10:
            return '10'
        with 'abc':
            return 'abc'    
        with [False, 0]:
            return '[False, 0]'
        with ('blah', True, 10):
            return 'triple'
        with (0, [1, (2, [3, (4,)])]):
            return 'nested'
        # todo name
        # todo quote

def match_many(value):
    # nest match statements on multiple levels
    pass

def match_method(value):
    # decorate class method
    pass

def match_as(value):
    # use with match(expr) _as name_: syntax
    pass

def match_bind(value):
    # test binding the same variable
    pass

def test():
    pass

from pypatt import uncompile, recompile
from types import FunctionType, CodeType

def test_roundtrip():
    import os

    print 'Importing everything in the medicine cabinet:'
    for filename in os.listdir(os.path.dirname(os.__file__)):
        name, ext = os.path.splitext(filename)
        if ext != '.py' or name == 'antigravity':
            continue
        try:
            __import__(name)
        except ImportError:
            pass    # some stuff in system library can't be imported
    print 'Done importing. We apologize for the noise above.\n'

    print 'Round-tripping functions to source code and back:'
    success = 0
    failed = 0
    unsupported = 0
    errors = 0

    import gc
    allfuncs = [obj for obj in gc.get_objects() if type(obj) is FunctionType]

    for func in allfuncs:
        c = func.func_code
        if type(c) is not CodeType:
            continue    # PyPy builtin-code

        try:
            rc = recompile(*uncompile(c))
            if c == rc:
                success += 1
            else:
                failed += 1
        except RuntimeError as exc:
            unsupported += 1
        except IOError:
            errors += 1

        print '\r%d successful roundtrip, %d failed roundtrip, %d unsupported, %d nosource ' % (success, failed, unsupported, errors),

    if errors > 0:
        raise Exception

if __name__ == '__main__':
    test_roundtrip()
