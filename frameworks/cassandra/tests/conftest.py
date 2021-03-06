from typing import Iterator

import pytest
import sdk_security
from tests import config


@pytest.fixture(scope="session")
def configure_security(configure_universe: None) -> Iterator[None]:
    yield from sdk_security.security_session(config.SERVICE_NAME)
