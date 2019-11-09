# Agriculture Yield Forecasting

A web application to predict what kind of crop is better to actually grow that crop to gain more profit based on the previous data

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Python 3
* django 1.9
* MySQL
* Sklearn
* numpy
* pandas
* matplotlib

### Installing

A step by step series of examples that tell you have to get a development env running

Install Django

```
pip install django==1.9
```

Install Sklearn

```
pip install sklearn
```

Install Numpy

```
pip install numpy
```

Install Pandas

```
pip install pandas
```

Install Matplotlib

```
pip install matplotlib
```

Install pymysql (Python-MySQL connector)

```
pip install pymysql
```

## Deployment

To run main server

```
cd /path/to/project
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Accessing Webpages

All the webpages can be accessed by adding the following url to base url http://localhost:8000/

*Home -> http://localhost:8000/ <br />
*Contact -> http://localhost:8000/contact/ <br />
*prediction -> http://localhost:8000/predict/ <br />
*query -> http://localhost:8000/query/

### Linear Regression

```
/kernel_regression/<reg_type>/<river>/<crop>
```

### SVM

```
/svm/<reg_type>/<river>/<crop>
```

### KNN

```
/kernel_regression/<river>/<crop>
```
