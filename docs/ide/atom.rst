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

.. _ide_atom:

PlatformIO IDE for Atom
=======================

PlatformIO IDE is the next generation integrated development environment for IoT:

* Cross-platform code builder without external dependencies to the system
  software:

    - 200+ embedded boards
    - 15+ development platforms
    - 10+ frameworks

* C/C++ Intelligent Code Completion
* C/C++ Smart Code Linter for rapid professional development
* Library Manager for the hundreds popular libraries
* Multi-projects workflow with multiple panes
* Themes support with dark and light colors
* Serial Port Monitor
* Built-in Terminal with :ref:`PlatformIO CLI <userguide>` tool (``pio``, ``platformio``)


PlatformIO IDE is based on GitHub's `Atom <https://atom.io>`_ source
code editor that's modern, approachable, yet hackable to the core; a tool you
can customize to do anything but also use productively without ever touching a
config file.


.. contents::

Installation
------------

PlatformIO IDE is the next generation integrated development environment for IoT.
It's built on top of `GitHub's Atom "hackable" text editor <https://atom.io>`_.
If you have already Atom installed, please install `PlatformIO IDE for Atom package <https://atom.io/packages/platformio-ide>`_.

Automatic Installation
~~~~~~~~~~~~~~~~~~~~~~

Please download PlatformIO IDE for Atom bundle with built-in auto installer
(be patient and let the installation complete)

- `Download PlatformIO IDE for Windows <https://dl.bintray.com/platformio/ide-bundles/platformio-atom-windows.exe>`_
- `Download PlatformIO IDE for Mac <https://dl.bintray.com/platformio/ide-bundles/platformio-atom-mac.zip>`_
- `Download PlatformIO IDE .deb <https://dl.bintray.com/platformio/ide-bundles/platformio-atom-linux-x86_64.deb>`_
- `Download PlatformIO IDE .rpm <https://dl.bintray.com/platformio/ide-bundles/platformio-atom-linux-x86_64.rpm>`_

Manual Installation
~~~~~~~~~~~~~~~~~~~

1. Download and install the latest Atom text editor

    - `Download Atom for Mac <https://atom.io/download/mac>`_
    - `Download Atom for Windows <https://atom.io/download/windows>`_
    - `Download Atom .deb <https://atom.io/download/deb>`_
    - `Download Atom .rpm <https://atom.io/download/rpm>`_
    - `Other platforms <https://github.com/atom/atom/releases/latest>`_


2. Open Atom Package Manager and install `platformio-ide <https://atom.io/packages/platformio-ide>`_ Atom package

    - **Mac OS X**: ``Menu: Atom > Preferences > Install``
    - **Windows**: ``Menu: File > Settings > Install``
    - **Linux**: ``Menu: Edit > Preferences > Install``

.. image:: ../_static/ide-atom-platformio-install.png


.. _atom_ide_quickstart:

Quick Start
-----------

This tutorial introduces you to the basics of PlatformIO IDE workflow and shows you a creation process of a simple "Blink" example. After finishing you will have a general understanding of how to work with projects in the IDE.

Launching
~~~~~~~~~

PlatformIO IDE is built on top of GitHub's Atom "hackable" text editor.
After installation please run one of ``Atom.exe``,  ``Atom.app`` or ``atom``
application depending on the OS.

Setting Up the Project
~~~~~~~~~~~~~~~~~~~~~~

1. To create a new project choose ``Menu: PlatformIO > Initialize new Project or update existing`` or press the corresponding icon in the PlatformIO toolbar as shown in the image below:

.. image:: ../_static/ide-atom-platformio-quick-start-1.png
    :target: http://docs.platformio.org/en/latest/_images/ide-atom-platformio-quick-start-1.png

2. In the "New Project Menu" choose desired boards (more than one board is allowed) and select a project directory. Then press "Initialize" button:

.. image:: ../_static/ide-atom-platformio-quick-start-2.png
    :target: http://docs.platformio.org/en/latest/_images/ide-atom-platformio-quick-start-2.png

3. If everything is fine, you should see the success message and project tree in the left panel:

.. image:: ../_static/ide-atom-platformio-quick-start-3.png
    :target: http://docs.platformio.org/en/latest/_images/ide-atom-platformio-quick-start-3.png

4. Now, let's create the first project source file: right-click on the folder ``src`` and choose ``New File``:

.. image:: ../_static/ide-atom-platformio-quick-start-4.png
    :target: http://docs.platformio.org/en/latest/_images/ide-atom-platformio-quick-start-4.png

Enter filename ``main.cpp``:

.. image:: ../_static/ide-atom-platformio-quick-start-5.png
    :target: http://docs.platformio.org/en/latest/_images/ide-atom-platformio-quick-start-5.png

Copy the next source code to the just created file ``main.cpp``:

