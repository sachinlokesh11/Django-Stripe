# Django Stripe Webhook Integration

This Django project demonstrates how to integrate Stripe webhook events into a Django application for handling payment-related events.

## Installation

1. Clone this repository to your local machine:
```commandline
git clone <repository_url>
```

2. Install the required dependencies:

```commandline
pip install -r requirements.txt
```


3. Configure Stripe API keys:

- Sign up for a Stripe account if you haven't already.
- Obtain your Stripe API keys from the Stripe Dashboard.
- Set your Stripe API keys in the Django project's settings file (`settings.py`):

  ```python
  STRIPE_PUBLIC_KEY = 'your_public_key'
  STRIPE_SECRET_KEY = 'your_secret_key'
  ```

4. Configure Stripe webhook endpoint:

- Log in to your Stripe account.
- Navigate to the Webhooks section in the Dashboard.
- Add a new webhook endpoint with the URL pointing to your Django application's `/stripe-webhook/` URL.

## Usage
1. Make Migrations:

- Run the following command to create migration files based on the changes you've made to your models:

```commandline
python manage.py makemigrations
```

3. Apply Migrations:

- After creating migration files, apply them to your database using the following command:

```commandline
python manage.py migarte
```

4. Start the Django development server:

```
python manage.py runserver
```


5. Access the Django admin interface to manage `Customer` objects:

- Navigate to `http://localhost:8000/admin/` in your web browser.
- Log in using your superuser credentials.
- Manage `Customer` objects and other models registered with the admin interface.

6. Test the Stripe webhook integration:

- Use the Stripe Dashboard to send test webhook events to your webhook endpoint (`/stripe-webhook/`).
- Verify that your Django application receives and handles the webhook events correctly.

## Webhook Endpoint

The webhook endpoint for receiving Stripe webhook events is located at `/stripe-webhook/`. This endpoint is CSRF-exempt to allow Stripe to send webhook requests directly to your server.

## Credits

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Stripe**: A payment processing platform that allows businesses to accept payments online and provides APIs for developers to integrate payment functionality into their applications.

