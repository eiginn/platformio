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

PlatformIO is an open source ecosystem for IoT development
==========================================================

**Cross-platform code builder and library manager. Continuous and IDE
integration. Arduino and MBED compatible. Ready for Cloud compiling.**

* **Development Platforms** - Embedded and Desktop development platforms with
  pre-built toolchains, debuggers, uploaders and frameworks which work under
  popular host OS: Mac, Windows, Linux (+ARM)
* **Embedded Boards** - Rapid Embedded Programming, IDE and Continuous
  Integration in a few steps with PlatformIO thanks to built-in project
  generator for the most popular embedded boards and IDE
* **Library Manager** - Hundreds Popular Libraries are organized into single
  Web 2.0 platform: list by categories, keywords, authors, compatible
  platforms and frameworks; learn via examples; be up-to-date with the latest
  version

*Atmel AVR & SAM, Espressif, Freescale Kinetis, Nordic nRF51, NXP LPC,
Silicon Labs EFM32, ST STM32, TI MSP430 & Tiva, Teensy, Arduino, mbed,
libOpenCM3, etc.*

* `Website <http://platformio.org>`_
* `Web 2.0 Library Search <http://platformio.org/#!/lib>`_ |
  `Embedded Boards Explorer <http://platformio.org/#!/boards>`_
* `Project Examples <https://github.com/platformio/platformio/tree/develop/examples>`_
* `Source Code <https://github.com/platformio/platformio>`_ |
  `Issues <https://github.com/platformio/platformio/issues>`_
* `Blog <http://www.ikravets.com/category/computer-life/platformio>`_ |
  `Twitter <https://twitter.com/PlatformIO_Org>`_ |
  `Hackaday <https://hackaday.io/project/7980-platformio>`_ |
  `Facebook <https://www.facebook.com/platformio>`_ |
  `Reddit <http://www.reddit.com/r/platformio/>`_

Embedded Development. *Easier Than Ever.*
-----------------------------------------

* Colourful command-line output
* :ref:`IDE Integration <ide>` with *Arduino, Atom, CLion, Eclipse, Emacs,
  Energia, Qt Creator, Sublime Text, Vim, Visual Studio*
* Cloud compiling and  :ref:`ci` with *AppVeyor, Circle CI, Drone, Shippable, Travis CI*
* Built-in :ref:`Serial Port Monitor <cmd_serialports_monitor>` and
  configurable build :ref:`-flags/-options <projectconf_build_flags>`
* Pre-built toolchains, :ref:`frameworks` for the
  :ref:`Development Platforms <platforms>`

Smart Code Builder. *Fast and Reliable.*
----------------------------------------

* Reliable, automatic dependency analysis and detection of build changes
* Improved support for parallel builds
* Ability to share built files in a cache
* Lookup for external libraries which are installed via :ref:`librarymanager`

The Missing Library Manager. *It's here!*
-----------------------------------------

* Friendly Command-Line Interface
* Modern `Web 2.0 Library Search <http://platformio.org/#!/lib>`_
* Library dependency management
* Automatic library updating
* It runs on Windows, Mac OS X, and Linux (+ARM).

For further details, please refer to
:ref:`What is PlatformIO? How does it work? <what_is_pio>`

Contents
--------

.. toctree::
    :maxdepth: 2

    what-is-platformio
    demo

.. toctree::
    :caption: Getting Started
    :maxdepth: 2

    installation
    quickstart
    userguide/index

.. toctree::
    :caption: Configuration
    :maxdepth: 2

    projectconf
    envvars

.. toctree::
    :caption: Instruments
    :maxdepth: 3

    Platforms & Boards <platforms/index>
    frameworks/index

.. toctree::
    :caption: Library Manager
    :maxdepth: 2

    Quickstart <librarymanager/index>
    User Guide <userguide/lib/index.rst>
    librarymanager/config
    librarymanager/creating

.. toctree::
    :caption: Integration
    :maxdepth: 2

    ci/index
    ide

.. toctree::
    :caption: Miscellaneous
    :maxdepth: 2

    articles
    FAQ <faq>
    history
