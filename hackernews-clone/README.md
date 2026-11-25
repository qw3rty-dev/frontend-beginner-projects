# Hacker News Clone

A Hacker News clone built using Python, FastAPI, BeautifulSoup, Redis, HTML, CSS and JavaScript.

The application scrapes stories directly from Hacker News, exposes them through a REST API, caches scraped results using Redis, and displays them through a custom frontend.

---

## Features

- Scrapes Hacker News Stories using BeautifulSoup.
- REST API built using FastAPI.
- Redis caching with a 5-minute TTL.
- Async HTTP requests using HTTPX.
- Dynamic frontend rendering using vanilla JavaScript.
- Responsive layout using CSS Flexbox.
---

## Tech Stack

| Component | Technology |
|-----------|-------------|
| Backend | Python, FastAPI |
| Scraping | BeautifulSoup, HTTPX |
| Caching | Redis |
| Frontend | HTML, CSS, JavaScript |

---

## Project Structure

```text
hackernews-clone/
│
├── backend/
│   └── src/
│        ├── scraper/
│        │   └──scraper.py
│        ├── cache_service.py
│        ├── main.py
│        ├── routes.py
│        ├── service.py
│        ├── .env
│        └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── .gitignore
└── README.md
```

---

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/qw3rty-dev/frontend-beginner-projects.git
cd frontend-beginner-projects/hackernews-clone
```

### 2. Set up the backend:

Create a virtual environment:
```bash
cd backend

python -m venv .venv

```
Activate it.

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure Redis

Create a `.env` file:

Set up your Redis:
```env
REDIS_URL = your_redis_url
```

### 4. Start the FastAPI server:

From the `backend` directory

```bash
uvicorn src.main:app --reload
```

The API will be available at: 

`http://localhost:8000`

Interactive API documentation:

`http://localhost:8000/docs`


### 5. Run the frontend

Open the frontend directory using VS code Live Server.

The frontend can then communicate with the FastAPI backend.

---

## Caching

The application uses Redis to cache scraped stories.
- Cache keys follow the format `stories:{page}.`
- Cached results expire after 300 seconds.
- Cache misses trigger a fresh scrape.
- Redis failures like connection timeout are considered and handled.


## Future Improvements

- Automated backend tests.
- Frontend pagination.
- Better scraper resilience.
- Improved frontend interactions.

---

## Disclaimer

This project is built for educational purposes only.

---
