import sys
import os
import time
from os import path

try:
    import esptool
    import espefuse
except ImportError:
    need_to_install_package_err()

esptool.main(sys.argv[1].split(' '))