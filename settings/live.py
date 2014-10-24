from __future__ import absolute_import
from .base import *
from .local import *

CACHE_BACKEND = 'redis_cache.cache://redis:6379/?timeout=15'
DEBUG = False
