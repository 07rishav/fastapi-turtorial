# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependencies file and install
COPY requirement.txt .

RUN pip install --no-cache-dir -r requirement.txt

# Copy the rest of the project
COPY . .

# Expose port 8000
EXPOSE 8000

# Run FastAPI app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
