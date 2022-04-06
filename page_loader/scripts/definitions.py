#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
# Calculate the correct path to the root directory of our project
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), ''))


# CLI config
DEFAULT_DIR = 'tmp'

# allowed tags for downloading resources
ALLOWED_TAGS = ['img', 'script', 'link']
