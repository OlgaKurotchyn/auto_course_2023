
def test_search_repo ():
    assert 1 == 1


def test_user_age_is_42(user):
    assert user.age == 43



def test_user_age_is_50():
    print("Create user")
    user = User(42)

    assert user.age == 43

    print("Remove user")
    user.remove()





