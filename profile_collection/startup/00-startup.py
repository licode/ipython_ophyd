import sys
import logging

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import faulthandler
from metadatastore.mds import MDS
from databroker import Broker
from databroker.core import register_builtin_handlers
from filestore.fs import FileStore
from hxntools.handlers.xspress3 import Xspress3HDF5Handler
from hxntools.handlers.timepix import TimepixHDF5Handler

faulthandler.enable()
plt.ion()

handler = logging.StreamHandler(sys.stderr)
fmt = logging.Formatter("%(asctime)-15s [%(name)5s:%(levelname)s] %(message)s")
handler.setFormatter(fmt)
handler.setLevel(logging.INFO)

logging.getLogger('hxntools').addHandler(handler)
logging.getLogger('hxnfly').addHandler(handler)
logging.getLogger('ppmac').addHandler(handler)

logging.getLogger('hxnfly').setLevel(logging.DEBUG)
logging.getLogger('hxntools').setLevel(logging.DEBUG)
logging.getLogger('ppmac').setLevel(logging.INFO)


# Flyscan results are shown using pandas. Maximum rows/columns to use when
# printing the table:
pd.options.display.width = 180
pd.options.display.max_rows = None
pd.options.display.max_columns = 10

_mds_config = {'host': 'xf03id-ca1',
               'port': 27017,
               'database': 'datastore-new',
               'timezone': 'US/Eastern'}
mds = MDS(_mds_config, auth=False)

_fs_config = {'host': 'xf03id-ca1',
              'port': 27017,
              'database': 'filestore-new'}
db_new = Broker(mds, FileStore(_fs_config))

_mds_config_old = {'host': 'xf03id-ca1',
                   'port': 27017,
                   'database': 'datastore',
                   'timezone': 'US/Eastern'}
mds_old = MDS(_mds_config_old, auth=False)

_fs_config_old = {'host': 'xf03id-ca1',
                  'port': 27017,
                  'database': 'filestore'}
db_old = Broker(mds_old, FileStore(_fs_config_old))


def _hxn_register_handlers(inp_db):
    "helper function to register handlers to both assert registries"
    register_builtin_handlers(inp_db.fs)
    inp_db.fs.register_handler(Xspress3HDF5Handler.HANDLER_NAME,
                               Xspress3HDF5Handler)
    inp_db.fs.register_handler(TimepixHDF5Handler._handler_name,
                               TimepixHDF5Handler, overwrite=True)


_hxn_register_handlers(db_new)
_hxn_register_handlers(db_old)
del _hxn_register_handlers


# wrapper for two databases
class Broker_New(Broker):

    def __getitem__(self, key):
        try:
            return db_new[key]
        except ValueError:
            return db_old[key]

    def get_table(self, *args, **kwargs):
        result_old = db_old.get_table(*args, **kwargs)
        result_new = db_new.get_table(*args, **kwargs)
        result = [result_old, result_new]
        return pd.concat(result)

    def get_images(self, *args, **kwargs):
        try:
            result = db_new.get_images(*args, **kwargs)
        except IndexError:
            result = db_old.get_images(*args, **kwargs)
        return result


db = Broker_New(mds, FileStore(_fs_config))


def remove_names_maybe(obj, names):
    for n in names:
        try:
            obj.read_attrs.remove(n)
        except ValueError:
            pass
    return obj
