from setuptools import setup
from setuptools import find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name = 'seins',
    packages=find_packages(),
    version = '0.3.2',
    description='A  small module and  command line utility to show you when the '
                'next train to your desired location is arriving by parsing the DB website',
    long_description = long_description,
    author = 'Kai',
    author_email = 'kai@woistbier.de',
    install_requires = [ 'colorama', 'requests', ' beautifulsoup4', 'lxml' ],
    url = 'https://github.com/kbruegge/sEins-Server',   # use the URL to the github repo
    download_url='https://github.com/kbruegge/sEins-Server/archive/master.zip',
    keywords=['traffic', 'scrapping', 'utility', 'transportation', 's1', 'DB'],
    license = 'MIT',
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "console_scripts": [
            "s1 = cmd_line.seins_cmd:main",
            "seins = cmd_line.seins_cmd:main",
        ],
    }
)
