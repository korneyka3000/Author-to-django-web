FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /proj
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "grpcrunserver", "--dev"]