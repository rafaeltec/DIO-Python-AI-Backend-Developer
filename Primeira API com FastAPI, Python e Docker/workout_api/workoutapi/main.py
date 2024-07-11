from fastapi import FastAPI

app = FastAPI(title='WorkoutApi')



    
@app.get("/")
async def root():
    return {"message": "Hello World"}