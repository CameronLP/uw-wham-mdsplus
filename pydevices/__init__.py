==========
@authors: Gabriele Manduchi (IGI Padova)
@copyright: 2008
@license: GNU GPL
=======
"""
import os
import MDSplus


def _mimport(name, level=1):
    try:
        module = __import__(name, globals())
    except:
        module = __import__(name, globals(), level=level)
    for k, v in module.__dict__.items():
        if isinstance(v, type(MDSplus.Device)):
            if issubclass(v, MDSplus.Device):
                globals()[k] = v


try:
    _mvers = _mimport('_version')
    __version__ = _mvers.version
    __doc__ = __doc__+"Version: %s\nBranch: %s\nCommit: %s\nRelease tag: %s\n" % (_mvers.version,
                                                                                  _mvers.branch,
                                                                                  _mvers.commit,
                                                                                  _mvers.release_tag)
    __doc__ = __doc__+"Release: %s\n" % _mvers.release_date
    branch = _mvers.branch
    commit = _mvers.commit
    release_tag = _mvers.release_tag
    del _mvers
except:
    __version__ = 'Unknown'

for filename in os.listdir(os.path.dirname(__file__)):
    if not filename.startswith("_"):
        if filename.endswith('.py'):
            _mimport(filename[:-3])
