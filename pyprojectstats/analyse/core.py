import abc
import functools


# Lazy property taken from here:
# https://stackoverflow.com/a/3013910/498873
# In Python 3.8 a functools.cached_property is added
# So we change to that name
def cached_property(fn):
    attr_name = "_cache_" + fn.__name__

    @property
    @functools.wraps(fn)
    def _cached_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return _cached_property


class BaseFile(abc.ABC):
    pass

    @cached_property
    def text(self):
        """Text file content"""
        return self.path.read_text()

    @cached_property
    def lines(self):
        return self.text.splitlines()

    @cached_property
    def n_lines_total(self):
        return len(self.lines)

    def to_dict(self):
        return {"path": self.path, "n_lines_total": self.n_lines_total}
