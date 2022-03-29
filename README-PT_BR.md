![Rony - Data Engineering made simple](img/Logo_Rony_horizontal.png)

[![PyPI version fury.io](https://badge.fury.io/py/rony.svg)](https://pypi.python.org/pypi/rony/)
![Test package](https://github.com/A3Data/rony/workflows/Test%20package/badge.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub issues](https://img.shields.io/github/issues/a3data/rony.svg)](https://GitHub.com/a3data/rony/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/a3data/rony.svg)](https://GitHub.com/a3data/rony/issues?q=is%3Aissue+is%3Aclosed)
[![PyPI status](https://img.shields.io/pypi/status/rony.svg)](https://pypi.python.org/pypi/rony/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/rony.svg)](https://pypi.python.org/pypi/rony/)
[![PyPi downloads](https://pypip.in/d/rony/badge.png)](https://crate.io/packages/rony/)

Um framework de Engenheria de Dados opinativo

Desenvolvido com ❤️ por <a href="http://www.a3data.com.br/" target="_blank">A3Data</a>

## O que é Rony 

Rony é um framework **open source** que ajuda os Engenheiros de Dados a configurar um código mais organizado e construir, testar e implantar pipelines de dados mais rapidamente.

## Porque Rony?

Rony é o *melhor amigo* da <a href="https://github.com/A3Data/hermione" target="_blank">Hermione</a>'s (ou então...). 

Esta foi uma escolha perfeita para nomear o segundo framework lançado pela A3Data, este com foco em Engenharia de Dados.

Em muitos anos ajudando empresas a construir seus projetos de análise de dados e infraestrutura em nuvem, adquirimos
uma base de conhecimento que levou a uma coleção de trechos de código e procedimentos de automação que aceleram as coisas
quando se trata de desenvolver estrutura de dados e pipelines de dados.

## Algumas escolhas que fizemos

Rony conta com algumas decisões que fazem sentido para a maioria dos projetos conduzidos pela A3Data: 

- <a href="https://www.terraform.io/intro/index.html" target="_blank">Terraform (>= 0.13)</a>
- <a href="https://www.docker.com/" target="_blank">Docker</a>
- <a href="https://airflow.apache.org/" target="_blank">Apache Airflow</a>
- <a href="https://aws.amazon.com/" target="_blank">AWS</a>

Você é livre para alterar essas decisões como desejar (esse é o ponto principal do framework - **flexibilidade**).

# Instalação

### Dependências

- Python (>=3.6)
- pip (>= 22.0.4)

### Instalar

```bash
pip install -U rony
```

### Habilitar autocompletion (usuários unix):

Para bash:

```bash
echo 'eval "$(_RONY_COMPLETE=bash_source rony)"' >> ~/.bashrc
```

Para Zsh:

```bash
echo 'eval "$(_RONY_COMPLETE=zsh_source rony)"' >> ~/.zshrc
```

# Como usar o Rony?

Depois de instalar o Rony teste se a instalação está ok para rodar:

```bash
rony info
```

e você verá um logotipo fofo. Então,

1) Crie um novo projeto:

```bash
rony new project_rony
```

2) Rony já cria um ambiente virtual para o projeto.
Os usuários do Windows podem ativá-lo com

```
<project_name>_env\Scripts\activate
```

Os usuários Linux e MacOS podem fazer com

```bash
source <project_name>_env/bin/activate
```

3) Após a ativação, você deve instalar algumas bibliotecas. Existem algumas sugestões no arquivo “requirements.txt”:

```bash
pip install -r requirements.txt
```

4) Rony também tem alguns comandos cli úteis para construir e executar imagens do docker localmente. Você pode fazer

```bash
cd etl
rony build <image_name>:<tag>
```

para construir uma imagem e executá-la com

```bash
rony run <image_name>:<tag>
```

Nesta implementação em particular, o `run.py` tem um código etl simples que aceita um parâmetro para filtrar os dados com base na coluna `Sexo`. Para usar isso, você pode fazer

```bash
docker run <image_name>:<tag> -s female
```

# Sugestões de implementação

Quando você inicia um novo projeto `rony`, você encontrará

- uma pasta `infrastructure` com criação de código terraform na AWS:
  - um S3 bucket
  - uma função Lambda
  - um grupo de logs do CloudWatch
  - um repositório ECR
  - um AWS Glue Crawler
  - Funções e políticas do IAM para lambda e glue

- uma pasta `etl` com:
  - um `Dockerfile` e um exemplo `run.py` de código ETL
  - um `lambda_function.py` com um exemplo "Hello World"

- uma pasta `tests` com teste de unidade na função Lambda
- uma pasta `.github/workflow` com uma sugestão de pipeline Github Actions CI/CD. Este pipeline:
  - Testa a função lambda
  - Cria e executa a imagem do docker
  - Define as credenciais da AWS
  - Faça um plano de terraform (mas não implante nada)

- uma pasta `dags` com algum código de exemplo do **Airflow** code.f

Você também tem uma pasta `scripts` com um arquivo bash que cria um pacote de implantação lambda.

**Sinta-se à vontade para ajustar e adaptar tudo de acordo com suas necessidades.**


## Contribuição

Dê uma olhada no nosso [guia de contribuição](CONTRIBUTING.md).

Crie um pull request com a sua implementação.

Para sugestões, entre em contato: rony@a3data.com.br

## Licença
Rony é open source e tem Apache 2.0 License: [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
