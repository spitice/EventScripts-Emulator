
from pickle import *

#
# [css2025_win32]
#
# Added for compatibility. (cPickle is no longer available in Py3)
#
# `ese convert <your-addon-name>` should fix the import name for pickle
# but if your Py2 code doesn't contain any deprecated usage other than `import cPickle`,
# then no need to convert it.
#
# (Recommend you to convert them to Py3 code nonetheless)
#
