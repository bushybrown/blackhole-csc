# setup.py for BlackHole Cipher Suite

from setuptools import setup, find_packages

setup(
    name='blackhole-cipher',
    version='6.0',
    author='Chris Nelson',
    description='Symbolic, entropy-reactive encryption system with drift-based encoding and fusion logic.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pycryptodome>=3.18.0',
        'ttkbootstrap>=1.10.1',
        'tkintertable>=1.3.3',
        'matplotlib>=3.8.0',
        'numpy>=1.26.0',
        'scipy>=1.11.3',
        'rich>=13.5.2',
        'colorama>=0.4.6'
    ],
    python_requires='>=3.10',
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Topic :: Security :: Cryptography',
        'Intended Audience :: Developers'
    ]
)
