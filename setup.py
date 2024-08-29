from setuptools import setup, find_packages

setup(
    name='taming-transformers',
    version='0.0.1',
    description='Taming Transformers for High-Resolution Image Synthesis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ulisrael/taming-transformers',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),  # Automatically find all packages and sub-packages
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
