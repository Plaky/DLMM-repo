# Use Python 3.12 as base image
FROM python:3.12-slim-bullseye

# Install system-level dependencies
RUN apt-get update && apt-get install -y git

# Install build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Copy Python dependencies and install them
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY . .

# Set default shell to bash
CMD ["bash"]
