#!/usr/bin/env python3
"""__init__ method that initializes packages"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
