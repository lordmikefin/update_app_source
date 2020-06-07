# -*- coding: UTF-8 -*-
"""
    update_app_source
    ~~~~~~~~~~~~~~~~~

    Module for automatically update content of 'app_source' project.

    License of this script file:
       MIT License

    License is available online:
      https://github.com/lordmikefin/update_app_source/blob/master/LICENSE

    Latest version of this script file:
      https://github.com/lordmikefin/update_app_source/blob/master/update_app_source/__init__.py


    :copyright: (c) 2020, Mikko Niemelä a.k.a. Lord Mike (lordmike@iki.fi)
    :license: MIT License
"""
import logging

__license__ = "MIT License"
__version__ = "0.0.3"
__revision__ = "update_app_source (module)  v" + __version__ + " (2020-06-07)"

#source_file = './app_source/app_source.xml'

#from . import source
from app_source_handler import source

def create_logger():
    # https://www.toptal.com/python/in-depth-python-logging
    log = logging.getLogger('update_app_source')
    # Do not propagate the log up to parent
    log.propagate = False
    return log

logger = create_logger()
