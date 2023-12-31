FROM python:3.9.10-alpine3.14
WORKDIR /app
COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 4000
CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000"]