FROM python:3.10
RUN python3 -m pip install --upgrade pip
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN python3 -m pip install --index-url https://test.pypi.org/simple/ rdfogm
COPY ./organizations /code/organizations
RUN touch .env
RUN echo TRIPLE_STORE_PROTOCOL="http" >> .env
RUN echo DEFAULT_GRAPH="http://www.data4knowledge/graphs/test" >> .env
RUN cat .env
CMD ["uvicorn", "organizations.main:app", "--host", "0.0.0.0", "--port", "80"]
