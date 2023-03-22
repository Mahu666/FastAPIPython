#region Imports
from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse
import database as db
#endregion

#region Params
headersGet = {
       # "content-type": "charset=utf-8"
    }
#endregion

app = FastAPI()

#region Endpoint for simple TEXT
@app.get("/")
async def index():
    content = {"mensaje": "¡Hola API ñ ó!"}
    return JSONResponse(
        content = content,
        headers = headers,
        media_type="application/json")
#endregion

#region Endpoint for simple html  Bloques
@app.get('/html/')
async def html():
    content = """
    <!DOCTYPE html>
<html>
<head>
<title>Title of the document</title>
</head>

<body>
<h1> ¡Haaaaaaaaa! </h1>
</body>

</html>
    """
    return Response(content=content, media_type="text/html")
#endregion

#region Endpoint GET
@app.get('/clientes/')
async def clientes():
    content = [
        #Descomentar y borrar to_dict en database.py en Cliente
        #{
        #    'dni': cliente.dni, 'nombre': cliente.nombre, 'apellido': cliente.apellido
        #}
        cliente.to_dict()
        for cliente in db.Clientes.lista
        
    ]
    return JSONResponse(content=content)
#endregion

#region Endpoint Get by One
@app.get('/clientes/buscar/{dni}')
async def clientes_buscar(dni: str):
    cliente = db.Clientes.buscar(dni=dni)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado error 404 NOT FOUND")
    return JSONResponse(content=cliente.to_dict())
#endregion