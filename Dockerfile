FROM python:3.6
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
VOLUME ["/app/Flaskr/demo/private"]
EXPOSE 5000
CMD ["python3 flaskr.py"]
