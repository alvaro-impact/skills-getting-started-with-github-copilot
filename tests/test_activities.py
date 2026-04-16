def test_root_redirects_to_static_index(client):
    # Arrange
    root_path = "/"

    # Act
    response = client.get(root_path, follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_all_activities(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)

    # Assert
    payload = response.json()
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert len(payload) == 9


def test_each_activity_has_required_fields(client):
    # Arrange
    endpoint = "/activities"
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get(endpoint)

    # Assert
    payload = response.json()
    for activity in payload.values():
        assert required_fields.issubset(activity.keys())
