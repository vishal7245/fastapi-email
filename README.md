# FastAPI Email Sender Documentation

## Introduction

This documentation provides information about a FastAPI application that serves as an email sender. The application exposes an HTTP endpoint (`/send_mail`) that accepts POST requests with JSON payloads containing email details such as the receiver's email address, email subject, and email body. The application then sends the email using the provided information.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [API Endpoint](#api-endpoint)
4. [Request Format](#request-format)
5. [Response Format](#response-format)
6. [Configuration](#configuration)
7. [Security Considerations](#security-considerations)
8. [Error Handling](#error-handling)
9. [Examples](#examples)
10. [Contributing](#contributing)
11. [License](#license)

## Installation

Ensure you have Python installed on your system. You can install the required dependencies using the following command:

```bash
pip install fastapi uvicorn
```

## Usage

To run the FastAPI application, use the following command:

```bash
uvicorn your_file_name:app --reload
```

Replace `your_file_name` with the name of the file containing the provided code.

## API Endpoint

### `POST /send_mail`

This endpoint is used to send emails.

## Request Format

The request payload should be a JSON object with the following structure:

```json
{
  "reciever_mail": "recipient@example.com",
  "title": "Email Subject",
  "body": "Email Body Content"
}
```

- `reciever_mail` (string): The email address of the recipient.
- `title` (string): The subject of the email.
- `body` (string): The body content of the email.

## Response Format

The response will be a JSON object with the following structure:

```json
{
  "status": "Email Sent"
}
```

## Configuration

Before running the application, make sure to configure the following parameters in the code:

- `sender_email`: The email address used as the sender.
- `smtp_username`: The username for the SMTP server.
- `smtp_password`: The password for the SMTP server.

## Security Considerations

- **Sensitive Information**: Do not expose sensitive information such as SMTP credentials in the code. Use environment variables or a configuration file to manage such sensitive data.

## Error Handling

The application currently provides minimal error handling. Ensure proper error handling mechanisms are implemented in a production environment.

## Examples

### Example Request

```bash
curl -X POST "http://localhost:8000/send_mail" -H "Content-Type: application/json" -d '{"reciever_mail": "recipient@example.com", "title": "Email Subject", "body": "Email Body Content"}'
```

### Example Response

```json
{
  "status": "Email Sent"
}
```

## Contributing

Feel free to contribute to the project. You can submit issues or pull requests on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
