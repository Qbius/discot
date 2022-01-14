import setuptools

setuptools.setup(
    name='discot',  
    version='1.0.1',
    scripts=[] ,
    author='Michał Surówka',
    author_email='michalpiotrsurowka@gmail.com',
    description='Discord bot creation framework',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/qbius/discot',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)