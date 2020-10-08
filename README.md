# A Simple Bidding App

This app uses Django for the backend and React for the frontend.

## Quickstart

While at the root of the repository:

- Use pipenv to install backend dependencies: `pipenv install`
- Install front end deependencies using npm: `npm install`
- Run the server with the command: `pipenv run python manage.py runserver`

## The Schema (sketch)

Models:

- User
  - email
  - is_admin
- UserProfile
  - user
  - first_name
  - last_name
  - total_credit
  - committed_credit
  - created_at
  - updated_at
- Product
  - user
  - name
  - description
  - image
  - min_price
  - max_price
  - expiry_date
  - created_at
  - updated_at
- Bid
  - user
  - product
  - amount
  - is_accepted
  - created_at
  - updated_at
