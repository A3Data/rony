# Rony - Data Engineering made simple

[![PyPI version fury.io](https://badge.fury.io/py/rony.svg)](https://pypi.python.org/pypi/rony/)
![Test package](https://github.com/A3Data/rony/workflows/Test%20package/badge.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub issues](https://img.shields.io/github/issues/a3data/rony.svg)](https://GitHub.com/a3data/rony/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/a3data/rony.svg)](https://GitHub.com/a3data/rony/issues?q=is%3Aissue+is%3Aclosed)
[![PyPI status](https://img.shields.io/pypi/status/rony.svg)](https://pypi.python.org/pypi/rony/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/rony.svg)](https://pypi.python.org/pypi/rony/)
[![PyPi downloads](https://pypip.in/d/rony/badge.png)](https://crate.io/packages/rony/)

An opinionated Data Engineering framework

Developed with ❤️ by <a href="http://www.a3data.com.br/" target="_blank">A3Data</a>

## What is Rony

Rony is an **open source** framework that helps Data Engineers setting up more organized code and build, test and deploy data pipelines faster.

## Why Rony?

Rony is <a href="https://github.com/A3Data/hermione" target="_blank">Hermione</a>'s *best friend* (or so...). 
This was a perfect choice for naming the second framework
released by A3Data, this one focusing on Data Engineering. 

In many years on helping companies building their data analytics projects and cloud infrastructure, we acquired 
a knowledge basis that led to a collection of code snippets and automation procedures that speed things up
when it comes to developing data structure and data pipelines.

## Some choices we made

Rony relies on top of a few decisions that make sense for the majority of projects conducted by A3Data:

- <a href="https://www.terraform.io/intro/index.html" target="_blank">Terraform (>= 0.13)</a>
- <a href="https://www.docker.com/" target="_blank">Docker</a>
- <a href="https://airflow.apache.org/" target="_blank">Apache Airflow</a>
- <a href="https://aws.amazon.com/" target="_blank">AWS</a>

You are free to change this decisions as you wish (that's the whole point of the framework - **flexibility**).

# Installing

### Dependencies

- Python (>=3.6)

### Install

```bash
pip install -U rony
```

# How do I use Rony?

After installing Rony you can test if the installation is ok by running:

```bash
rony info
```

and you shall see a cute logo. Then,

1) Create a new project:

```bash
rony new project_rony
```

2) Rony already creates a virtual environment for the project. 
Windows users can activate it with 

```
<project_name>_env\Scripts\activate
```

Linux and MacOS users can do

```bash
source <project_name>_env/bin/activate
```

3) After activating, you should install some libraries. There are a few suggestions in “requirements.txt” file:

```bash
pip install -r requirements.txt
```

4) Rony has also some handy cli commands to build and run docker images locally. You can do

```bash
cd etl
rony build <image_name>:<tag>
```

to build an image and run it with

```bash
rony run <image_name>:<tag>
```

In this particular implementation, `run.py` has a simple etl code that accepts a parameter to filter the data based on the `Sex` column. To use that, you can do

```bash
docker run <image_name>:<tag> -s female
```

# Implementation suggestions

When you start a new `rony` project, you will find

- an `infrastructure` folder with terraform code creating on AWS:
  - an S3 bucket
  - a Lambda function
  - a CloudWatch log group
  - a ECR repository
  - a AWS Glue Crawler
  - IAM roles and policies for lambda and glue

- an `etl` folder with:
  - a `Dockerfile` and a `run.py` example of ETL code
  - a `lambda_function.py` with a "Hello World" example

- a `tests` folder with unit testing on the Lambda function
- a `.github/workflow` folder with a Github Actions CI/CD pipeline suggestion. This pipeline
  - Tests lambda function
  - Builds and runs the docker image
  - Sets AWS credentials
  - Make a terraform plan (but not actually deploy anything)

- a `dags` folder with some **Airflow** example code.f

You also have a `scripts` folder with a bash file that builds a lambda deploy package.

**Feel free to adjust and adapt everything according to your needs.**


## Contributing

Make a pull request with your implementation.

For suggestions, contact us: rony@a3data.com.br

## Licence
Rony is open source and has Apache 2.0 License: [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)