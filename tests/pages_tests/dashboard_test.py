
from app_main import app
from tests import OhmTestCase


class DashboardTest(OhmTestCase):
    @staticmethod
    def test_dashboard():
        with app.test_client() as c:
            response = c.get('/dashboard')
            assert "Ready to begin assessment" in response.data

    @staticmethod
    def test_community_response():
        with app.test_client() as c:
            response = c.get('/community')
            assert "Recent Signed Users" in response.data
