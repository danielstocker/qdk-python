##
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
##
import logging
from .version import __version__

from .job import *
from .workspace import *

from ._client.models import JobStatus

logger = logging.getLogger(__name__)
logger.info(f"version: {__version__}")
