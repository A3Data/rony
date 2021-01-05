import pytest
import etl.lambda_function as lf
import os


def test_response():
    res = lf.handler(None, None)
    assert res['statusCode'] == 200