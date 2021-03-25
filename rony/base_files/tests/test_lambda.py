import etl.lambda_function as lf

def test_response():
    res = lf.handler(None, None)
    assert res['statusCode'] == 200