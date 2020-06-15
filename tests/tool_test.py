# -*- coding: UTF-8 -*-

# Import from standard library
import os
# Import from our lib
from mlproject.tools import haversine
import pytest


def test_haversine():
  assert haversine(48.865070, 2.3800099, 48.235070, 2.393409) == 70.00788937941758
