FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "tamil_chatbot.py", "--server.port=8501", "--server.enableCORS=false"]
