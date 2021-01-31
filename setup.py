from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md")) as f:
    long_description = f.read()

setup(
    name="nyc_taxi_fare",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="Deployment example for a simple scikit-learn model deployment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xhochy/nyc-taxi-fare-prediction-deployment-example",
    author="Uwe L. Korn",
    author_email="noreply@uwekorn.com",
    classifiers=[  # Optional
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={"console_scripts": ["nyc_taxi_fare_train = nyc_taxi_fare.cli:train"]},
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "scikit-learn",
        "lightgbm",
        "pandas",
        "pyarrow",
    ],
)
