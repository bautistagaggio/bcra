import pytest

@pytest.mark.usefixtures('init_driver')
@pytest.mark.usefixtures('info_logging')
class BaseTest:
    pass