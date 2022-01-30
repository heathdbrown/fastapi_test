# FastAPI Test
> Messing with FASTAPI

# Run  the application
```bash
docker-compose up -d --build
```

# Test the application
```bash
docker-compose up -d --build
docker-compose exec -T web pytest .
```

# Non-docker workflow, local only

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r ./src/requirements-dev.txt
pytest .
```

# See the application
- http://localhost:8002/ping
- http://localhost:8002/docs

# References
- [Devleoping and Testing an Asynchronous API with FastAPI and Pytest: testdrive.io](https://testdriven.io/blog/fastapi-crud/)
- [Testing FASTAPI endpoints with docker and pytest: jeffastor.com](https://www.jeffastor.com/blog/testing-fastapi-endpoints-with-docker-and-pytest)
- [Using FastAPI to Build Python Web APIs: realpython.com](https://realpython.com/fastapi-python-web-apis/)
- [FastAPI Example: github.com](https://github.com/nsidnev/fastapi-realworld-example-app)
- [FastAPI Full Stack Postgresal: github.com](https://github.com/tiangolo/full-stack-fastapi-postgresql)
- [FastAPI Users: github.com](https://github.com/fastapi-users/fastapi-users)
- [ASGI-LifeSpan: github.com](https://github.com/florimondmanca/asgi-lifespan)
- [CISAGov Python Template: github.com](https://github.com/cisagov/skeleton-python-library)
