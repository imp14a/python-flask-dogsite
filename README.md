# To run this application

This is part of a packer sample, you can find the packer build here: https://github.com/imp14a/gcp-packer-ansible-sample

## Requires
- Python 3 
- pip installation
- apt install python3.9-venv

## Create enviroment
```
python3 -m venv venv
. venv/bin/activate
python3 -m pip install Flask
pip freeze > requirements.txt
```

## Run
´´´
pip install -r requirements.txt
export FLASK_APP=getapug
flask run --debug
flask run --host=0.0.0.0
´´´

## Docker build and run
´´´
docker image build -t pugsite .
´´´