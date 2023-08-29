r"""
Provides frozendict, a simple immutable dictionary.
"""

try:
    from ._frozendict import *
    c_ext = True
    del _frozendict
except ImportError:
    from .core import *
    c_ext = False

from .version import version as __version__
from . import monkeypatch


def _getFrozendictJsonEncoder(BaseJsonEncoder = None):
    if BaseJsonEncoder == None:
        from json.encoder import JSONEncoder
        
        
        BaseJsonEncoder = JSONEncoder
    
    
    class FrozendictJsonEncoder(BaseJsonEncoder):
        def default(self, obj):
            if isinstance(obj, frozendict):
                # TODO create a C serializer
                return dict(obj)
            
            
            return BaseJsonEncoder.default(self, obj)
    
    
    return FrozendictJsonEncoder


FrozendictJsonEncoder = _getFrozendictJsonEncoder()
monkeypatch.patchOrUnpatchAll(patch = True, warn = False)


from collections.abc import Mapping
Mapping.register(frozendict)
del Mapping


if c_ext:
    __all__ = (frozendict.__name__, )
else:
    __all__ = core.__all__
    del core

# TODO deprecated, to remove in future versions
FrozenOrderedDict = frozendict

__all__ += (FrozendictJsonEncoder.__name__, "FrozenOrderedDict")
