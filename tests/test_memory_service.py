from services.memory_service import MemoryService


def test_save():

    service = MemoryService()

    service.save(
        "Hello",
        "Hi",
    )

    history = service.history()

    assert len(history) == 1

    assert history[0]["query"] == "Hello"

    assert history[0]["answer"] == "Hi"


def test_recent():

    service = MemoryService()

    for i in range(5):

        service.save(
            f"Q{i}",
            f"A{i}",
        )

    history = service.recent(2)

    assert len(history) == 2

    assert history[0]["query"] == "Q3"

    assert history[1]["query"] == "Q4"


def test_clear():

    service = MemoryService()

    service.save(
        "Hello",
        "World",
    )

    service.clear()

    assert service.history() == []