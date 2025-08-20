FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

# Create a non-root user for security
RUN useradd --create-home --shell /bin/bash calculator
USER calculator

# Expose port (if needed for future web interface)
EXPOSE 8000

# Default command
CMD ["python", "calculator.py"]
