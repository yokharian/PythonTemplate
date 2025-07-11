from setuptools import setup, find_packages

setup(
    name="yokharianpythontemplate",
    version="1.0.0",
    description="A template for quickly bootstrapping Python projects using PDM.",
    author="Sofia Escobedo",
    author_email="63127299+yokharian@users.noreply.github.com",
    url="https://github.com/yokharian/PythonTemplate",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
)
