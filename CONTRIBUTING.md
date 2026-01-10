# Contributing to Tgram

First off, thank you for considering contributing to **Tgram**! We appreciate your efforts and time in making this library better. Here are some guidelines to help you contribute effectively.

---

## How Can You Contribute?

### Reporting Issues

If you find a bug or have a feature request, please [open an issue](https://github.com/z44d/tgram/issues). Ensure the following:

- Search existing issues to avoid duplicates.
- Provide a clear and descriptive title.
- Include as much relevant information as possible, such as:
  - Steps to reproduce the issue.
  - Expected vs actual behavior.
  - Error messages, logs, or screenshots (if applicable).

### Suggesting Features

Have an idea to enhance Tgram? We'd love to hear it! Create an issue with the `enhancement` label and describe:

- The problem the feature solves.
- How it fits into the scope of Tgram.
- Possible implementation ideas (if any).

### Code Contributions

Want to add new features, fix bugs, or improve the documentation? Follow these steps:

1. **Fork the repository**\
   Click the "Fork" button on the top right of the repo to create your own copy.

2. **Clone your fork**

   ```bash
   git clone https://github.com/<your-username>/tgram.git
   cd tgram
   ```

3. **Create a new branch**\
   Use a meaningful branch name that reflects your changes:

   ```bash
   git checkout -b fix-bug-123
   ```

4. **Install dependencies**\
   Ensure your development environment is set up by installing dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. **Write code and tests**

   - Follow the existing coding style.
   - Add or update tests for your changes.
   - Run tests locally before committing:
     ```bash
     pytest
     ```

6. **Lint your code**
   Use [Ruff](https://github.com/charliermarsh/ruff) to ensure your code follows style guidelines:
   ```bash
   ruff check .
   ```
   Fix any issues Ruff identifies automatically with:
   ```bash
   ruff check . --fix
   ```

7. **Commit your changes**\
   Use clear and descriptive commit messages:

   ```bash
   git commit -m "Fix issue #123: Description of fix"
   ```

8. **Push your branch**

   ```bash
   git push origin fix-bug-123
   ```

9. **Open a pull request**\
   Go to the repository on GitHub and click the "New Pull Request" button. Provide the following details:

   - A clear and concise title.
   - A detailed description of your changes and why they are necessary.

---

## Code Style Guidelines

- Follow the [PEP 8](https://peps.python.org/pep-0008/) coding standards.
- Use type hints wherever applicable.
- Write docstrings for functions and classes.
- Ensure your code passes [Ruff](https://github.com/charliermarsh/ruff) checks.

---

## Reviewing Pull Requests

Pull requests are reviewed to maintain the quality and consistency of the library. During the review process:

- Be patient, as maintainers may need time to review.
- Address feedback promptly and update your pull request as needed.
- Ensure your branch is up-to-date with the `main` branch.

---

## Community Guidelines

- Be respectful and considerate of others.
- Avoid spamming or submitting low-quality contributions.
- Provide constructive feedback during discussions.

---

Thank you for contributing to **Tgram**! Together, we can build something amazing. 🙌

