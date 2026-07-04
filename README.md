# Backend Chatbot API

## Overview
This project is a FastAPI backend that integrates with the CallMissed API.

## Features
- Chat API using kimi-k2.7-code
- Image Generation API using flux-2-klein-9b
- Modular FastAPI project structure
- Environment variable support
- Error handling

## Tech Stack
- Python 3.12
- FastAPI
- OpenAI SDK
- CallMissed API

## Setup

1. Clone the repository
2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file

```env
CALLMISSED_API_KEY=your_api_key_here
```

4. Run

```bash
uvicorn main:app --reload
```

## API Endpoints

- GET /
- POST /chat
- POST /image

## Models Used

- kimi-k2.7-code (Chat)
- flux-2-klein-9b (Image Generation)

## AI Usage

I used ChatGPT to understand FastAPI structure, debug errors, and improve the project organization. I implemented, tested, and integrated the project step by step.
