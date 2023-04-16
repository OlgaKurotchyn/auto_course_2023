import pytest

class User:
    def __init__(self, age) -> None:
        # database interacton
        self.age = age

    def remove(self):
        # database iteraction
        self.age = None

@pytest.fixture
def user():
    #before test
    print("Create user")
    user = User(42)

    # pass user object to test
    yield user
        
    #after test
    print("Remove user")
    user.remove()



def test_user_age_is_42(user):
    assert user.age == 43