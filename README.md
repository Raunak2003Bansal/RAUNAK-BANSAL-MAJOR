Markdown
# Serverless FastAPI HTML Resume & CI/CD Pipeline

A modern, high-performance serverless web application that hosts a professional HTML-based resume. Built with Python using FastAPI, optimized using the `uv` package manager, and deployed automatically to Vercel via a custom GitHub Actions CI/CD pipeline.

---

## 🚀 Live Demo
You can view the live production site here:
👉 **[raunak-bansal-resume.vercel.app](https://raunak-bansal-resume.vercel.app)**

### Live Endpoints:
* **Root (`/`):** Serves the main interactive resume homepage.
* **Resume Routing (`/resume`):** A dedicated explicit endpoint rendering the resume layout for differentiation.

---

## 🛠️ Tech Stack & Tooling

* **Backend Framework:** FastAPI (Python 3.12+)
* **Hosting Platform:** Vercel (Serverless Functions)
* **Package Management:** `uv` by Astral (ultra-fast dependency management)
* **CI/CD Automation:** GitHub Actions
* **Configuration Syntax:** ASGI / Uvicorn handling routing structures

---

## 📂 Project Structure

```text
MAJOR_PROJECT/
├── .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions automated CI/CD engine
├── api/
│   └── index.py            # Main FastAPI server logic & route endpoints
├── basic_html_resume.html  # Production-ready resume frontend template
├── pyproject.toml          # Modern python package definitions
├── requirements.txt        # Generated package lock configurations
├── uv.lock                 # Strict cryptographic dependency tree lockfile
└── vercel.json             # Vercel serverless routing & builder instructions
⚡ Automated CI/CD Lifecycle
This repository utilizes a smart branch-based deployment architecture via GitHub Actions:

Production Pipeline (main branch): Pushing code directly to or merging into main fires an automated script that configures a clean Linux runner, provisions the uv environment, compiles production artifacts, and pushes updates directly live to the primary domain.

Preview Pipeline (test branch): Pushing to the test branch executes an identical build matrix but routes the output to an isolated, temporary Vercel preview deployment URL for safe layout testing.