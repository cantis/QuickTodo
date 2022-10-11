import pytest

from web import create_app, db
from web.models import Todo

@pytest.fixture(scope='session')
def app():
    '''application fixture'''
    app = create_app()
    yield app

def client():
    with app.app_context():
        client = app.test_client()
        # db.create_all
        yield client
        # db.drop_all()


def test_addTodo_ok(client):
    # arrange

    # act
    rv = client.post('/addtodo', data=dict(
        title='test',
        text='test'
    ), follow_redirects=True)

    # assert
    assert b'Added todo' in rv.data


def test_navigate_to_home(client):
    # arrange

    # act
    result = client.get('/', follow_redirects=True)

    # assert
    assert b'Current Todos' in result.data