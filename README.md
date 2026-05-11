# Baby Tools World

Baby Tools World is a Django-powered e-commerce platform specializing in baby products and accessories.  
The application offers intuitive product browsing, detailed product pages, category navigation, user authentication, and customer reviews.  
This version includes a flexible tagging system for products, fully manageable through the Django admin interface.

## Quickstart

### What You'll Need

Before setting up the project locally, please ensure you have:

- Python installed
- Git
- Docker (or any OCI-compliant container engine)
- Your preferred code editor or IDE

### Setting Up Locally

First, clone the repository and move into the project directory:

```bash
git clone <repository-url>
cd baby-tools-world-project
```

Create a virtual environment:

```bash
python -m venv my-venv
```

Activate the virtual environment:

**Windows PowerShell:**

```bash
.\my-venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
source my-venv/bin/activate
```

Install all required dependencies:

```bash
pip install -r requirements.txt
```

Set up your local environment configuration:

**Windows PowerShell:**

```bash
Copy-Item example.env src\.env
```

**macOS/Linux:**
```bash
cp example.env src/.env
```

Navigate to the Django source directory:

```bash
cd src
```

Run database migrations:

```bash
python manage.py migrate
```

Load sample data to get started:
```bash
python manage.py seed_db
```

Launch the development server:

```bash
python manage.py runserver
```

You can now access the application at: `http://127.0.0.1:8000`

## Usage

### Admin Panel

To create a Django superuser account, run:

```bash
python manage.py createsuperuser
```

Access the admin panel at: `http://127.0.0.1:8000/admin`

Through the admin panel, you can manage:

- Products
- Categories
- Tags
- Customer comments
- User accounts

### Product Tags

Products can be associated with multiple tags directly from the Django admin panel.

On each product detail page, assigned tags appear below the rating summary and above the purchase button.

If no tags are assigned to a product, the page will display: `no tags available`

### Customer Reviews

Both registered users and guests can submit product reviews, including a star rating and an optional written comment.

Once a review is successfully submitted, the rating selection and comment field automatically reset for convenience.

## Testing

To run the complete Django test suite, navigate to the `src` directory and execute:

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

