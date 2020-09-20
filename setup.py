from setuptools import setup, find_packages

setup(
    name='IA Workplace',
    version='1.0',
    description='Módulo Principal do Projeto',
    author='Juan & Monge',
    #install_requires=['numpy ', 'pysimplegui',
    #                'pandas', 'matplotlib'],
    install_requires=['numpy', 'mpmath'],
    packages=find_packages(),
)
