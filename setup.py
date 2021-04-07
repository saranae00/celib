from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:  # README.md 내용 읽어오기
    long_description = f.read()
setup(
    name="celib",
    version="0.0.2.1",
    description="celib",
    author="cekwak",
    author_email="saranae00@gmail.com",
    url="https://github.com/saranae00/celib",
    download_url="https://github.com/saranae00/celib/archive/refs/tags/0.0.2.tar.gz",
    install_requires=["pandas", "numpy", "pathos"],
    packages=find_packages(exclude=[]),
    keywords=["celib"],
    python_requires=">=3.6",
    package_data={},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    py_modules=["celib.common"],
)
