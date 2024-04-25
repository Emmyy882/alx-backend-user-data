#!/usr/bin/env python3
"""Authenticates"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """returns bytes of a string argument"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
