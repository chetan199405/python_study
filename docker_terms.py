| Term                     | Simple Explanation                                                    | Example or Analogy                       |
| ------------------------ | --------------------------------------------------------------------- | ---------------------------------------- |
| **Docker**               | A tool to run apps inside isolated environments called **containers** | Like running apps in a safe box 📦       |
| **Container**            | A lightweight, standalone instance of your app with all dependencies  | Like a ready-to-eat packed meal 🍱       |
| **Image**                | A read-only snapshot (template) to create containers                  | Like a recipe 📄 to make meals           |
| **Dockerfile**           | A script with steps to build a Docker image                           | Like cooking instructions 🍳             |
| **Docker Hub**           | Online registry where images are stored and shared                    | Like Play Store for Docker apps 🌐       |
| **Build**                | Process of creating a Docker image from a Dockerfile                  | `docker build -t myapp .`                |
| **Run**                  | Starts a container from an image                                      | `docker run myapp`                       |
| **Pull**                 | Downloads an image from Docker Hub                                    | `docker pull python:3.9`                 |
| **Push**                 | Uploads your image to Docker Hub                                      | `docker push username/myapp`             |
| **Tag**                  | A version label given to an image                                     | `myapp:latest`, `myapp:v1.0`             |
| **Volume**               | Persistent storage outside the container                              | Saves user data (like database files)    |
| **Port Mapping**         | Makes container app accessible on local machine                       | `-p 5000:5000` → exposes container port  |
| **Container ID**         | Unique ID assigned to each running container                          | Used in commands like `docker stop <id>` |
| **Environment Variable** | Settings passed to containers at runtime                              | `-e ENV=production`                      |
| **ENTRYPOINT / CMD**     | Commands to run when container starts                                 | Usually starts your app                  |
| **Expose**               | Declares which port the app inside container listens on               | `EXPOSE 5000` in Dockerfile              |
| **Layers**               | Each instruction in Dockerfile creates a layer (cached step)          | Makes building faster                    |
| **Context**              | The files/folders in the current directory during `docker build`      | `.` (dot) in `docker build -t myapp .`   |
| **Registry**             | A storage for Docker images (Docker Hub is a public registry)         | Can be private or public                 |
| **Docker Engine**        | The core service running Docker commands                              | Backend system of Docker                 |
| **Bind Mount**           | Link between a local file/folder and container                        | Share code between host and container    |
| **Detached Mode**        | Runs container in background                                          | `docker run -d myapp`                    |
| **Interactive Mode**     | Attach terminal to container                                          | `docker run -it ubuntu /bin/bash`        |
| **Compose**              | Tool to manage multi-container apps                                   | `docker-compose up`                      |
| **Swarm**                | Docker’s built-in orchestration (like Kubernetes)                     | For managing clusters of containers      |
