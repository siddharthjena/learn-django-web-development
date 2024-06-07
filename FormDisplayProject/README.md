# FormDisplay Project (A Django Form Handling Project)

Welcome to the FormDisplay project! This project focuses on demonstrating how to create a form in Django using `forms.py`, capture the form data in views functions (server-side), and display it on a webpage (frontend) without storing the data in a database. In the future, we plan to enhance the project by adding form validation using Django's inbuilt form validation mechanisms.

## Project Overview

This project aims to help students learn how to:
- Define forms in Django using `forms.py`.
- Capture form data in views functions without using models.
- Display form data in HTML templates using Jinja templating.
- Set up URL routing to connect forms and views.

## Project Flow

1. **URL Routing:**
   - When a user visits a URL (e.g., `/form/`), Django's URL dispatcher (`urls.py`) maps the URL to the corresponding view function.

2. **Form Creation:**
   - The form is defined in `forms.py` using Django's form classes.
   - Fields like text inputs, checkboxes, radio buttons, etc., can be added to the form.

3. **Form Submission and Processing:**
   - The view function associated with the form URL processes the form submission.
   - It captures the form data, and prepares it for display.

4. **Rendering Template:**
   - After processing, the view passes the form data to an HTML template.
   - The HTML template uses Jinja templating to dynamically render the form data in the desired format.

5. **Displaying Result:**
   - The rendered HTML page, containing the form data, is sent back as the HTTP response.
   - Users can see the submitted form data on their web browser.

## Future Enhancements

- **Form Validation**:
  Implement form validation using Django's inbuilt form validation mechanisms. This will include validating required fields, checking for valid input formats, and displaying appropriate error messages.

Stay tuned for these exciting enhancements!

For any questions or feedback, feel free to contact the project owner.

Happy coding! 🚀

