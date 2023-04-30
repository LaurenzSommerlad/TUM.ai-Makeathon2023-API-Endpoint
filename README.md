# CanAI FastAPI Backend

## Running with Dockerfile (local, recommended)

1) Install docker
2) Build and run the container

    ```sh
    docker build -t canai-fastapi-docker .
    docker run -p 4321:80 canai-fastapi-container
    ```
    This will run the server under ```http://localhost:4321```