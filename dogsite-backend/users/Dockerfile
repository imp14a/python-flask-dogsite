FROM python:3.10-alpine

WORKDIR /app
COPY . /app
#RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#ENTRYPOINT [ "python" ]
CMD ["gunicorn","--bind","0.0.0.0:8080", "app:app"]
#CMD ["wsgi.py"]