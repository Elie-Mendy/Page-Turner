FROM python:3.10

WORKDIR /app

# libgdal-dev est nécessaire pour installer GDAL 
RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/* &&\
    # project dependencies 
    pip install --upgrade pip && \
    pip install django &&\
    pip install djangorestframework &&\
    pip install python-dotenv &&\
    pip install django-cors-headers &&\
    pip install psycopg2-binary &&\
    pip install djangorestframework-simplejwt &&\
    pip install numpy &&\
    pip install tensorflow &&\
    pip install pandas &&\
    pip install scikit-learn &&\
    pip install nltk &&\
    pip install matplotlib &&\
    pip install ipython

COPY . .

EXPOSE 8000

# Démarrez votre application Django
CMD ["python3", "page-turner/manage.py", "runserver", "0.0.0.0:8000"]