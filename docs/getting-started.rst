Getting started
===============

The repository groups Python environments by module. Run each command from
the checkout root unless the example changes directories.

Run the statistics notebooks
----------------------------

Install `uv <https://docs.astral.sh/uv/>`_ and prepare the locked third-party
dependencies for Modules 2 and 4. Module 4 supplies the Jupyter server.

.. code-block:: bash

   uv python install 3.14
   uv sync --project "Module 2" --python 3.14 --frozen --no-install-local
   uv sync --project "Module 4" --python 3.14 --frozen --no-install-local
   "Module 2/.venv/bin/python" -m ipykernel install \
     --prefix "$PWD/Module 4/.venv" --name cas-ads-module-2 \
     --display-name "CAS ADS - Module 2"
   "Module 4/.venv/bin/python" -m notebook --no-browser

Open the URL printed by Jupyter, browse to ``Module 2/CAS-D2-Regression.ipynb``,
and select the **CAS ADS - Module 2** kernel. Keep notebooks alongside their
data files so relative imports and data paths resolve.

The frozen mode uses the checked-in lockfiles. Skipping local package
installation avoids packaging the course directories and still installs their
third-party dependencies.

.. note::

   Two Module 2 notebooks have known compatibility issues with the locked
   dependencies. ``CAS-D1-DescriptiveStatistics.ipynb`` attempts a pandas mean
   over a text column. ``CAS-D1-Probability.ipynb`` uses ``steps-mid`` as a
   Matplotlib line style.

Run a database example
----------------------

The SQLite example uses Python's standard library. Run it from the directory
that contains the included ``university.db`` file.

.. code-block:: bash

   cd "Module 1/M1-D2-DB"
   python access-sql.py

Run the Module 4 tests
----------------------

After installing the Module 4 dependencies as shown above, run the example
test suite from the repository root.

.. code-block:: bash

   "Module 4/.venv/bin/python" -m pytest -q "Module 4/CAS_ADS_4-main/pytest_examle"

Choose a Python version for Module 3
------------------------------------

Module 3 supports Python 3.10 through 3.13. Select a version explicitly when
syncing it with uv, since the repository root pins Python 3.14. This module's
TensorFlow and PyTorch dependencies can require substantial disk space.
