from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


class TestUserRegistration:
    """TestUserRegistration tests /users"""

    def test_get_request_returns_405(self):
        """register endpoint only expect a post request"""
        response = client.get("/users")
        assert response.status_code == 405
