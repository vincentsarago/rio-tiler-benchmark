"""Setup for rio-tiler-benchmark."""

from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

# Runtime requirements.
inst_reqs = []

extra_reqs = {
    "test": [
        "pytest",
        "pytest-benchmark",
        "rio-tiler @ git+https://github.com/cogeotiff/rio-tiler.git@warpOverview",
        "rio-cogeo"
    ]
}

setup(
    name="rio-tiler-benchmark",
    version="0.0.1",
    python_requires=">=3",
    description=u"""Benchmark rio-tiler""",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    zip_safe=False,
    install_requires=inst_reqs,
    extras_require=extra_reqs,
)
