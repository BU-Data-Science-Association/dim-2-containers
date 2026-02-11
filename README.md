# dim-2-containers

Data in Motion 2: Containers

This workshop introduces containerization concepts using Docker, progressing from single-container applications to multi-container orchestrated systems.

## Workshop Structure

### Part 1: Single Container Application

- **Location**: `part1/`
- **Files**:
  - `Dockerfile`: Container definition for a Python application
  - `message.py`: Python script that prints a joke
- **Objective**: Learn basic Docker concepts by containerizing a simple Python script

### Part 2: Multi-Container Data Pipeline

- **Location**: `part2/`
- **Files**:
  - `docker-compose.yaml`: Orchestration configuration for the entire stack
  - `ingest/`: Data ingestion service
    - `app.py`: Fetches ISS position data from API and stores in PostgreSQL
    - `Dockerfile`: Container definition
    - `requirements.txt`: Python dependencies (requests, psycopg2-binary)
  - `transform-worker/`: Data transformation service
    - `app.py`: Calculates latitude/longitude changes between consecutive ISS positions
    - `Dockerfile`: Container definition
    - `requirements.txt`: Python dependencies (requests, psycopg2-binary)
- **Objective**: Build a complete data pipeline using Docker Compose with PostgreSQL, ingestion, and transformation services

## Prerequisites

- Docker Desktop installed and running
- Basic understanding of Python
- Familiarity with command line operations

## Getting Started

### Part 1: Single Container

1. Navigate to the part1 directory:

   ```bash
   cd part1
   ```

2. Complete the `message.py` script to print a joke

3. Complete the `Dockerfile` with appropriate instructions:
   - Base image (Python runtime)
   - Working directory
   - Copy the Python script
   - Command to run the script

4. Build and run the container:
   ```bash
   docker build -t joke-app .
   docker run joke-app
   ```

### Part 2: Multi-Container Pipeline

1. Navigate to the part2 directory:

   ```bash
   cd part2
   ```

2. Start the entire stack:

   ```bash
   docker-compose up --build
   ```

3. The pipeline will:
   - Start a PostgreSQL database
   - Launch the ingest service to fetch ISS position data every 5 seconds
   - Launch the transform-worker to calculate position changes every 30 seconds

4. Monitor the logs to see data being processed

5. To stop the services:
   ```bash
   docker-compose down
   ```

## Learning Objectives

- Understand containerization fundamentals
- Create Dockerfiles for Python applications
- Use Docker Compose for multi-service applications
- Implement data ingestion and transformation patterns
- Work with containerized databases
- Handle inter-service dependencies

## Data Flow (Part 2)

1. **Ingest Service**: Polls the Open Notify ISS API every 5 seconds
2. **Database**: Stores raw position data in PostgreSQL
3. **Transform Worker**: Processes unprocessed records, calculating lat/long changes from previous positions
4. **Database**: Updates records with calculated changes

## Troubleshooting

- Ensure Docker Desktop is running
- Check container logs with `docker-compose logs <service-name>`
- Verify port 5432 is available (PostgreSQL)
- Use `docker-compose ps` to check service status
