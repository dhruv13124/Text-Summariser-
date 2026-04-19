import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()
    
    
_version_="0.0.0"

REPO_NAME="Text-Summariser-"
AUTHOR_USER_NAME= "dhruv13124"   
SRC_REPO="textsummarizer" 
AUTHOR_EMAIL="dhruvjangid522@gmail.com"
 
 

setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"Bug tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    
)    
    