FROM python:3

WORKDIR /app/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY qa327 qa327
CMD python -m qa327