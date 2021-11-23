from setuptools import setup
import pathlib
import pkg_resources

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name='whatajoke',
    version='1.0',
    packages=['whatajoke'],
    url='https://github.com/joaoduartepinto/whatajoke',
    download_url='https://github.com/joaoduartepinto/whatajoke/archive/refs/tags/v1.0.tar.gz',
    license='GPLv3',
    author='João Duarte Pinto',
    author_email='joaoduartepinto@outlook.com',
    description='Send a joke to a Whatsapp group!',
    entry_points={
        'console_scripts': ['wj=whatajoke.whatajoke:main']
    },
    install_requires=install_requires,
)
