from setuptools import setup, find_packages

setup(
    name='my_doc_server',  # Choose a unique name here
    version='0.1.0',
    description='A self-hosted documentation server for serving markdown files.',
    author='Sudarshan Sinha',
    author_email='s.sinha2103@outlook.com',
    url='https://github.com/yourusername/mydocserver',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,  # Includes templates, static files
    install_requires=[
        'Flask',
        'Markdown',
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'docserver=my_doc_server.cli:cli',  # Adjust to match the new package name
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
