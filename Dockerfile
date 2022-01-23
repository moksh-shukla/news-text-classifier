# Only builds and runs the Flask backend
# Ensure that frontend static bundle is already in `server/static` directory

FROM python:3.9.7-buster
EXPOSE 5000
WORKDIR /app
ADD . .
RUN pip3 install -r requirements.txt
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]