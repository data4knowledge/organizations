# Building Package

```
pip install wheel         
pip install twine   
python setup.py sdist bdist_wheel  
twine check dist/*  
```

For test repository

```
twine upload --repository-url https://test.pypi.org/legacy/ dist/*              
```

Install version form Test

```
pip install -i https://test.pypi.org/pypi/ --extra-index-url https://pypi.org/simple rdfogm==0.0.4
```

# Build Docker Image

Build the image

```
docker build -t organization .  
```

List the images

```
docker images  
```

Tag the image

```
docker tag organization:latest organization:v0.0.1
```

Run image

```
docker run -d --name organization -p 80:80 organization:latest
```

# Running Docker

## Configuration 

Contents of file rdfogm_config.yml

```
rdf_types: 
  http://www.data4knowledge.dk/schema/organizations#Namespace: NsTest
  http://www.data4knowledge.dk/schema/organizations#RegistrationAuthority: RaTest
default_graph: http://www.data4knowledge/graphs/test
host: fuseki
```

## Fuseki And Organizations Containers

Run the two containers

```
docker run -p 3030:3030 --name fuseki daveih/fuseki:v3.16.0 --loc ds --update /test 
docker run  --name organization -p 80:80 organization
```

Create the docker network

```
docker network create microservice-network 
docker network inspect microservice-network
docker network connect microservice-network fuseki   
docker network connect microservice-network organization
```

Expected results

```
http://0.0.0.0/mdr/ORG/DUNS123456789
{"detail":"URI not found"}
http://0.0.0.0/
{"message":"Organization microservice, version 1.0.0"}
```



