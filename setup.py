import uvicorn

from app.main import fast_app

if __name__ == "__main__":
    uvicorn.run(fast_app, host="0.0.0.0", port=8000)
