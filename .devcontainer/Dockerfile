# Use Python 3.12 as base image
FROM python:3.12-slim-bullseye

# Install system-level dependencies
RUN apt-get update && apt-get install -y git

# Set working directory
WORKDIR /workspace

# Copy Python dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY . .

# Set default shell to bash
CMD ["bash"]
