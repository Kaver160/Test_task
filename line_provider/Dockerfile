FROM python:3.10-slim

WORKDIR /line_provider

COPY requirements.txt .

RUN  pip install --upgrade pip --root-user-action=ignore \
     && pip install --no-cache-dir --upgrade -r requirements.txt --root-user-action=ignore

COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8001"]