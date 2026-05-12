# Baby Tools World

Baby Tools World is a Django-based shop application for baby products and product categories.  
The application provides product listings, product detail pages, category navigation, user authentication, and customer reviews.  
This version adds product tags that can be managed through the Django admin panel and displayed on product detail pages.

## Table of Contents

- [Quickstart](#quickstart)
- [Deployed Application](#deployed-application)
- [Usage](#usage)
- [Testing](#testing)
- [Code Quality](#code-quality)
- [Docker](#docker)
- [Git Workflow](#git-workflow)

## Quickstart

### Prerequisites

Before running the project locally, make sure the following tools are installed:

- Python
- Git
- Docker or another OCI-compliant container engine
- Code editor or IDE

### Local Setup

1. Clone the repository and move into the project directory:

```bash
git clone <repository-url>
cd baby-tools-world-project
```

2. Create a virtual environment:

```bash
python -m venv my-venv
```

3. Activate the virtual environment.

Windows PowerShell:

```powershell
.\my-venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source my-venv/bin/activate
```

4. Install all required dependencies:

```bash
pip install -r requirements.txt
```

5. Set up the local environment configuration.

Windows PowerShell:

```powershell
Copy-Item example.env src\.env
```

macOS / Linux:

```bash
cp example.env src/.env
```

6. Navigate to the Django source directory:

```bash
cd src
```

7. Run database migrations:

```bash
python manage.py migrate
```

8. Load sample data to get started:

```bash
python manage.py seed_db
```

9. Launch the development server:

```bash
python manage.py runserver
```

The application is available at:

```text
http://127.0.0.1:8000
```

## Deployed Application

The application is currently available on the project VM at:

```text
http://46.225.103.211:8080/
```

## Usage

### Admin Panel

A Django superuser can be created with:

```bash
python manage.py createsuperuser
```

The admin panel is available at:

```text
http://127.0.0.1:8000/admin
```

The admin panel can be used to manage:

- Products
- Categories
- Tags
- Customer comments
- User accounts


### Product Tags

Products can be associated with one or more tags through the Django admin panel.

On the product detail page, assigned tags are displayed below the rating summary and above the buy button.

If no tags are assigned to a product, the page displays:

```text
no tags available
```

### Customer Reviews

Registered users and guests can submit product reviews with a star rating and an optional comment.

After a review has been submitted successfully, the rating selection and comment field are cleared.

## Testing

Run the Django test suite from the `src` directory:

```bash
python manage.py test
```

## Code Quality

Run the formatting and linting checks from the project root directory:

```bash
black --check .
isort --check-only .
flake8 .
```

To format the Python code, run:

```bash
black .
isort .
```

## Docker

Build the container image from the project root directory:

```bash
docker build -t baby-tools-world:local .
```

Run the containerized application:

```bash
docker run --rm -it -p 8000:8000 --env-file src/.env baby-tools-world:local
```

The application is available at:

```text
http://127.0.0.1:8000
```

## Git Workflow

Development is done on a dedicated feature branch.

For this implementation, the feature branch is:

```text
add-product-tags
```

Changes are committed locally, pushed to GitHub, and reviewed through a Pull Request.  
The automated pipeline must pass successfully before the review process is completed.
