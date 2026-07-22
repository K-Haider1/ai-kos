from memory.conversation_memory import ConversationMemory
import pytest


def test_add_interaction():

    memory = ConversationMemory()

    memory.add_interaction(
        "Hello",
        "Hi there",
    )

    history = memory.get_history()

    assert len(history) == 1

    assert history[0]["query"] == "Hello"

    assert history[0]["answer"] == "Hi there"


def test_get_last():

    memory = ConversationMemory()

    for i in range(10):

        memory.add_interaction(
            f"Question {i}",
            f"Answer {i}",
        )

    history = memory.get_last(3)

    assert len(history) == 3

    assert history[0]["query"] == "Question 7"

    assert history[-1]["query"] == "Question 9"


def test_clear():

    memory = ConversationMemory()

    memory.add_interaction(
        "A",
        "B",
    )

    memory.clear()

    assert memory.get_history() == []


def test_empty_query_raises_error():

    memory = ConversationMemory()

    with pytest.raises(ValueError):

        memory.add_interaction(
            "",
            "answer",
        )


def test_empty_answer_raises_error():

    memory = ConversationMemory()

    with pytest.raises(ValueError):

        memory.add_interaction(
            "question",
            "",
        )


def test_invalid_get_last():

    memory = ConversationMemory()

    with pytest.raises(ValueError):

        memory.get_last(0)