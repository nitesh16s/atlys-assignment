from fastapi import FastAPI
from scrappy import run

app = FastAPI()


@app.get("/page/{page_num}")
def read_item(page_num: int):
    run(page_num, n_secs=3)
    return {"results": 'Scrapping done'}
    # return {"results": results}

