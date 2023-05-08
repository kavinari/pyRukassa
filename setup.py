from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='pyRukassa',
      version='1.0',
      url='https://github.com/kavinari/pyRukassa',
      license='MIT',
      description='rukassa api python wrapper',
      packages=['pyRukassa'],
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='kavinari',
      install_requires=['requests'],
      author_email='kavinariy@gmail.com',
      zip_safe=False)
