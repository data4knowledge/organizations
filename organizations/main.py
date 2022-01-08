import uvicorn

from fastapi import FastAPI, Request, HTTPException
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
    return {"message": "Organization microservice, version 1.0.0"}

@app.get("/organization/{item_id}")
async def organization(item_id):
    ns = RaTest.find(item_id)
    if ns == None:
        raise HTTPException(status_code=404, detail="URI not found")
    else:
        return {"name": ns.name, "short_name": ns.short_name, "triples": ns.triples}

@app.get("/namespace/{item_id}")
async def namesapce(item_id):
    ns = NsTest.find(item_id)
    if ns == None:
        raise HTTPException(status_code=404, detail="URI not found")
    else:
        return {"name": ns.name, "short_name": ns.short_name, "triples": ns.triples}

@app.api_route("/{path_name:path}", methods=["GET"])
async def resource(request: Request, path_name: str):
    uri = PropertyUri(f'http://www.data4knowledge.dk/{path_name}')
    #klass = Model.klass_for_type(uri)
    klass = NsTest
    ns = klass.find(uri)
    if ns == None:
        raise HTTPException(status_code=404, detail="URI not found")
    else:
        return {"name": ns.name, "short_name": ns.short_name, "triples": ns.triples}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)