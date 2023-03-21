from tasks.tasks import create_task


def test_home():
    assert True


def test_tasks():
    assert create_task.run(1)
    assert create_task.run(2)
    assert create_task.run(3)