.. code-block:: cpp

    /**
     * Blink
     * Turns on an LED on for one second,
     * then off for one second, repeatedly.
     */
    #include "Arduino.h"

    void setup()
    {
      // initialize LED digital pin as an output.
      pinMode(LED_BUILTIN, OUTPUT);
    }

    void loop()
    {
      // turn the LED on (HIGH is the voltage level)
      digitalWrite(LED_BUILTIN, HIGH);
      // wait for a second
      delay(1000);
      // turn the LED off by making the voltage LOW
      digitalWrite(LED_BUILTIN, LOW);
       // wait for a second
      delay(1000);
    }

Process Project
~~~~~~~~~~~~~~~

PlatformIO IDE proposes different ways to process project (build, clean, upload firmware, run other targets) using:

    - :ref:`atom_ide_platformio_toolbar`
    - :ref:`atom_ide_platformio_menu`
    - :ref:`ide_atom_building_targets` and hotkeys

.. image:: ../_static/ide-atom-platformio-quick-start-6.png
    :target: http://docs.platformio.org/en/latest/_images/ide-atom-platformio-quick-start-6.png

5. Run ``Build`` and you should see green "success" result in the building
   panel:

.. image:: ../_static/ide-atom-platformio-quick-start-7.png
    :target: http://docs.platformio.org/en/latest/_images/ide-atom-platformio-quick-start-7.png

To upload firmware to the board run ``Upload``.

6. What is more, you can run specific target or process project environment
   using ``Menu: PlatformIO > Run other target...``
   or call targets list from the status bar (bottom, left corner):

.. image:: ../_static/ide-atom-platformio-quick-start-8.png
    :target: http://docs.platformio.org/en/latest/_images/ide-atom-platformio-quick-start-8.png

And select desired target:

.. image:: ../_static/ide-atom-platformio-quick-start-9.png
    :target: http://docs.platformio.org/en/latest/_images/ide-atom-platformio-quick-start-9.png

7. To run built-in terminal interface choose ``Menu: PlatformIO > Terminal`` or press the corresponding icon in the PlatformIO toolbar:

.. image:: ../_static/ide-atom-platformio-quick-start-10.png
    :target: http://docs.platformio.org/en/latest/_images/ide-atom-platformio-quick-start-10.png

It provides you fast access to all set of powerful PlatformIO CLI commands:

.. image:: ../_static/ide-atom-platformio-quick-start-11.png
    :target: http://docs.platformio.org/en/latest/_images/ide-atom-platformio-quick-start-11.png

8. To run built-in "Serial Monitor" choose ``Menu: PlatformIO > Serial Monitor`` or press the corresponding icon in the PlatformIO toolbar:

.. image:: ../_static/ide-atom-platformio-quick-start-12.png
    :target: http://docs.platformio.org/en/latest/_images/ide-atom-platformio-quick-start-12.png

It has several settings to adjust your connection:

.. image:: ../_static/ide-atom-platformio-quick-start-13.png
    :target: http://docs.platformio.org/en/latest/_images/ide-atom-platformio-quick-start-13.png

And allows you to communicate with your board in an easy way:

.. image:: ../_static/ide-atom-platformio-quick-start-14.png
    :target: http://docs.platformio.org/en/latest/_images/ide-atom-platformio-quick-start-14.png


User Guide
----------

.. _atom_ide_platformio_menu:

Menu item ``PlatformIO``
~~~~~~~~~~~~~~~~~~~~~~~~

`platformio-ide <https://atom.io/packages/platformio-ide>`_ package adds to Atom
new menu item named ``Menu: PlatformIO`` (after ``Menu: Help`` item).

.. image:: ../_static/ide-atom-platformio-menu-item.png

.. _atom_ide_platformio_toolbar:

PlatformIO Toolbar
~~~~~~~~~~~~~~~~~~

PlatformIO IDE Toolbar contains the quick access button to the popular commands.
Each button contains hint (delay mouse on it).

.. image:: ../_static/ide-atom-platformio-toolbar.png

* PlatformIO: Build
* PlatformIO: Upload
* PlatformIO: Clean
* ||
* Initialize new PlatformIO Project or update existing...
* Add/Open Project Folder...
* Find in Project...
* ||
* Terminal
* Library Manager
* Serial Ports
* Serial Monitor
* ||
* Settings
* PlatformIO Documentation

.. _ide_atom_building_targets:

Building / Uploading / Targets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``cmd-alt-b`` / ``ctrl-alt-b`` / ``f9`` builds project without auto-uploading.
* ``cmd-alt-u`` / ``ctrl-alt-u`` builds and uploads (if no errors).
* ``cmd-alt-c`` / ``ctrl-alt-c`` cleans compiled objects.
* ``cmd-alt-t`` / ``ctrl-alt-t`` / ``f7`` run other targets (Upload using Programmer, Upload SPIFFS image, Update platforms and libraries).
* ``cmd-alt-g`` / ``ctrl-alt-g`` / ``f4`` cycles through causes of build error.
* ``cmd-alt-h`` / ``ctrl-alt-h`` / ``shift-f4`` goes to the first build error.
* ``cmd-alt-v`` / ``ctrl-alt-v`` / ``f8`` toggles the build panel.
* ``escape`` terminates build / closes the build window.

