# Cria o diretório e instala as dependências da função lambda
mkdir package
pip install --target ./package -r ./etl/lambda_requirements.txt

# Zipa o pacote para deploy
cd package
cp ../etl/lambda_function.py .
zip -r9 ../infrastructure/lambda_function_payload.zip .
cd ..