VERSION = (1, 2, 0, "alpha")
__version__ = VERSION


def get_version():
    version = "%s.%s" % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = "%s.%s" % (version, VERSION[2])
    if VERSION[3:] == ("alpha", 0):
        version = "%s pre-alpha" % version
    else:
        if VERSION[3][0:4] == "post":
            version = "%s.%s" % (version, VERSION[3])
        elif VERSION[3] != "final":
            try:
                rev = VERSION[4]
            except IndexError:
                rev = 0
            version = "%s%s%s" % (version, VERSION[3][0:1], rev)
    return version
