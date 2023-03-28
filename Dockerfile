FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip 
RUN pip install pipenv
RUN pip install --no-cache-dir -r requirements.txt

COPY . . 
# Expose port 8000 on the container
EXPOSE 8000
CMD [ "python", "manage.py", "runserver"]
#--------------------------------------

