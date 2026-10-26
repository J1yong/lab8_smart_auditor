FROM python:3.12-slim

WORKDIR /app

COPY inf1103_labs_smart_auditor.py .
COPY inventory.json .

CMD ["python", "inf1103_labs_smart_auditor.py"]