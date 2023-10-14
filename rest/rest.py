from fastapi import FastAPI
from pydantic import BaseModel, Field
import wikipedia
wikipedia.set_lang('RU')
app = FastAPI()


class Bd(BaseModel):
    fullname: str
    
    
@app.get("/paths/{path}")
def get_path(path: str):
    path_of_content = wikipedia.page(path).url
    return{"data": path_of_content}

@app.get("/queries/{query}")
def get_query(query: str):
    
    query_to_content = wikipedia.page(query).content
    return {"data": query_to_content}



@app.post("/bodies/{body}")
def post_body(body: Bd):
    person_info = wikipedia.page(body.fullname).content
    return {"status":200, "data": person_info}
    
    
    