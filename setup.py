# from setuptools import setup, find_packages

# setup(
#     name='taming-transformers',
#     version='0.0.1',
#     description='Taming Transformers for High-Resolution Image Synthesis',
#     long_description=open('README.md').read(),
#     long_description_content_type='text/markdown',
#     url='https://github.com/ulisrael/taming-transformers',  # Replace with the correct URL
#     author='Your Name',
#     author_email='your.email@example.com',
#     packages=find_packages(),
#     install_requires=[
#         'torch==1.7.0',
#         'torchvision==0.8.1',
#         'transformers==4.3.1',
#         'sacrebleu==1.5.1',
#         'packaging==20.9',
#         'filelock==3.0.12',
#         'numpy==1.19.5',
#         'tokenizers==0.10.1',
#         'sacremoses==0.0.43',
#         'tqdm==4.49.0',
#         'regex==2020.11.13',
#         'requests==2.24.0'
#     ],
#     classifiers=[
#         'Programming Language :: Python :: 3',
#         'License :: OSI Approved :: MIT License',
#         'Operating System :: OS Independent',
#     ],
#     python_requires='>=3.6',
# )


from setuptools import setup, find_packages

setup(
    name='taming-transformers',
    version='0.0.1',
    description='Taming Transformers for High-Resolution Image Synthesis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ulisrael/taming-transformers',  # Replace with the correct URL
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'torch',
        'pytorch-lightning',
        'einops',
        'Pillow',
        'omegaconf',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
