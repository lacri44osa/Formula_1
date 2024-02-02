import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from Server.db_manager import base_manager
from Server.settings import SCRIPTS_TABLES_PATH
from routers import (visitors_router, violator_router,
                     personal_data_router)

app = FastAPI(
    title='Formula 1'
)

app.include_router(visitors_router, prefix='/visitors')
app.include_router(violator_router, prefix='/violator')
app.include_router(personal_data_router, prefix='/personal_data')


@app.get('/')
def root():
    return RedirectResponse('/docs')


if __name__ == '__main__':
    if not base_manager.check_base():
        base_manager.create_base(SCRIPTS_TABLES_PATH)
    uvicorn.run(app="start_server:app", host="127.0.0.1",  port=8000, reload=True)