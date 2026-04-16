def test_signup_then_unregister_workflow(client):
    # Arrange
    activity_name = "Science Club"
    email = "workflow.student@mergington.edu"

    # Act
    signup_response = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    after_signup = client.get("/activities").json()

    unregister_response = client.delete(
        f"/activities/{activity_name}/participants", params={"email": email}
    )
    after_unregister = client.get("/activities").json()

    # Assert
    assert signup_response.status_code == 200
    assert email in after_signup[activity_name]["participants"]

    assert unregister_response.status_code == 200
    assert email not in after_unregister[activity_name]["participants"]
