FROM python:3.9

WORKDIR /tuketici

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "tuketici.py" ]
