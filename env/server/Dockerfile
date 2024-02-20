FROM python:3.10-alpine

# Set the working directory
WORKDIR /app
# Copy your Python script (which listens for UDP packets) into the container
COPY server.py .

# Install any necessary dependencies
# RUN pip install pydantic
EXPOSE 8000/udp

# Specify the command to run when the container starts
CMD ["python3", "server.py"]
