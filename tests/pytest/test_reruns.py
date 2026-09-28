import pytest
import random

PLATFORM = "Windows"

@pytest.mark.flaky(reruns=3, reruns_limit=2)
def test_reruns():
    assert False


@pytest.mark.flaky(reruns=3, reruns_limit=2)
class TestsReruns:
    def test_rerun_1(self):
        assert random.choice([True, False])

    def test_rerun_2(self):
        assert random.choice([True, False])

@pytest.mark.flaky(reruns=3, reruns_limit=2, condition= PLATFORM == "Windows")
def test_test_rerun_with_condition():
    assert random.choice([True, False])
