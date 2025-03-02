from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ayaka-models-emotensor",
    version="0.0.1",
    author="Lexa-B",
    description="Emotional Tensor Models for Ayaka AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lexa-B/Ayaka_Model_EmoTensor",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pydantic>=2.10.6",
    ],
) 