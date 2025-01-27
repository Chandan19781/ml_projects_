from setuptools import find_packages,setup
setup(
name='ml_project',
author='chandan',
version='0.0.1',
author_email='ck052142@gmail.com',
packages=find_packages(),
install_requries=get_requirement('requirement.txt')
)