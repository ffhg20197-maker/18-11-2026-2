# WordPress Security Lab — тема 3.2.50

Практическая работа по теме «Назначение конфигурационных файлов WordPress».

## Быстрый запуск
1. Установить Docker Desktop / Docker Compose.
2. Скопировать .env.example в .env и задать длинные уникальные пароли.
3. Выполнить docker compose up -d.
4. Открыть http://localhost:8080 и завершить установку WordPress.

## Проверки
    python3 tests/check-config.py
    docker compose config
    docker compose ps

Проект содержит защиту Apache, robots.txt, безопасные параметры отладки, отключение встроенных редакторов, пример HTTPS-редиректа, скрипт прав доступа и статические тесты.

Важно: HTTPS-редирект находится отдельно в deploy/https-redirect.conf.example и включается только после настройки TLS. Не коммитьте .env, реальные пароли, соли или логи.

Отчёт DOCX сформирован отдельно и доступен в материалах этой беседы. Подробный текстовый отчёт: docs/report.md.
