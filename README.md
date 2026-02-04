🚀 Semantic Search using Endee Vector Database

📌 Project Overview

This project demonstrates a Semantic Search system built using Endee, a high-performance open-source vector database.
Instead of matching keywords, the system understands the meaning of text using embeddings and returns the most relevant results.

The project is designed as a simple, practical AI application suitable for internship evaluation, showing:

How embeddings work

How vector databases like Endee are used

How semantic search / RAG-style systems are built

How to integrate AI models with a backend API

🧠 Problem Statement

Traditional search systems rely on keyword matching, which fails when:

The user uses different words with the same meaning

The query is semantically similar but not textually similar

This project solves that by:

Converting text into vector embeddings

Storing/searching them using Endee vector database

Returning results based on semantic similarity, not exact words

🏗️ System Design / Architecture

Components:

FastAPI → Backend API server

Sentence Transformers → Converts text into embeddings (vectors)

Endee → Stores and searches vectors efficiently

Python Requests → Communicates with Endee API

🧩 How Endee Is Used

Endee acts as the vector database in this project:

Document embeddings are stored (upserted) into Endee

User queries are converted into embeddings

Endee performs similarity search on vectors

Most relevant documents are returned

This demonstrates a real-world use case of Endee for:

Semantic Search

RAG systems

AI-powered search engines

Recommendation systems

⚙️ Tech Stack

Python

FastAPI

Sentence-Transformers (all-MiniLM-L6-v2)

Endee Vector Database (Docker)

Requests

Uvicorn

📂 Project Structure
semantic-search-endee/

<img width="640" height="395" alt="Screenshot 2026-02-05 001535" src="https://github.com/user-attachments/assets/4b793dfe-05da-4b85-847d-3118cea56cc5" />


🐳 Step 1: Run Endee using Docker
Install Docker first:


Run Endee server:
docker run -d -p 8080:8080 -v endee-data:/data --name endee-server endeeio/endee-server:latest


Check if it’s running:

docker ps

🧪 Step 2: Setup Backend

Go to backend folder:

cd backend


Install dependencies:

pip install -r requirements.txt


Run the server:

uvicorn app.main:app --reload


You should see:

{"message": "Semantic Search API is running"}

🔍 Step 3: Test Semantic Search

Open in browser:

http://127.0.0.1:8000/search?q=ai



Try:

http://127.0.0.1:8000/search?q=machine
 learning

http://127.0.0.1:8000/search?q=vector
 database

http://127.0.0.1:8000/search?q=semantic
 search

You will get meaning-based results, not just keyword matches.

🎯 Use Cases

Semantic Search Engines

RAG (Retrieval Augmented Generation) Systems

AI Assistants

Document Search

Recommendation Systems
