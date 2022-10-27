FROM python:3.9

ENV APP /app
ENV PORT 5000

WORKDIR $APP

EXPOSE $PORT

COPY . $APP

RUN pip install -r requirements.txt

CMD [ "python3", "-m", "flask", "run","--host=0.0.0.0" ]

