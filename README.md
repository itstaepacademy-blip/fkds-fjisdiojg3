# quality-gate-lab

Учебный проект для практических работ 1 и 2 по Quality Gate.

## Практика 1 — локальный Quality Gate

Установка инструментов:

```bash
python -m pip install -r requirements-dev.txt
pre-commit install
```

Проверки вручную:

```bash
ruff format --check .
ruff check .
pytest
pre-commit run --all-files
```

## Практика 2 — GitHub Actions CI

Файл `.github/workflows/ci.yml` автоматически запускает Ruff Format, Ruff Check и Pytest при push в `main` и при создании Pull Request в `main`.

1. Отправьте проект в GitHub в ветку `main`.
2. Создайте ветку `feat/discount-calculator`.
3. Для демонстрации провала CI добавьте в `cashback.py` функцию с ошибками форматирования и неиспользуемой переменной, закоммитьте её с `--no-verify` и откройте Pull Request.
4. После просмотра упавших проверок исправьте функцию, добавьте тест и отправьте исправляющий коммит.
5. Дождитесь успешных проверок и объедините Pull Request.


## Функции

- `calculate_cashback(price)` — возвращает 5% кэшбэка.
- `calculate_discount(price, discount_percent)` — возвращает цену после скидки.
