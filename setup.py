from setuptools import setup, find_packages

setup(
    name="math_quiz",                  # Name of the package
    version="0.1.0",                           # Initial version
    author="divya",
    author_email="divya@myemail.com",
    description="DSSS Homework_2 for generating random math problems",               # Short description
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/divya-dan/dsss_HW.git",  # URL of your Git repository
    packages=find_packages(),                  # Automatically finds and includes your packages
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",                   # Python version requirement

    entry_points={
    'console_scripts': [
        'math_quiz=math_quiz:main',  # Example
    ],
}

)
