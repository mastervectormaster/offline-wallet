# Activate Python Virtual Env (Recommended, but can be skipped)

## Create Python Virtual Env (Only first time)

```sh
python -m venv .venv
```

## Activate Python Virtual Env

```sh
source .venv/bin/activate
```

# Install Dependencies

```sh
pip install -r requirements.txt
```

# Run Tests

```sh
pytest --cov-report term --cov=src tests/
```

> Note: `.env` file is required.

# Run Examples

```sh
python example_erc20_usdt.py
python example_bep20_usdt.py
```
