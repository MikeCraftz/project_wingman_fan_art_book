# De Re Militari - Project Wingman Fan Site

A static fan site for the "De Re Militari" art book project, designed with an in-universe defense contractor aesthetic ("United Service Institute").

## Overview

This project is a Flask application that generates a static website using `Frozen-Flask`. It is designed to be hosted on GitHub Pages.

### Features
-   **Immersive Design**: Styled like a modern military analysis journal (inspired by Anduril).
-   **Book Viewer**: Dedicated high-resolution viewer for book pages.
-   **Responsive**: Fully responsive layout for desktop and mobile.
-   **Automated Deployment**: GitHub Actions workflow to build and deploy to `gh-pages`.

## Development Setup

### Prerequisites
-   Python 3.11 or higher
-   `pip` (Python package manager)

### Installation

1.  **Clone the repository**:
    ```bash
    git clone <your-repo-url>
    cd project_wingman_site
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running Locally

To run the site in development mode (with hot reloading):

```bash
python3 app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Building for Production

This site is static, meaning it doesn't need a backend server to run in production. You "freeze" the Flask app into HTML/CSS/JS files.

1.  **Run the freeze script**:
    ```bash
    python3 freeze.py
    ```

2.  **Check the output**:
    The generated static site will be in the `build/` directory.

3.  **Preview the build**:
    You can serve the `build` directory locally to verify everything works:
    ```bash
    cd build
    python3 -m http.server 8000
    ```
    Open `http://localhost:8000`.

## Deployment

The project is configured for extensive automation via **GitHub Actions**.

-   **Workflow File**: `.github/workflows/deploy.yml`
-   **Trigger**: Pushes to the `main` branch.
-   **Process**:
    1.  Checks out code.
    2.  Installs Python and dependencies.
    3.  Runs `freeze.py`.
    4.  Deploys the `build/` folder to the `gh-pages` branch.

## Project Structure

-   `app.py`: Main Flask application and route definitions.
-   `freeze.py`: Configuration for generating the static site.
-   `templates/`: HTML templates (Jinja2).
-   `static/`: CSS, JavaScript, and Images.
    -   `static/img/`: Book pages and assets.
-   `pages/`: Raw asset directory (source images).
