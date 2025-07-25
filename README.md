# FastAPI Fibonacci Calculator

A high-performance FastAPI application for calculating Fibonacci numbers with full Docker support and production-ready deployment configuration.

## Features

- **Fast Fibonacci Calculation**: Efficient iterative algorithm for calculating Fibonacci numbers
- **RESTful API**: Clean REST endpoints with automatic OpenAPI documentation
- **Docker Support**: Complete containerization with multi-stage builds and security best practices
- **Production Ready**: Health checks, error handling, and performance optimizations
- **Easy Deployment**: Docker Compose setup with deployment scripts

## API Endpoints

- `GET /` - API information and available endpoints
- `GET /fibonacci/{n}` - Calculate the nth Fibonacci number
- `GET /fibonacci/sequence/{count}` - Generate a sequence of Fibonacci numbers
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation

## Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/jngy36/fastapi_fibonacci.git
   cd fastapi_fibonacci
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

4. **Access the API**
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs

### Docker Deployment

#### Option 1: Docker Compose (Recommended)
```bash
# Deploy the application
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the application
docker-compose down
```

#### Option 2: Docker Commands
```bash
# Build the image
docker build -t fibonacci-api .

# Run the container
docker run -d -p 8000:8000 --name fibonacci-api fibonacci-api

# Stop and remove
docker stop fibonacci-api && docker rm fibonacci-api
```

#### Option 3: Using Scripts
```bash
# Make scripts executable
chmod +x scripts/*.sh

# Build and deploy
./scripts/deploy.sh

# Or build and run separately
./scripts/build.sh
./scripts/run.sh

# Stop the application
./scripts/stop.sh
```

## API Usage Examples

### Calculate Single Fibonacci Number
```bash
curl http://localhost:8000/fibonacci/10
```
Response:
```json
{
  "input": 10,
  "fibonacci": 55,
  "calculation_time_seconds": 0.000001
}
```

### Generate Fibonacci Sequence
```bash
curl http://localhost:8000/fibonacci/sequence/5
```
Response:
```json
{
  "count": 5,
  "sequence": [0, 1, 1, 2, 3],
  "calculation_time_seconds": 0.000002
}
```

### Error Handling
```bash
curl http://localhost:8000/fibonacci/-1
```
Response:
```json
{
  "detail": "Fibonacci is not defined for negative numbers"
}
```

## Configuration

### Environment Variables
- `ENV`: Application environment (default: production)
- `PORT`: Server port (default: 8000)
- `HOST`: Server host (default: 0.0.0.0)

### Limits
- Maximum Fibonacci number: 10,000 (configurable)
- Maximum sequence length: 100 (configurable)

## Architecture

### Application Structure
```
fastapi_fibonacci/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── Dockerfile          # Container definition
├── docker-compose.yml  # Multi-container setup
├── .dockerignore       # Docker build exclusions
├── scripts/            # Deployment scripts
│   ├── build.sh
│   ├── deploy.sh
│   ├── run.sh
│   └── stop.sh
└── README.md           # This file
```

### Docker Features
- **Multi-stage build** for optimized image size
- **Non-root user** for enhanced security
- **Health checks** for reliability monitoring
- **Restart policies** for high availability
- **Network isolation** with custom networks

## Performance

The application uses an iterative Fibonacci algorithm with O(n) time complexity and O(1) space complexity, making it suitable for calculating large Fibonacci numbers efficiently.

Benchmark results (approximate):
- Fibonacci(100): ~0.000001 seconds
- Fibonacci(1000): ~0.000010 seconds
- Fibonacci(10000): ~0.001000 seconds

## Production Deployment

### Cloud Platforms
This application can be deployed to any Docker-compatible platform:

- **AWS**: ECS, Fargate, or EC2
- **Google Cloud**: Cloud Run or GKE
- **Azure**: Container Instances or AKS
- **DigitalOcean**: App Platform or Droplets
- **Heroku**: Container Registry

### Kubernetes Deployment
For Kubernetes deployment, use the Docker image with appropriate manifests:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fibonacci-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: fibonacci-api
  template:
    metadata:
      labels:
        app: fibonacci-api
    spec:
      containers:
      - name: fibonacci-api
        image: fibonacci-api:latest
        ports:
        - containerPort: 8000
        livenessProbe:
          httpGet:
            path: /
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
```

## Security

- Non-root container execution
- Input validation and sanitization
- Rate limiting for large calculations
- No sensitive data exposure
- Regular security updates

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source. Feel free to use it for learning and development purposes.

## Support

For issues and questions:
- Open an issue on GitHub
- Check the API documentation at `/docs`
- Review the deployment logs for troubleshooting
