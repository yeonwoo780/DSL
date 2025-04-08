from fastapi import FastAPI
from router import (
    user_info, 
    gen_model_info
)
import uvicorn, asyncio

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')
app.include_router(user_info.router)
app.include_router(gen_model_info.router)

async def server_main():
    config = uvicorn.Config("app:app", host='0.0.0.0',port=13000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == '__main__':
    asyncio.run(server_main())