from fastapi import FastAPI

app = FastAPI

app.post("/register")
async def register():
    pass


app.post("/unregister")
async def unregister():
    pass 