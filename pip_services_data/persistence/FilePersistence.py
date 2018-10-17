# -*- coding: utf-8 -*-
"""
    pip_services_data.persistence.FilePersistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    File persistence implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_commons.config import IConfigurable
from .MemoryPersistence import MemoryPersistence
from .JsonFilePersister import JsonFilePersister

class FilePersistence(MemoryPersistence, IConfigurable):
    _persister = None

    def __init__(self, persister):
        super(FilePersistence, self).__init__(persister if persister != None else JsonFilePersister(),
                                              persister if persister != None else JsonFilePersister())

        self._persister = persister
        # self._saver = self._persister
        # self._loader = self._persister

    def configure(self, config):
        self._persister.configure(config)
