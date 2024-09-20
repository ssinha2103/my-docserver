from setuptools import setup, find_packages

setup(
    name='docserver',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'Markdown',
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'docserver=docserver.cli:cli',
        ],
    },
    author='Sudarshan Sinha',
    author_email='s.sinha2103@gmail.com',
    description='A self-hosted documentation server for Python projects',
    url='https://github.com/yourusername/docserver',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
