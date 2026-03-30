def test_get_activities_returns_all_known_activities(client):
    # Arrange
    endpoint = "/activities"
    expected_activities = {
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Basketball Club",
        "Tennis Team",
        "Art Club",
        "Drama Club",
        "Debate Club",
        "Science Club",
    }

    # Act
    response = client.get(endpoint)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert set(payload.keys()) == expected_activities
