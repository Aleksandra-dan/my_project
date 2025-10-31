from setuptools import setup, find_packages

setup(
    name="notebook",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'notebook=notebook.commands:main',
        ],
    },
    python_requires='>=3.6',
)