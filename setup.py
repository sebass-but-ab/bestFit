from setuptools import setup, find_packages
setup(
  name = "bestFit",
  version='0.1.2',
  licence ="MIT",
  author = "SebassNoob",
  description="A small example package",
  long_description=open("README.md","r").read(),
  long_description_content_type="text/markdown",
  author_email="sebastian.ong@hotmail.com",
  packages=find_packages('src'),
  install_requires=[
    'numpy',
    'matplotlib'
  ],
  
  
)