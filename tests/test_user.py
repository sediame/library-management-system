from src.user import User


def test_user():
    user = User("test_id")
    assert "test_id" == user.id_user
