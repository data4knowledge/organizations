from fastapi import FastAPI, Request
from rdfogm import Model, RdfTypeProperty, DataProperty, PropertyUri

class RaTest(Model):
    rdf_type = RdfTypeProperty(PropertyUri("http://www.data4knowledge.dk/schema/organizations#RegistrationAuthority"))

class NsTest(Model):
    rdf_type = RdfTypeProperty(PropertyUri("http://www.data4knowledge.dk/schema/organizations#Namespace"))
    name = DataProperty(**{'name': 'name', 'cardinality': 'one', 'predicate': PropertyUri("http://www.data4knowledge.dk/schema/organizations#name")})
    short_name = DataProperty(**{'name': 'short_name', 'cardinality': 'one', 'predicate': PropertyUri("http://www.data4knowledge.dk/schema/organizations#shortName")})
    #rel = ObjectProperty(**{'name': 'rel', 'predicate': PropertyUri("http://www.w3.org/rel")})
    #links = ObjectProperty(**{'name': 'links', 'cardinality': 'many', 'predicate': PropertyUri("http://www.w3.org/links")})

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.api_route("/{path_name:path}", methods=["GET"])
async def catch_all(request: Request, path_name: str):
    print("Path:", path_name)
    print("Request:", request.url)
    uri = PropertyUri(f'http://www.data4knowledge.dk/{path_name}')
    print("URI:", uri)
    ns = NsTest.find(uri)
    print("Result:", ns)
    if ns == None:
        return {"request_method": request.method, "path_name": path_name}
    else:
        return {"name": ns.name, "short_name": ns.short_name, "triples": ns.triples}
    