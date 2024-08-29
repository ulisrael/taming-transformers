# from setuptools import setup, find_packages

# setup(
#     name='taming-transformers',
#     version='0.0.1',
#     description='Taming Transformers for High-Resolution Image Synthesis',
#     packages=find_packages(include=["taming", "taming.*"]),
#     install_requires=[
#         'torch',
#         'numpy',
#         'tqdm',
#     ],
# )

from setuptools import setup, find_packages

setup(
    name='taming-transformers',
    version='0.0.1',
    description='Taming Transformers for High-Resolution Image Synthesis',
    long_description=open('README.md').read(),  # Assuming you have a README.md file
    long_description_content_type='text/markdown',  # Specifies the content type of the long description
    url='https://github.com/yourusername/taming-transformers',  # Replace with your repository URL
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(include=["taming", "taming.*"]),
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Change to your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python version requirement
)
