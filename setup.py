from setuptools import setup, find_packages

setup(
    name="data-visalization-package",
    version="0.1.0",
    author="Gustavo",
    author_email="gustavovicencotti@gmail.com",
    description="Data visualization package with graphics and interactivity support",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gvicencotti/image-processing-package",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'plotly'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.8',
)