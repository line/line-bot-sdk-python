FROM python:3.8
ADD . / 

RUN apt-get update \ 
    && apt-get install gcc libgl1 -y \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

CMD ["python", "main.py"]
