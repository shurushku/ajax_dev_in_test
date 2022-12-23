import pytest


@pytest.mark.parametrize(
    'email,password,expected',
    [
        pytest.param(
            'qa.ajax.app.automation@gmail.com', 'qa_automation_password', True,
            id='authentication of user that exist in system'
        ),
        pytest.param(
            'qa.ajax.app.automation@gmail.com', 'automation_word', False,
            id='authentication of user with incorrect password'
        ),
        pytest.param(
            'qa.ajax.app.automation@gmail.com', 'automation_word', False,
            id='authentication of user with incorrect password'
        ),
        pytest.param(
            'test_unreal_user@blabla.bla', 'password_with_number_5', False,
            id='authentication of user that does not exist in system'
        ),
        pytest.param(
            '', 'qa_automation_password', False,
            id='authentication of user with missing email'
        ),
        pytest.param(
            'qa.ajax.app.automation@gmail.com', '', False,
            id='authentication of user with missing password'
        ),
        pytest.param(
            '', '', False,
            id='authentication of user with empty inputs'
        ),
    ]
)
def test_user_login(email: str, password: str, expected, user_login_fixture):
    page = user_login_fixture
    page.login_user(email, password)
    page.wait(5)
    assert page.user_on_main_page() == expected
