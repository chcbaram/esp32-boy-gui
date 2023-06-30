from setuptools import setup, find_packages

setup_requires = [
    ]

install_requires = [
    'PySide6==6.5.0',
    'pyserial',
    'esptool'
    ]

setup(
    name="esp32-boy-gui",
    version="0.0.1",
    packages=find_packages(),
    author="baram",
    author_email="chcbaram@gmail.com",
    description="esp32-boy-gui",
    keywords="",
    url="",
    install_requires=install_requires,

    setup_requires=setup_requires,
    package_data={'esp32-boy-gui': ['*.ttf', 'app/data/fonts/*.ttf']},
    include_package_data=True,

    entry_points={
      "console_scripts":[
        "esp32-boy-gui=app.launcher:main"
        ],
    },
    classifiers=[
        "Environment :: Qt",
        "Operating System :: POSIX",
    ]
)