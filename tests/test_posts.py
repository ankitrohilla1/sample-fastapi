from typing import List
from app import schemas
import pytest


def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get('/posts/')
    def validate(post):
        return schemas.Postout(**post)

    posts_map = map(validate, res.json())
    posts_list = posts_map
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200
    # assert posts_list[0].Post.id == test_posts[0].id


def test_unauthorized_user_get_all_post(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401


def test_unauthorized_user_get_one_post(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401


def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get("/posts/879")
    assert res.status_code == 404


def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.Postout(**res.json())
    assert post.Post.id == test_posts[0].id

@pytest.mark.parametrize("title, content, published", [("1st", "1st con", True),
                                                       ("2nd", "2nd con", False),
                                                       ("3rd", "3rd con", True)])
def test_create_post(authorized_client, test_user, test_posts, title, content, published):
    res = authorized_client.post("/posts/", json={"title":title, "content":content, "published":published})
    created_post = schemas.PostIn(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.owner_id == test_user['id']


def test_default_published_set(authorized_client, test_user, test_posts):
    res = authorized_client.post("/posts/", json={"title":"12345", "content":"1233"})
    created_post = schemas.PostIn(**res.json())
    assert res.status_code == 201
    assert created_post.title == "12345"
    assert created_post.published == True
    assert created_post.owner_id == test_user['id']


def test_unauthorized_create_post(client, test_user, test_posts):
    res = client.post("/posts/", json={"title": "12345", "content": "1233"})
    assert res.status_code == 401


def test_unauthorized_delete_post(client, test_user, test_posts):
    res = client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401


def test_authorized_delete_post(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 204


def test_delete_post_non_existing(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/27268")
    assert res.status_code == 404


def test_delete_other_user_post(authorized_client, test_user, test_posts, test_user2):
    res = authorized_client.delete(f"/posts/{test_posts[3].id}")
    assert res.status_code == 403

def test_update_post(authorized_client, test_user, test_posts):
    data = {
        "title": "updated", "content":"updated","id": test_posts[0].id
    }
    res = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)
    updated_post = schemas.PostIn(**res.json())
    assert res.status_code == 200
    assert updated_post.title == data['title']
    assert updated_post.content == data['content']


def test_other_user_post(authorized_client, test_user, test_posts, test_user2):
    data = {
        "title": "updated", "content":"updated","id": test_posts[3].id
    }
    res = authorized_client.put(f"/posts/{test_posts[3].id}", json=data)
    # updated_post = schemas.PostIn(**res.json())
    assert res.status_code == 403


def test_unauthorized_update_post(client, test_user, test_posts, test_user2):
    data = {
        "title": "updated", "content":"updated","id": test_posts[0].id
    }
    res = client.put(f"/posts/{test_posts[0].id}", json=data)
    # updated_post = schemas.PostIn(**res.json())
    assert res.status_code == 401


def test_update_post_non_existing(authorized_client, test_user, test_posts):
    data = {
        "title": "updated", "content":"updated","id": test_posts[0].id
    }
    res = authorized_client.put(f"/posts/83583", json=data)
    assert res.status_code == 404