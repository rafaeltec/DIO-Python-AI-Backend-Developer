from fastapi import FastAPI

app = FastAPI(title='WorkoutApi')


if __name__ =='main':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='infor', reload=True)
    
@app.get("/")
async def root():
    return {"message": "Hello World"}