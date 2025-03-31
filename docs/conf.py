import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Dokumentacja przykładowa'
author = 'Jan Kowalski'
release = '0.1'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
