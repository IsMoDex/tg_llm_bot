# КассПомощник (tg_llm_bot)

**КассПомощник** — это Telegram-бот для помощи в настройке и обслуживании кассовой техники. Бот использует LLM (ChatGPT) для генерации ответов на вопросы, связанные с фискальными регистраторами, POS-системами и чековыми принтерами.

## Основные возможности

- Ответы на вопросы по настройке кассового оборудования
- Поддержка истории диалога и контекста
- Хранение моделей касс пользователя
- Логирование запросов и ошибок
- Конфигурация через `.env`

## Требования

- Python 3.11+
- Библиотеки из `requirements.txt`
- API ключ OpenAI (`OPENAI_API_KEY`)
- Telegram Bot Token (`TELEGRAM_BOT_TOKEN`)

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://your-repo-url/tg_llm_bot.git
   cd tg_llm_bot
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .\.venv\Scripts\activate  # Windows PowerShell
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Создайте `.env` в корне проекта и добавьте:
   ```env
   TELEGRAM_BOT_TOKEN=your-telegram-token
   OPENAI_API_KEY=your-openai-api-key
   ```

## Запуск

```bash
python bot.py
```

Бот запустится и начнёт принимать сообщения в Telegram.

## Структура проекта

```
tg_llm_bot/
├── bot.py              # Точка входа, запуск бота
├── config.py           # Загрузка переменных окружения
├── .env                # Конфиг (не коммитить в репозиторий)
├── requirements.txt    # Зависимости
├── handlers/           # Обработчики команд и сообщений
│   ├── __init__.py
│   ├── start.py
│   ├── help.py
│   ├── message.py
│   └── cash_registers.py
├── llm/                # Логика работы с LLM и контекстом
│   ├── __init__.py
│   ├── context.py
│   └── openai_llm.py
├── storage/            # Модули хранения данных в памяти
│   ├── message_history.py
│   └── cash_registers.py
├── queries/            # Модули для работы с БД (Prisma)
│   ├── users.py
│   ├── messages.py
│   └── history.py
├── utils/              # Вспомогательные утилиты
│   └── logger.py
├── logs/               # Логи работы бота
└── README.md           # Этот файл
```

## Использование

- `/start` — начать работу с ботом
- `/help` — справка по использованию
- `/кассы <модель>` — добавить модель кассы в свой список
- Просто отправьте вопрос про кассовую технику
