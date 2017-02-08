from setuptools import setup, find_packages
from bahasa import __version__

setup(
    name='bahasa',
    packages=find_packages(),
    package_data={'bahasa': ['data/kamus.txt']},
    version=__version__,
    description='Bahasa is natural language toolkit for bahasa indonesia',
    license='MIT',
    author='Sutrisno Efendi',
    author_email='kangfend@gmail.com',
    url='https://github.com/kangfend/bahasa',
    keywords=['NLP', 'Bahasa', 'Indonesia', 'Stemmer'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Natural Language :: Indonesian',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
