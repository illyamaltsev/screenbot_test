FROM python:3.7

# install wkhtmltopdf
RUN apt-get update
RUN apt-get install -y wkhtmltopdf

#RUN apk add chromium chromium-chromedriver

# upgrade pip
RUN pip install --upgrade pip

# install pakages
RUN pip install imgkit telebot pytelegrambotapi python-dotenv

ADD . /

CMD [ "python", "./main.py" ]
