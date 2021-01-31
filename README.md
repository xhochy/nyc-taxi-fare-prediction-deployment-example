Deployment example for a scikit-learn/lightgbm pipeline
=======================================================

This project shows a simple machine learning pipeline that uses `scikit-learn` and `lightgbm`.
We train a model based on the New York Taxi trip dataset and then deploy it using FastAPI.

Development
-----------

This package is intended to be developed inside a conda environment defined with the environment.yml. With the following commands you can setup the development environment initially:

```
mamba env create
conda activate quantcore-reproduce
python -m pip install --no-deps --disable-pip-version-check -e .
```

Deployment
----------

As this repository is an example for various ways to deploy a pipeline inside a docker container, there are several flavour present.
We have supplied a small `Makefile` that can be used to execute the `docker build` command for each of them.

```
# Build the container
make anaconda
# Run the container
docker run -t nyc-taxi-anaconda -p 8000:8000
```
