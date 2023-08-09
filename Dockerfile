FROM python:3.10

WORKDIR /code
COPY poetry.lock pyproject.toml /code/
RUN pip install poetry
RUN poetry install 
EXPOSE 80
# 
COPY . /code/

ENTRYPOINT ["poetry", "run"]
# 
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]