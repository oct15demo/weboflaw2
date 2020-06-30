'''
Created on May 8, 2020

@author: charles
'''
import logging, sys, os
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(message)s | \'%(name)s:%(lineno)s\'')
log = logging.getLogger(os.path.basename(__file__))

log.debug("hello logging linked to source")

x = 3
b= x+4
log.debug(b)