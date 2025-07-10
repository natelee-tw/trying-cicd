# Streamlit CI/CD Demo

A simple Streamlit application with automated CI/CD pipeline using GitHub Actions.

## Features

- Basic Streamlit UI with interactive button
- Automated linting with flake8
- Unit tests with pytest
- GitHub Actions CI/CD pipeline
- Automatic deployment to Streamlit Cloud

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app locally:
   ```bash
   streamlit run app.py
   ```

3. Run tests:
   ```bash
   pytest test_app.py
   ```

4. Run linting:
   ```bash
   flake8 app.py test_app.py
   ```

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) automatically:
- Installs dependencies
- Runs linting with flake8
- Executes unit tests
- Deploys to Streamlit Cloud (on main branch)

## Streamlit Cloud Deployment

To deploy to Streamlit Cloud:

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set the main file path to `streamlit_app.py`
5. Deploy!

The app will automatically redeploy when you push changes to the main branch.