# sneaker-tracker

## Branching Structure

This project uses a specific branching structure to streamline development and maintain code quality. Please follow these guidelines when working on the project.

### Branches

1. **`main`**

   - **Purpose**: The `main` branch contains the stable, production-ready code. This branch should always reflect the latest stable version of the project.
   - **Usage**: Only merge into `main` when code is thoroughly tested and ready for production.

2. **`develop`**
   - **Purpose**: The `develop` branch serves as the integration branch where all features and fixes are merged before being incorporated into `main`.
   - **Usage**: Regularly merge feature branches into `develop` for testing and integration.

### Branch Types

1. **Feature Branches**

   - **Naming Convention**: `feature/short-description`
   - **Purpose**: To develop new features or significant changes.
   - **Example**: `feature/user-authentication`
   - **Workflow**:
     1. Create a new branch from `develop`:
        ```bash
        git checkout develop
        git pull origin develop
        git checkout -b feature/short-description
        ```
     2. Work on the feature and commit your changes.
     3. Push the branch to the remote repository:
        ```bash
        git push origin feature/short-description
        ```
     4. Open a pull request to merge the feature branch into `develop`.

2. **Bugfix Branches**

   - **Naming Convention**: `bugfix/short-description`
   - **Purpose**: To address bugs or issues.
   - **Example**: `bugfix/fix-login-error`
   - **Workflow**:
     1. Create a new branch from `develop` or `main`:
        ```bash
        git checkout develop
        git pull origin develop
        git checkout -b bugfix/short-description
        ```
     2. Work on the fix and commit your changes.
     3. Push the branch to the remote repository:
        ```bash
        git push origin bugfix/short-description
        ```
     4. Open a pull request to merge the bugfix branch into `develop`.

3. **Hotfix Branches**
   - **Naming Convention**: `hotfix/short-description`
   - **Purpose**: To apply urgent fixes directly to `main` (e.g., critical bugs or security issues).
   - **Example**: `hotfix/patch-vulnerable-dependency`
   - **Workflow**:
     1. Create a new branch from `main`:
        ```bash
        git checkout main
        git pull origin main
        git checkout -b hotfix/short-description
        ```
     2. Work on the fix and commit your changes.
     3. Push the branch to the remote repository:
        ```bash
        git push origin hotfix/short-description
        ```
     4. Open a pull request to merge the hotfix branch into `main` and `develop`.

### General Workflow

1. **Start with a New Branch**: Always start your work by creating a new branch for features, bugfixes, or hotfixes.
2. **Commit Changes**: Regularly commit your changes with clear, descriptive messages.
3. **Push Branches**: Push your branches to the remote repository frequently.
4. **Create Pull Requests**: Open pull requests to merge changes into `develop` (or `main` for hotfixes).
5. **Review and Merge**: Review pull requests, ensure all tests pass, and merge into the appropriate branch.

### Summary

- **`main`**: Stable, production-ready code.
- **`develop`**: Integration branch for features and fixes.
- **Feature Branches**: `feature/short-description`.
- **Bugfix Branches**: `bugfix/short-description`.
- **Hotfix Branches**: `hotfix/short-description`.

Please follow these guidelines to maintain consistency and ensure smooth collaboration.

---

Feel free to modify or expand this template according to your project's specific needs and practices.
