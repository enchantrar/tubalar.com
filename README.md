# My Flask Learning Project

A beginner Flask app built module by module.

## Setup

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then visit http://127.0.0.1:5000

## Project Structure

```
flask_app/
├── app.py                  # Routes & app logic
├── requirements.txt
├── templates/
│   ├── base.html           # Shared layout (nav, footer, flash messages)
│   ├── home.html
│   ├── about.html
│   └── contact.html
└── static/
    └── css/
        └── style.css
```

## Concepts Covered

| Concept | Where |
|---|---|
| `@app.route` | `app.py` |
| GET vs POST | `contact` route |
| `render_template` | all routes |
| Template inheritance | `base.html` + child templates |
| `url_for` | nav links in templates |
| Flash messages | contact form |
| Static files | `style.css` |
