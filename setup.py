from setuptools import setup, find_packages

setup(
    name="AssumpHelp", 
    version="0.1.0",            
    packages=find_packages(),   
    install_requires=[
        "numpy>=1.26.0",
        "pandas>=2.0.0",
        "scipy>=1.10.0",
        "statsmodels>=0.14.0",
        "scikit-learn>=1.3.0",
        "matplotlib>=3.7.0",
    ],         
    author="Badilla",
    author_email="rodelpellazar1@gmail.com",
    description="Linear Regression Assumption Interpretation Guide",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rodelcoder1/AssumpHelp",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
