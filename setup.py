from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="niph",
    version="0.1",
    description="Tools for searching and text mining transcribed podcasts",
    url="https://github.com/lambdaofgod/niph",
    author="Jakub Bartczuk",
    packages=find_packages(),
    install_requires=requirements,
)
