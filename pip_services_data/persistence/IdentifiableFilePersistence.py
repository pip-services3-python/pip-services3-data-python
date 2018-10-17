# -*- coding: utf-8 -*-
"""
    pip_services_data.persistence.IdentifiableFilePersistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Identifiable file persistence implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .IdentifiableMemoryPersistence import IdentifiableMemoryPersistence
from .JsonFilePersister import JsonFilePersister

class IdentifiableFilePersistence(IdentifiableMemoryPersistence):
    _persister = None

    def __init__(self, persister):
        super(IdentifiableFilePersistence, self).__init__(persister if persister != None else JsonFilePersister(),
                                                          persister if persister != None else JsonFilePersister())


        self._persister = persister
        # self._saver = self._persister
        # self._loader = self._persister

    def configure(self, config):
        super().configure(config)
        self._persister.configure(config)
