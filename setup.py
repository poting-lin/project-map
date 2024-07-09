from setuptools import setup, find_packages

setup(
    name='project-map',
    version='0.1.0',
    author='Po-Ting Lin',
    description='A tool to scan and visualize the directory structure of a project.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/poting-lin/project-map',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'project-map=project_map.scan:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
