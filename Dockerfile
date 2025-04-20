FROM python:3.12
WORKDIR /app
COPY gym/requirements.txt . 
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "app.py" ]

