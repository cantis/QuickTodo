FROM python:3.10.7
WORKDIR /web
ADD . /web
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uwsgi", "app.ini"]

