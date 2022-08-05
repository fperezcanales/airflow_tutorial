cd airflow_tutorial

python3 -m venv .venv

source .venv/bin/activate

pip install "apache-airflow[postgres, password]"

pip freeze > requirements.txt