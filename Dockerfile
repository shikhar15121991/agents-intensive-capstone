
# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port for Streamlit or Flask UI
EXPOSE 8501

# Default command (Streamlit app or orchestrator script)
CMD ["streamlit", "run", "src/app.py"]
