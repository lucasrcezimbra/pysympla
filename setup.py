# coding: utf-8
from setuptools import setup
import os


README = os.path.join(os.path.dirname(__file__), 'README.rst')
REQUIREMENTS = os.path.join(os.path.dirname(__file__), 'requirements.txt')


if __name__ == "__main__":
    setup(name='pysympla',
        description='Scraper para acessar informações dos seus eventos no Sympla.',
        version='0.0.6',
        long_description=open(README).read(),
        author="Lucas Rangel Cezimbra",
        author_email="lucas.cezimbra@gmail.com",
        license="MIT License",
        url='https://github.com/Lrcezimbra/pysympla',
        keywords=['sympla', 'scraper', 'requests', 'events'],
        install_requires=open(REQUIREMENTS).readlines(),
        packages=['pysympla'],
        zip_safe=False,
        include_package_data=True,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: Portuguese (Brazilian)',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.0',
            'Programming Language :: Python :: 3.1',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3 :: Only',
        ])
    )
