from unittest.mock import patch

from app.course import Course


@patch("app.lesson.requests.get")
def test_request_response_ok(mock_get):
    mocked_response = '{"totalCount":4,"items":[{"id":"624aa519fa63d931d88d8033","externalId":"","title":"How to be a Passionate Leader","description":"This course explains how to impact others as a leader in a positive manner.\\n","status":"published","locale":"en","duration":2400,"thumbnailUrl":"https://da9zu2inyxpcd.cloudfront.net/images/course.brandingImage-1542280071788.png","createdDateTime":"2022-04-04T07:58:17.0140000Z","modifiedDateTime":"2022-04-04T07:58:58.5830000Z"},{"id":"624aa51afa63d931d88d80a6","externalId":"","title":"Understanding Customer Motivations","description":"Gain an in depth understanding of customer psychology - analyse why customers come to a store, and why they buy what they buy. ","status":"published","locale":"en","duration":1200,"thumbnailUrl":"https://da9zu2inyxpcd.cloudfront.net/images/course.brandingImage-1540422459125.jpeg","createdDateTime":"2022-04-04T07:58:18.7780000Z","modifiedDateTime":"2022-04-04T07:58:56.1400000Z"},{"id":"624aa519fa63d931d88d8064","externalId":"","title":"Teamwork in Hospitality","description":"By embracing teamwork, you will not only improve your own working experience, but also that of your co-workers. Let’s look at how you can improve your teamwork skills. ","status":"published","locale":"en","duration":1200,"thumbnailUrl":"https://da9zu2inyxpcd.cloudfront.net/images/course.brandingImage-1543187228448.jpeg","createdDateTime":"2022-04-04T07:58:17.8980000Z","modifiedDateTime":"2022-04-04T07:58:53.9820000Z"},{"id":"624aa51afa63d931d88d8085","externalId":"","title":"Creating a Positive Customer Experience","description":"This course is an overview of how to create a positive customer experience while working in the retail industry.","status":"published","locale":"en","duration":1200,"thumbnailUrl":"https://d4r32jufzfa4q.cloudfront.net/images/course.brandingImage-1545278384828.jpeg","createdDateTime":"2022-04-04T07:58:18.4050000Z","modifiedDateTime":"2022-04-04T07:58:48.3760000Z"}]}'

    mock_get.return_value.ok = True
    mock_get.return_value.text = mocked_response
    response = Course().get_course()

    assert response.ok
    assert response.text == mocked_response
