
# Multiple-choice

## **Task**

---

Create a multiple-choice game web app where the user guesses the correct author for a given quote. 

**Back-end**

Develop a Django application that retrieves [quotes](https://scalablepath.com/api/test/test-quotes) and their corresponding [authors](https://www.scalablepath.com/api/test/test-authors) from an external source. Store this data in a database and utilize it to generate questions for a multiple-choice game.

1. Implement a **`/quotes`** endpoint that returns a random quote from the database along with four potential authors in JSON format.
2. The initial call to the endpoint should trigger the seeding of the database. Determine the necessity of this action by checking if the database table is empty.

**Front-end**
Develop a JavaScript application that interacts with your back-end endpoint to present a Multiple-Choice Game.

1. Display a quote and four buttons, each labeled with a potential author's name, roughly following the provided wireframe layout.
2. When a selection is made, the user interface should indicate whether the user's guess was correct. Incorrect answers will remove that option, allowing the user another attempt. Correct answers will proceed to the next quote.

**Specific Requirements:**
1. Each quiz must present four unique author choices without any repetition.
2. The correct author must always be included among the options, with their position randomized for each new question.

## Installation

This project uses Django Framework, Django Rest Framework, and Alpine.js.

```bash
  git clone git@github.com:jcroot/quotes.git
  cd quotes
  python -m venv venv
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver
```

### Seed the database

```bash
  python manage.py seed_authors
  python manage.py seed_quotes
```

### API Endpoints
Get Random quote with authors
```bash
    /api/quotes
```