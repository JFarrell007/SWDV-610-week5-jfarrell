"""
Name: Jim Farrell
Description: class to handle exceptions when trying to add too many items
"""

class Error(Exception):
    """Base class for exceptions in this module"""
    pass

class FullError(Error):
    """Raised when trying to get hash for one too many items"""
    
    def __init__(self, message):
        self.message = message