from setuptools import find_packages, setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='MultiConTest',
    version='1.0',
    packages=['multicontest'],
    entry_points={
        'console_scripts': [
            'MultiConTest = multicontest.App:main'
        ]
    },
    install_requires=[
        'PySide6==6.5.2',
        'pandas==2.1.0',
        'numpy==1.25.2',
        'matplotlib==3.7.2',
        'scipy==1.11.2'
    ],
    python_requires='>=3.11.3',
    author='Nicolas Kersten',
    author_email='nicolas.kersten@uni-tuebingen.de',
    description='A GUI application that allows for easy identification of confounding factors in multimodal data',
    long_description=long_description,
    license='GNU General Public License v3.0',
    keywords='confounding factors, clustering, multimodal data, bioinformatics, data analysis, multi-omics, multi-view',
    url='https://github.com/pfeiferAI/MultiConTest'
)