from urllib.parse import quote


def test_unregister_removes_existing_participant(client):
    # Arrange
    activity_name = "Chess Club"
    encoded_activity_name = quote(activity_name, safe="")
    email = "daniel@mergington.edu"
    path = f"/activities/{encoded_activity_name}/participants"

    # Act
    response = client.delete(path, params={"email": email})
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert payload == {"message": f"Unregistered {email} from {activity_name}"}


def test_unregister_returns_404_for_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Club"
    encoded_activity_name = quote(activity_name, safe="")
    path = f"/activities/{encoded_activity_name}/participants"

    # Act
    response = client.delete(path, params={"email": "student@mergington.edu"})
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload == {"detail": "Activity not found"}


def test_unregister_returns_404_for_missing_participant(client):
    # Arrange
    activity_name = "Chess Club"
    encoded_activity_name = quote(activity_name, safe="")
    email = "not-signed-up@mergington.edu"
    path = f"/activities/{encoded_activity_name}/participants"

    # Act
    response = client.delete(path, params={"email": email})
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload == {"detail": "Participant not found"}