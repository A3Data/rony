#!/usr/bin/env bash 
set -e
SCRIPT_FOLDER=$1

echo $1
# Declara variavel para reutilização nas validações do diretório
PACKAGE="$SCRIPT_FOLDER/package"

# Cria o diretório e instala as dependências da função lambda
if [ -d $PACKAGE ]
then
    echo "O Diretório "$PACKAGE" já existe."
else
    echo "============================================="
    echo "Criando o diretório "$PACKAGE"..."
    mkdir $PACKAGE
    echo "O diretório "$PACKAGE" foi criado."
    echo "============================================="
fi

# Declara variavel que localiza o requirements com as dependências do projeto
FILE_REQUIREMENTS=$SCRIPT_FOLDER/requirements.txt

# Verifica se o arquivo lambda_requirements existe
if [ -f $FILE_REQUIREMENTS ]
then
    echo "============================================="
    echo "Instalando dependências localizadas no "$FILE_REQUIREMENTS""
    pip install --target $PACKAGE -r $FILE_REQUIREMENTS
    echo "Dependências instaladas com sucesso."
    echo "============================================="
fi

# Declara variavel que localiza a função lambda para reutilização no código.
LAMBDA_FUNCTION=$SCRIPT_FOLDER/handler.py

echo basename $SCRIPT_FOLDER
# Verifica se o arquivo lambda_function.py existe
if [ -f $LAMBDA_FUNCTION ]
then
    echo "============================================="
    echo "Copiando função Handler..."
    cp $LAMBDA_FUNCTION $PACKAGE
    echo "Compactando arquivo lambda_function_payload.zip"
    cwd=$(pwd)
    cd $PACKAGE
    zip -r9 $cwd/$SCRIPT_FOLDER.zip . #Compacta o pacote para o deploy
    cd $cwd
    echo "Arquivo compactado com sucesso!"
    echo "============================================="
fi