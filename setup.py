from setuptools import setup, find_packages
from bahasa import __version__

setup(
    name='bahasa',
    packages=find_packages(),
    package_data={'bahasa': ['data/kamus.txt']},
    version=__version__,
    description='Bahasa is natural language toolkit for bahasa indonesia',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    author='Sutrisno Efendi',
    author_email='kangfend@gmail.com',
    url='https://github.com/kangfend/bahasa',
    keywords=['NLP', 'Bahasa', 'Indonesia', 'Stemmer', 'Sastrawi', 'Stemming'],
    install_requires=['six==1.16.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Natural Language :: Indonesian',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
