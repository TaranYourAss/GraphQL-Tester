#!/usr/bin/env python

class AttribDict(dict):
    """
    A class that allows storing and accessing of attributes that get assigned to itself.
    """
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(f"'AttributeDict' object has no attribute '{item}'")
    
    def __setattr__(self, key, value):
        self[key] = value
    
    def __delattr__(self, item):
        try:
            del self[item]
        except KeyError:
            raise AttributeError(f"'AttributeDict' object has no attribute '{item}'")