import pytest

from log10.load import log10_session


def pytest_addoption(parser):
    parser.addoption("--openai_model", action="store", help="Model name for OpenAI tests")

    parser.addoption("--openai_vision_model", action="store", help="Model name for OpenAI vision tests")

    parser.addoption("--anthropic_model", action="store", help="Model name for Message API Anthropic tests")

    parser.addoption("--anthropic_legacy_model", action="store", help="Model name for legacy Anthropic tests")

    parser.addoption("--lamini_model", action="store", help="Model name for Lamini tests")

    parser.addoption(
        "--mistralai_model", action="store", default="mistral-tiny", help="Model name for Mistralai tests"
    )

    parser.addoption("--google_model", action="store", help="Model name for Google tests")

    parser.addoption("--llm_provider", action="store", help="Model provider name for Magentic tests")


@pytest.fixture
def openai_model(request):
    return request.config.getoption("--openai_model")


@pytest.fixture
def openai_vision_model(request):
    return request.config.getoption("--openai_vision_model")


@pytest.fixture
def anthropic_model(request):
    return request.config.getoption("--anthropic_model")


@pytest.fixture
def anthropic_legacy_model(request):
    return request.config.getoption("--anthropic_legacy_model")


@pytest.fixture
def mistralai_model(request):
    return request.config.getoption("--mistralai_model")


@pytest.fixture
def lamini_model(request):
    return request.config.getoption("--lamini_model")


@pytest.fixture
def google_model(request):
    return request.config.getoption("--google_model")


@pytest.fixture
def llm_provider(request):
    return request.config.getoption("--llm_provider")


@pytest.fixture
def magentic_models(request):
    llm_provider = request.config.getoption("--llm_provider")
    model_config_name = f"--{llm_provider}_model"
    vision_model_config_name = llm_provider == "openai" and f"--{llm_provider}_vision_model" or model_config_name

    return {
        "chat_model": request.config.getoption(model_config_name),
        "vision_model": request.config.getoption(vision_model_config_name),
    }


@pytest.fixture
def session():
    with log10_session() as session:
        assert session.last_completion_id() is None, "No completion ID should be found."
        yield session
