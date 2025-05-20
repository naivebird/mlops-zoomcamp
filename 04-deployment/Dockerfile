FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim
WORKDIR /app
RUN mkdir -p output/yellow
COPY ["starter.py", "./"]
COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pip install pipenv
RUN pipenv install --system

ENTRYPOINT ["python", "./starter.py"]