More details `Atom Build package <https://atom.io/packages/build>`_.

Intelligent Code Autocompletion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PlatformIO IDE uses `clang <http://clang.llvm.org>`_ for the Intelligent Code Autocompletion.
To check that ``clang`` is available in your system, please open
Terminal and run ``clang --version``. If ``clang`` is not installed, then install it:

- **Mac OS X**: Install the latest Xcode along with the latest Command Line Tools
  (they are installed automatically when you run ``clang`` in Terminal for the
  first time, or manually by running ``xcode-select --install``
- **Windows**: Download the latest `Clang for Windows <http://llvm.org/releases/download.html>`_.
  Please select "Add LLVM to the system PATH" option on the installation step.
- **Linux**: Using package managers: ``apt-get install clang`` or ``yum install clang``.
- **Other Systems**: Download the latest `Clang for the other systems <http://llvm.org/releases/download.html>`_.

.. warning::
    The libraries which are added/installed after initializing process will
    not be reflected in code linter. You need ``Menu: PlatformIO >
    Rebuild C/C++ Project Index (Autocomplete, Linter)``.

.. _ide_atom_smart_code_linter:

Smart Code Linter
~~~~~~~~~~~~~~~~~

PlatformIO IDE uses PlatformIO's pre-built GCC toolchains for Smart Code Linter
and rapid professional development.
The configuration data are located in ``.gcc-flags.json``. This file will be
automatically created and preconfigured when you initialize project using
``Menu: PlatformIO > Initialize new PlatformIO Project or update existing...``.

.. warning::
    The libraries which are added/installed after initializing process will
    not be reflected in code linter. You need ``Menu: PlatformIO >
    Rebuild C/C++ Project Index (Autocomplete, Linter)``.


.. error::
    If you have error like ``linter-gcc: Executable not found`` and
    ``"***/.platformio/packages/toolchain-atmelavr/bin/avr-g++" not found``
    please ``Menu: PlatformIO > Initialize new PlatformIO Project or update existing...``.

Install Shell Commands
~~~~~~~~~~~~~~~~~~~~~~

To install ``platformio`` and ``pio`` shell commands please use ``Menu:
PlatformIO > Install Shell Commands``. It will allow you to call PlatformIO from
other process, terminal and etc.

Known issues
------------

Smart Code Linter is disabled for Arduino files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`ide_atom_smart_code_linter` is disabled by default for Arduino files
(``*.ino`` and ``.pde``) because they  are not valid C/C++ based
source files:

1. Missing includes such as ``#include <Arduino.h>``
2. Function declarations are omitted.

There are two solutions:

.. contents::
    :local:

.. _ide_atom_knownissues_sclarduino_manually:

Convert Arduino file to C++ manually
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For example, we have the next ``Demo.ino`` file:

.. code-block:: cpp

    void function setup () {
        someFunction(13);
    }

    void function loop() {
        delay(1000);
    }

    void someFunction(int num) {
    }

Let's convert it to  ``Demo.cpp``:

1. Add ``#include <Arduino.h>`` at the top of the source file
2. Declare each custom function (excluding built-in, such as ``setup`` and ``loop``)
   before it will be called.

The final ``Demo.cpp``:

.. code-block:: cpp

    #include <Arduino.h>

    void someFunction(int num);

    void function setup () {
        someFunction(13);
    }

    void function loop() {
        delay(1000);
    }

    void someFunction(int num) {
    }

Force Arduino file as C++
^^^^^^^^^^^^^^^^^^^^^^^^^

To force Smart Code Linter to use Arduino files as C++ please

1. Open ``.gcc-flags.json`` file from the Initialized/Imported project and add
   ``-x c++`` flag at the beginning of the value of ``gccDefaultCppFlags`` field:

.. code-block:: json

    {
      "execPath": "...",
      "gccDefaultCFlags": "...",
      "gccDefaultCppFlags": "-x c++ -fsyntax-only ...",
      "gccErrorLimit": 15,
      "gccIncludePaths": "...",
      "gccSuppressWarnings": false
    }

2. Perform all steps from :ref:`ide_atom_knownissues_sclarduino_manually`
   (without renaming to ``.cpp``).

Articles / Manuals
------------------

* Feb 28, 2016 - **Alex Bloggt** - `PlatformIO vorgestellt (Introduction to PlatformIO IDE, German) <https://alexbloggt.com/platformio-vorgestellt/>`_
* Feb 25, 2016 - **NutDIY** - `PlatformIO Blink On Nodemcu Dev Kit V1.0 (Thai) <http://nutdiy.blogspot.com/2016/02/platformio-blink-on-nodemcu-dev-kit-v10.html>`_

See a full list with :ref:`articles`.

Screenshot
----------

.. image:: ../_static/ide-atom-platformio.png
    :target: http://docs.platformio.org/en/latest/_images/ide-atom-platformio.png
