from setuptools import setup, find_packages

setup(
    name="Fido",  
    version="0.1.0", 
    author="Saranya", 
    author_email="saranyaece29@gmail.com",  
    description="Fido interview assessment",  
    long_description=open("README.md").read(), 
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/Fido",  
    packages=find_packages(),  
    install_requires=[ 
        "requests>=2.25.1",
        "numpy>=1.21.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7", 
)
