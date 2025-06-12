# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy server files
COPY server/server.py ./
COPY rfcontrol_pb2.py ./
COPY rfcontrol_pb2_grpc.py ./
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose gRPC port
EXPOSE 50051

# Run the server
CMD ["python", "server.py"]
