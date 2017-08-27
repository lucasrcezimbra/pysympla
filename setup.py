# coding: utf-8
from setuptools import setup
import os


README = os.path.join(os.path.dirname(__file__), 'README.md')
REQUIREMENTS = os.path.join(os.path.dirname(__file__), 'requirements.txt')


if __name__ == "__main__":
    setup(name='pysympla',
          description='Scraper para acessar informações dos seus eventos no Sympla.',
          version='0.0.1',
          long_description=open(README).read(),
          author="Lucas Rangel Cezimbra",
          author_email="lucas.cezimbra@gmail.com",
          license="MIT License",
          url='https://github.com/Lrcezimbra/pysympla',
          keywords=['sympla', 'scraper', 'requests', 'events'],
          install_requires=open(REQUIREMENTS).readlines(),
          packages=['pysympla'],
    )
