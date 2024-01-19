from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = FastAPI(title="Contact" ,version="4.0")

class EmailRequest(BaseModel):
    reciever_mail : str
    title: str
    body: str

@app.post("/send_mail")
async def endpoint_to_send_email(request_data : EmailRequest):
    sender_email = ""
    receiver_email = request_data.reciever_mail
    subject = request_data.title
    body = request_data.body
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = ""
    smtp_password = ""

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    return JSONResponse(content={"status":"Email Sent"})



