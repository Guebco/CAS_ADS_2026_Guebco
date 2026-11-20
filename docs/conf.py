"""Sphinx configuration for the CAS Applied Data Science repository."""

import sys
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY / "Module 4" / "CAS_ADS_4-main" / "documentation"))

project = "CAS Applied Data Science 2026"
author = "Cornel Guebeli"
language = "en"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.githubpages",
]
templates_path = ["_templates"]
exclude_patterns = ["_build"]

html_theme = "alabaster"
html_title = project
html_copy_source = False
html_context = {
    "repository_url": "https://github.com/Guebco/CAS_ADS_2026_Guebco",
}
