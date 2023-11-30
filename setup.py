from setuptools import find_packages, setup

setup(
    name='tools',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'exceptiongroup==1.2.0',
        'iniconfig==2.0.0',
        'mccabe==0.7.0',
        'numpy==1.26.2',
        'packaging==23.2',
        'pandas==2.1.3',
        'pluggy==1.3.0',
        'pycodestyle==2.11.1',
        'pyflakes==3.1.0',
        'pytest==7.4.3',
        'python-dateutil==2.8.2',
        'pytz==2023.3.post1',
        'six==1.16.0',
        'tomli==2.0.1',
        'tzdata==2023.3',
    ],
    test_suite='tests',
    tests_require=[
        'pytest',
    ],
)
