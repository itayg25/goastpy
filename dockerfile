# Use Ubuntu as the base image
FROM golang



# Update package lists and install dependencies
RUN apt-get update && \
    apt-get install -y \
    make \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy your Python requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy your Golang and Python source files
COPY . .

CMD ["bash"]
