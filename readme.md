# Continuous integration

 mkdir -p .github/workflows/
-p flag with mkdir to create the parent directories if they don't exist.


### Adding linting and formatting tests

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


### Marketplace

market-place has some very useful workflows that can be used for many cases: For example check this script that reads a file:
https://github.com/marketplace/actions/read-file

we are going to use one for linting and black: https://github.com/marketplace/actions/lint-action