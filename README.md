# 🌌 Space Explorer

**Space Explorer** is a Flask-based AI-powered search engine for space-related content. It integrates NASA's public APIs and Gemini AI to deliver stunning space imagery, rover photos, asteroid data, and intelligent summaries in response to user queries.

---

## 🚀 Features

* 🔍 Ask space-related questions via Gemini API
* 📷 View NASA's Astronomy Picture of the Day (APOD)
* 🚘 Explore Mars Rover Photos
* ☄️ Fetch Near-Earth Object (asteroid) data
* 🎨 Clean and responsive interface using Flask + HTML
* 🤖 AI-based summary generation with Gemini (optional)
* 🧠 Modular backend with route-based architecture

---

## 📁 Folder Structure

```
space-explorer/
│
├── app/
│   ├── __init__.py       # Flask app factory
│   ├── routes.py         # All route definitions
│   ├── models.py         # For future database logic (optional)
│   ├── static/           # CSS, JS, images
│   └── templates/        # HTML templates
│       └── home.html
│
├── run.py                # App entry point
├── .gitignore
├── LICENSE
├── requirements.txt
└── venv/                 # Virtual environment (ignored by Git)
```

---

## ⚙️ Getting Started (Local Setup)

1. Clone the repository:

```bash
git clone https://github.com/pxD1311/space-explorer.git
cd space-explorer
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the environment (Windows):

```bash
venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the Flask app:

```bash
python run.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to view the app.

---

## 📦 Requirements

All Python packages are listed in `requirements.txt`.

To update it:

```bash
pip freeze > requirements.txt
```

---

## 🧪 APIs Used

* [NASA APOD](https://api.nasa.gov/)
* [NASA Mars Rover Photos](https://api.nasa.gov/)
* [NASA NEO (Asteroids)](https://api.nasa.gov/)
* [Gemini API](https://ai.google.dev/) *(optional)*

---

## 📝 License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

---

## 🤝 Contributing

To join the project:

1. Fork the repository
2. Clone your fork
3. Create a new branch: `git checkout -b feature-name`
4. Push your changes and open a pull request

Drop your GitHub username to be added as a collaborator!

---

## ✨ Team Goals

> Build a beautiful, fast, and intelligent way to explore the universe with just one search.
