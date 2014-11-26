import warnings

warnings.warn("include('registration.urls') is deprecated; use include('registration.backends.default.urls') instead.", DeprecationWarning)

from registration.backends.simple.urls import *
