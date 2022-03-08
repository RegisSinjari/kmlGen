import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kmlGen",
    version="0.0.1",
    author="Regis Sinjari",
    author_email="regis.sinjari@live.com",
    description="simple kml file generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RegisSinjari/kmlGen",
    project_urls={
        "Bug Tracker": "https://github.com/RegisSinjari/kmlGen/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)