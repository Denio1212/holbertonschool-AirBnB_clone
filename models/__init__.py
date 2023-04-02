#!/usr/bin/python3
"""
links file_storage to BaseModule
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
