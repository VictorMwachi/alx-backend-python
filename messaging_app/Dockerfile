FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
EXPOSE 8000
# This Dockerfile sets up a Python environment, copies the application code, installs dependencies, and runs the application.
# It also exposes port 8000 for the application to be accessible.     