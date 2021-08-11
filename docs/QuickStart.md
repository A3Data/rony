# Quick Start

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

## Implementation suggestions

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
