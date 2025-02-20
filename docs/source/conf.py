# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import django

# Adicione o caminho para o seu projeto Django
sys.path.insert(0, os.path.abspath('../../'))

# Configurar o Django para encontrar o arquivo settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'setup.settings'

# Inicializar o Django
django.setup()

project = 'Escola Alura'
copyright = '2024, Amauri'
author = 'Amauri'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Suporte para docstrings no estilo Google/NumPy
    'sphinx.ext.viewcode',  # Links para o código-fonte
]

templates_path = ['_templates']
exclude_patterns = []

language = 'pt-BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
