FROM python:3.9

# Install from requirements.txt
COPY requirements.txt .
# Upgrade pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
ADD . /app
WORKDIR /app

ENTRYPOINT ["python", "cli.py"]
