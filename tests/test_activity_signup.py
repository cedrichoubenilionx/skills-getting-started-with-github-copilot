def test_signup_adds_student_to_activity(client):
    # Arrange
    activity_name = "Chess%20Club"
    email = "new.student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    updated = client.get("/activities").json()["Chess Club"]["participants"]

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for Chess Club"
    assert email in updated


def test_signup_returns_400_when_student_already_signed_up(client):
    # Arrange
    activity_name = "Chess%20Club"
    existing_email = "michael@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": existing_email},
    )

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_signup_returns_404_for_unknown_activity(client):
    # Arrange
    unknown_activity = "Unknown%20Club"
    email = "student@mergington.edu"

    # Act
    response = client.post(f"/activities/{unknown_activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_remove_signup_removes_student_from_activity(client):
    # Arrange
    activity_name = "Chess%20Club"
    email = "daniel@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": email})
    updated = client.get("/activities").json()["Chess Club"]["participants"]

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {email} from Chess Club"
    assert email not in updated


def test_remove_signup_returns_400_when_student_not_signed_up(client):
    # Arrange
    activity_name = "Chess%20Club"
    missing_email = "not.signed.up@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": missing_email},
    )

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_remove_signup_returns_404_for_unknown_activity(client):
    # Arrange
    unknown_activity = "Unknown%20Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(f"/activities/{unknown_activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
