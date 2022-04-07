from unittest.mock import patch

from app.lesson import Lesson


@patch("app.lesson.requests.get")
def test_request_response_ok(mock_get):
    mocked_response = '[{"id":"624aa519fa63d931d88d8034","externalId":"","title":"Build Trust in your Enterprise","description":"Learn different methods to use in order for you to build trust in your enterprise. ","status":"published","minimumScore":0},{"id":"624aa519fa63d931d88d8035","externalId":"","title":"Your Words Should Match Your Behavior ","description":"Learn how to walk your talk","status":"published","minimumScore":0},{"id":"624aa519fa63d931d88d8036","externalId":"","title":"Be Bold and Track your Behavior ","description":"Identify the importance of being firm and tracking your behavior.","status":"published","minimumScore":0},{"id":"624aa519fa63d931d88d8037","externalId":"","title":"Review","description":"A summary for all the previous lessons.","status":"published","minimumScore":0},{"id":"624aa519fa63d931d88d8038","externalId":"","title":"The Importance of Personal Passion","description":"Learn how passion gives leaders authority","status":"published","minimumScore":0},{"id":"624aa519fa63d931d88d8039","externalId":"","title":"Introduction","description":"This lesson introduces the benefits of being a passionate leader.","status":"published","minimumScore":0},{"id":"624aa519fa63d931d88d803a","externalId":"","title":"Build Relationship & Trust","description":"Recognize why trust is a critical factor for success ","status":"published","minimumScore":0},{"id":"624aa519fa63d931d88d803b","externalId":"","title":"Avoid the Trap of Difficult Decisions","description":"Evaluate how leaders avoid managerial traps","status":"published","minimumScore":0}]'

    mock_get.return_value.ok = True
    mock_get.return_value.text = mocked_response
    response = Lesson().get_lessons("624aa519fa63d931d88d8033")

    assert response.ok
    assert response.text == mocked_response
