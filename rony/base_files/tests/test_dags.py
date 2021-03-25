import os

from airflow.models import DagBag

def test_dags_load_with_no_errors():
    for dag_name in os.listdir('../dags'):
        dag_bag = DagBag(include_examples=False)
        dag_bag.process_file(dag_name)
        assert len(dag_bag.import_errors) == 0
