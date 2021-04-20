from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt", "r") as req:
        content = req.read()
        requirements = content.split("\n")
    return requirements

setup(
        name="scrapr-cli",
        version="0.0.1",
        author="Shahriyar Khan",
        author_email="kshahriyar4@gmail.com",
        description="A light weight cli tool that scrapes email addresses",
        url="https://github.com/shahriyar-khan/scrapr-cli",
        packages=find_packages(),
        include_package_data=True,
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating Systems :: OS Independent",
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: End Users/Desktop"
        ],
        install_requires=read_requirements(),
        entry_points="""
            [console_scripts]
            scrapr=scrapr_cli.app:scrapr
        """
)