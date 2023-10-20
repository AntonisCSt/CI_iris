# Continuous integration


mkdir -p .github/workflows/
-p flag with mkdir to create the parent directories if they don't exist.

## Creating our first workflow

```yaml
name: learn-github-actions
run-name: ${{ github.actor }} is learning GitHub Actions
on: [push]
jobs:
  saying-hello:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Hello World
        run: echo "Hello Github World"

      - run: echo "Hello World without run-name"

      - run: ls
```



## Adding linting and formatting tests: Starting our Continuous integration

Let's make a workflow for that.

```yaml
name: linting-formatting
run-name: ${{ github.actor }} is learning GitHub Actions
on: [push]
jobs:
  check-bats-version:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v1
        with:
          python-version: 3.10

      - name: Install Python dependencies
        run: pip install black==23.7.0 pylint==2.17.5

      - run: black ./
      - run: find . -type f -name "*.py" | xargs pylint --recursive=yes .


```

## Marketplace

market-place has some very useful workflows that can be used for many cases: For example check this script that reads a file:
https://github.com/marketplace/actions/read-file

we are going to use one for linting and black: https://github.com/marketplace/actions/lint-action

let's edit our previous workflow
```yaml
name: linting-formatting
run-name: ${{ github.actor }} is learning GitHub Actions
on: [push]
jobs:
  check-bats-version:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v1
        with:
          python-version: 3.10.13

      - name: Install Python dependencies
        run: pip install -r requirements.txt

      - name: Run linters
        uses: wearerequired/lint-action@v2
        with:
          black: true
          flake8: true

```

if you get an error:  `Received status code 403. Resource not accessible by integration https://docs.github.com/rest/checks/runs#create-a-check-run
Warning: Some check runs could not be created.`

it is related to fact that we are using the `push` event to trigger the workflow while the `pull` is recommended.

Reference: https://docs.github.com/en/code-security/code-scanning/troubleshooting-code-scanning/resource-not-accessible-by-integration

Exercise: 
Write a workflow that uses the makefile to perform the tests.