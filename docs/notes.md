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

