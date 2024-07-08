from setuptools import setup, find_packages

setup(
    name='project-map',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'project-map=project-map.scan:main',
        ],
    },
)
