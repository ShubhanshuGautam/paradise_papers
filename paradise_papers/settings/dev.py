from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#Connect to Neo4j Database
config.DATABASE_URL = 'bolt://neo4j:shubh@localhost:7687'
