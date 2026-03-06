from urllib.parse import quote


def test_signup_adds_new_participant(client):
    # Arrange
    activity_name = "Chess Club"
    encoded_activity_name = quote(activity_name, safe="")
    email = "newstudent@mergington.edu"
    path = f"/activities/{encoded_activity_name}/signup"

    # Act
    response = client.post(path, params={"email": email})
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert payload == {"message": f"Signed up {email} for {activity_name}"}


def test_signup_returns_404_for_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Club"
    encoded_activity_name = quote(activity_name, safe="")
    path = f"/activities/{encoded_activity_name}/signup"

    # Act
    response = client.post(path, params={"email": "student@mergington.edu"})
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload == {"detail": "Activity not found"}


def test_signup_returns_400_for_duplicate_participant(client):
    # Arrange
    activity_name = "Chess Club"
    encoded_activity_name = quote(activity_name, safe="")
    email = "michael@mergington.edu"
    path = f"/activities/{encoded_activity_name}/signup"

    # Act
    response = client.post(path, params={"email": email})
    payload = response.json()

    # Assert
    assert response.status_code == 400
    assert payload == {"detail": "Student already signed up for this activity"}