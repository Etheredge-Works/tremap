FROM python:3.8
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
RUN pip install streamlit
COPY . /app
WORKDIR /app
CMD streamlit run app.py