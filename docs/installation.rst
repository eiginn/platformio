..  Copyright 2014-2016 Ivan Kravets <me@ikravets.com>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _installation:

Installation
============

.. include:: /ide/_platformio_ide_extra.rst

**PlatformIO** is written in `Python <https://www.python.org/downloads/>`_ and
works on Mac OS X, Linux, Windows OS and *ARM*-based credit-card sized
computers (`Raspberry Pi <http://www.raspberrypi.org>`_,
`BeagleBone <http://beagleboard.org>`_,
`CubieBoard <http://cubieboard.org>`_).

.. contents::

System requirements
-------------------

:Operating System: Mac OS X, Linux (+ARM) or Windows
:Python Interpreter:

    Python 2.6 or 2.7. Python 2.7 is recommended

    .. attention::
        **Windows Users**: Please `Download the latest Python 2.7.x
        <https://www.python.org/downloads/>`_ and install it.
        **DON'T FORGET** to select ``Add python.exe to Path`` feature on the
        "Customize" stage, otherwise ``pip`` command will not be available.

:Terminal Application:

    All commands below should be executed in
    `Command-line <http://en.wikipedia.org/wiki/Command-line_interface>`_
    application (Terminal). For Mac OS X and Linux OS - *Terminal* application,
    for Windows OS – ``cmd.exe`` application.

Installation Methods
--------------------

Please *choose ONE of* the following methods:

.. contents::
    :local:

Python Package Manager
~~~~~~~~~~~~~~~~~~~~~~

The latest stable version of PlatformIO may be installed or upgraded via
Python Package Manager (`pip <https://pip.pypa.io>`_) as follows:

.. code-block:: bash

    pip install -U platformio

If ``pip`` command is not available run ``easy_install pip`` or use
:ref:`installation_installer_script` which will install ``pip`` and
``platformio`` automatically.

Note that you may run into permissions issues running these commands. You have
a few options here:

* Run with ``sudo`` to install PlatformIO and dependencies globally
* Specify the `pip install --user <https://pip.pypa.io/en/stable/user_guide.html#user-installs>`_
  option to install local to your user
* Run the command in a `virtualenv <https://virtualenv.pypa.io>`_ local to a
  specific project working set.

.. _installation_installer_script:

Installer Script
~~~~~~~~~~~~~~~~

Super-Quick (Mac / Linux)
'''''''''''''''''''''''''

To install or upgrade *PlatformIO* paste that at a *Terminal* prompt
(**MAY require** administrator access ``sudo``):

.. code-block:: bash

    python -c "$(curl -fsSL https://raw.githubusercontent.com/platformio/platformio/master/scripts/get-platformio.py)"


Local Download (Mac / Linux / Windows)
''''''''''''''''''''''''''''''''''''''

To install or upgrade *PlatformIO*, download (save as...)
`get-platformio.py <https://raw.githubusercontent.com/platformio/platformio/master/scripts/get-platformio.py>`_
script. Then run the following (**MAY require** administrator access ``sudo``):

.. code-block:: bash

    # change directory to folder where is located downloaded "get-platformio.py"
    cd /path/to/dir/where/is/located/get-platformio.py/script

    # run it
    python get-platformio.py


On *Windows OS* it may look like:

.. code-block:: bash

    # change directory to folder where is located downloaded "get-platformio.py"
    cd C:\path\to\dir\where\is\located\get-platformio.py\script

    # run it
    C:\Python27\python.exe get-platformio.py

Full Guide
~~~~~~~~~~

1. Check a ``python`` version (only 2.6-2.7 is supported):

.. code-block:: bash

    python --version

*Windows Users* only:

    * `Download Python 2.7 <https://www.python.org/downloads/>`_ and install it.
    * Add to PATH system variable ``;C:\Python27;C:\Python27\Scripts;`` and reopen *Command Prompt* (``cmd.exe``) application. Please read this article `How to set the path and environment variables in Windows <http://www.computerhope.com/issues/ch000549.htm>`_.

2. Install a ``platformio`` and related packages:

.. code-block:: bash

    pip install -U platformio

If your computer does not recognize ``pip`` command, try to install it first
using `these instructions <https://pip.pypa.io/en/latest/installing.html>`_.

For upgrading ``platformio`` to the latest version:

.. code-block:: bash

    pip install -U platformio

Development Version
~~~~~~~~~~~~~~~~~~~

Install the latest PlatformIO from the ``develop`` branch:

.. code-block:: bash

    # uninstall existing version
    pip uninstall platformio

    # install the latest development version of PlatformIO
    pip install -U https://github.com/platformio/platformio/archive/develop.zip

If you want to be up-to-date with the latest ``develop`` version of PlatformIO,
then you need to re-install PlatformIO each time if you see the new commits in
`PlatformIO GitHub repository (branch: develop) <https://github.com/platformio/platformio/commits/develop>`_.

To revert to the latest stable version

.. code-block:: bash

    pip uninstall platformio
    pip install -U platformio


Troubleshooting
---------------

.. warning::
    If you are going to run *PlatformIO* from **subprocess**, you
    :ref:`MUST DISABLE <faq_troubleshooting_pioblocksprompt>` all prompts.
    It will allow you to avoid blocking.

.. note::
    **Linux OS**: Don't forget to install "udev" rules file
    `99-platformio-udev.rules <https://github.com/platformio/platformio/blob/develop/scripts/99-platformio-udev.rules>`_ (an instruction is located in the file).

    **Windows OS**: Please check that you have correctly installed USB driver
    from board manufacturer

For further details, frequently questions, known issues, please
refer to :ref:`faq`.
