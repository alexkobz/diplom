FROM python:3.12
LABEL authors="alexkobz"

WORKDIR /diplom

COPY requirements.txt .

RUN python -m pip install -U pip
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./__main__.py" ]
