'''
The setup.py file is a part of packaging and distributing python projects.
It is used by setuptools to define the configuration of our project such as metadata, dependencies and more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''
    requirement_list:List[str]= []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from requirements.txt
            lines = file.readlines()
            # Process the line
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and '-e .'
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

setup(
    name="Phishing Domain Detection System",
    version="0.0.1",
    author="Akshada Bauskar",
    author_email="akshada.bauskar171222@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements()
)