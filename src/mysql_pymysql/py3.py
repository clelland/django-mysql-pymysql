import sys

if sys.version_info[0] < 3:
    text_type = unicode
    long_type = long
    iteritems = lambda o: o.iteritems()
    def exec_(code, globs=None, locs=None):
        """Execute code in a namespace."""
        if globs is None:
            frame = sys._getframe(1)
            globs = frame.f_globals
            if locs is None:
                locs = frame.f_locals
            del frame
        elif locs is None:
            locs = globs
        exec("""exec code in globs, locs""")
    exec_("""def reraise(tp, value, tb=None):
    raise tp, value, tb
""")
else:
    text_type = str
    long_type = int
    iteritems = lambda o: o.items()
    def reraise(tp, value, tb=None):
        if value.__traceback__ is not tb:
            raise value.with_traceback(tb)
        raise value

