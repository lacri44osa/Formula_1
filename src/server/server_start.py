from fastapi import FastAPI
import uvicorn
from db_manager import db_manager
from settings import SCRIPTS_TABLES_PATH
from fastapi.responses import RedirectResponse
from personal_data import routers as pd_router

app = FastAPI(title= "Formula 1")

app.include_router(pd_router, prefix='/personal_data')

@app.get('/')
def root():
    return RedirectResponse('/docs')

if __name__ == '__main__':
    if not db_manager.check_base():
        db_manager.create_base(SCRIPTS_TABLES_PATH)
    uvicorn.run(app="start_server:app", host="0.0.0.0",  port=8000, reload=True)