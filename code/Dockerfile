FROM python:3.9-buster

WORKDIR /app
COPY ./code/requirements.txt ./requirements
RUN pip install -r code/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    rm requirements.txt
COPY . .

CMD [ "python", "-u", "/app/main.py" ]
