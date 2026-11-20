Build and publish the documentation
===================================

Build and preview locally
-------------------------

Use Python 3.12, matching the documentation workflow, and run these commands
from the repository root.

.. code-block:: bash

   python3.12 -m venv .venv
   .venv/bin/python -m pip install -r docs/requirements.txt
   .venv/bin/python -m sphinx -W -b html docs docs/_build/html
   .venv/bin/python -m http.server 8000 --bind 127.0.0.1 --directory docs/_build/html

Open `the local preview <http://127.0.0.1:8000/>`_. The entry point is
``docs/_build/html/index.html``. Keep the full HTML directory together because
it contains navigation, stylesheets, and search files. Sphinx also creates
``.nojekyll`` for Pages compatibility.

Deploy through GitHub Actions
-----------------------------

In the repository's **Settings → Pages**, set **Source** to **GitHub Actions**.
The ``.github/workflows/docs.yml`` workflow checks the documentation build on
pull requests. A push to ``main`` builds and deploys the same HTML. You can
also run the workflow from the **Actions** tab using the ``main`` branch.

When deployment succeeds, the workflow's ``github-pages`` environment shows
the site URL. Keep the generated HTML under ``docs/_build/`` out of Git.
Update the ``.rst`` files for guides, the Python docstrings for API content,
and ``docs/_templates/layout.html`` for the shared HTML layout.
