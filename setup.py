from setuptools import find_packages,setup
from typing import List



def get_requirements(file_path:str) -> list[str]:

    '''
    this will return the lsit of  requirements
    '''
    requirement=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','') for req in requirements]

    return requirements







setup(
    name='mlproject',
    version='0.0.1',
    author='karan pratap',
    author_email='kplohiya2005@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')

)