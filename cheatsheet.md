# Docker & Container Commands Cheatsheet

## Terminal Basics

### Navigation

```bash
pwd                    # Print current working directory
ls                     # List files in current directory
cd <directory>         # Change to specified directory
cd ..                  # Go up one directory level
```

## Docker Commands

### Images

```bash
docker images          # List all local images
docker pull <image>    # Pull image from registry
docker build -t <name> .  # Build image from Dockerfile
docker rmi <image>     # Remove image
docker image prune     # Remove unused images
```

### Containers

```bash
docker ps              # List running containers
docker run <image>     # Run container from image
docker start <container>  # Start stopped container
docker stop <container>  # Stop running container
docker restart <container>  # Restart container
docker logs <container>  # Show container logs
docker rm <container>   # Remove container
docker container prune  # Remove stopped containers
```

### Volumes

```bash
docker volume ls       # List volumes
docker volume create <name>  # Create volume
docker volume rm <name>  # Remove volume
docker volume prune     # Remove unused volumes
```

## Docker Compose Commands

### Basic Operations

```bash
docker-compose up      # Start services
docker-compose up -d   # Start services in background
docker-compose up --build  # Build and start services
docker-compose down    # Stop and remove services
docker-compose stop    # Stop services without removing
docker-compose start   # Start stopped services
docker-compose restart # Restart services
```

## Docker Compose File Structure

```yaml
version: "3.8"
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
  db:
    image: postgres:13
    environment:
      POSTGRES_PASSWORD: password
    volumes:
      - db_data:/var/lib/postgresql/data
volumes:
  db_data:
```
