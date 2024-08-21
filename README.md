# Digital Event Management and Approval System

Welcome to the Digital Event Management and Approval System. This web application streamlines the process of event management and approval within the SRMIST Faculty of Science and Humanities. It allows students and staff to submit event-related forms, which are then reviewed and approved by the designated authorities.

## Table of Contents
- [Introduction](#introduction)
- [User Guide](#user-guide)
  - [Student and Staff User](#student-and-staff-user)
  - [Authority Module](#authority-module)
- [Developer Guide](#developer-guide)
  - [Technologies Used](#technologies-used)
  - [Database Models](#database-models)
  - [Setup Instructions](#setup-instructions)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Digital Event Management and Approval System is designed to assist in the submission and approval process for events within SRMIST Faculty of Science and Humanities. Students and staff can fill out and submit forms detailing their event requirements, which are then reviewed by authorized personnel who have the ability to approve or reject these submissions.

## User Guide

### Student and Staff User

To submit an event form, follow these steps:
1. Fill out the form with your name, register number/employee ID, phone number, email, subject of the letter, and purpose of the event.
2. Submit the form for approval.

### Authority Module

Authorized personnel can manage event submissions as follows:
1. Log in to the web application with your authority credentials.
2. View all submitted forms.
3. Approve or reject the submissions based on the event's requirements and feasibility.

## Developer Guide

### Technologies Used

- **Backend and Database**: Django and Supabase

### Database Models

The application uses the following database model:

- **Formdetailsmodel**: Stores all individual form data submitted by students and staff.

### Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/htarab-b/srm-fsh-iqac-management.git
    cd srm-fsh-iqac-management
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

4. **Access the application**:
    Open your browser and navigate to `http://localhost:8000/`.

## Contributing

We welcome contributions to enhance the Digital Event Management and Approval System. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.