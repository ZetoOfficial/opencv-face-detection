# OpenCV Face Detection

## Описание

Приложение на Python, которое обнаруживает лица на изображении с использованием библиотеки OpenCV.

## Использование

### Запуск с Docker

1. Убедитесь, что у вас установлен Docker.
2. Скачайте образ:

    ```bash
    docker pull zetoqqq/opencv-face-detection:latest
    ```

3. Запустите контейнер:

    ```bash
    docker run --rm -v $(pwd):/app zetoqqq/opencv-face-detection:latest python app/main.py path/to/your/image.jpg
    ```

    Если путь к изображению не указан, будет использовано `app/image.jpg` из репозитория.

### Пример запуска без аргументов

Если вы хотите использовать изображение по умолчанию из репозитория:

```bash
docker run --rm zetoqqq/opencv-face-detection:latest
```
