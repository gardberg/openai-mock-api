# Mock OpenAI-like API

Simple API server serving a mock OpenAI-like API.


## Usage

### Locally
Clone repo:

`git clone git@github.com:gardberg/openai-mock-api.git`

Install dependencies using poetry in a virtual environment:

`poetry install`

Run the server on `localhost:8000`:

`poetry run python src/api.py`

Run tests with debug output:

`poetry run pytest -s`

### Container

TODO

## TODO

- [ ] Add automated tests
- [ ] Support streaming responses
- [ ] Add a `Dockerfile` to build a Docker image
- [ ] Add a `docker-compose.yml` 
