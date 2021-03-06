from __future__ import absolute_import
import rollbar
import sys
import os
import logging


logger = logging.getLogger("django")


def event(event_name, extra_data_dict={}):
    """
    Log an event to the analytics backend
    """
    logger.info('%s: %s', event_name, extra_data_dict)


def exception(request=None, extra_data=None):
    """
    Log an exception to the logging backend
    """
    rollbar.report_exc_info(sys.exc_info(), request=request, extra_data=extra_data)
