FROM redis:4.0.11

ENV REDIS_PASSWORD wDUp5tssqV8qQLk5

CMD ["sh", "-c", "exec redis-server --requirepass \"$REDIS_PASSWORD\""]
