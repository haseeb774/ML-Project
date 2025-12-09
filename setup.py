from setuptools import find_packages,setup
from typing import List
HYPHENDOT = "-e ."
def get_requirements(file_path:str)->list[str]:
    requirements = []
    with open(file_path) as file_obj:   
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHENDOT in requirements:
            requirements.remove(HYPHENDOT)
    return requirements        
setup(
    name="mlproject",
    version="0.0.1",
    author="Haseeb-u-Rehman",
    author_email="haseeb16001@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)