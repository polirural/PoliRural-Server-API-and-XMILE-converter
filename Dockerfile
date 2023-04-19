FROM python:3.8

COPY . .

RUN python -m pip install -r requirements.txt

RUN python -m pip install ./pysd_wheel_dist/pysd-2.0.0.dev0-py3-none-any.whl

CMD ["python", "./app.py"] 
