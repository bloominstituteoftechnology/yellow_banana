from setuptools import setup, find_packages

setup(
    name='yellow_banana',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'yellow_banana=yellow_banana.main:main',
        ],
    },
    install_requires=[],
    author='Gabriel Cabrejas',
    author_email='gabriel@cabrejas.net',
    description='A simple CLI tool.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bloominstituteoftechnology/yellow_banana',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
