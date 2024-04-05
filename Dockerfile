#docker file for the django project


# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app

WORKDIR /app

# Copy the current directory contents into the container at /app

COPY . /app

# Install any needed packages specified in requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container

EXPOSE 8000

# Define environment variable

ENV NAME World

# Run app.py when the container launches

CMD ["python", "manage.py", "runserver" ]

#docker build -t mydjangoapp .
#docker run -p 8000:8000 mydjangoapp
#docker run -p 8000:8000 -v $(pwd):/app mydjangoapp
#docker run -p 8000:8000 -v $(pwd):/app mydjangoapp python manage.py runserver

