import os

def test_zip_lambda():
    os.system('cd .. && sh scripts/build_lambda_package.sh')
    assert os.path.isfile('../infrastructure/lambda_function_payload.zip') is True
