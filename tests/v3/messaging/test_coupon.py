import json
import unittest
from urllib.parse import urlparse, parse_qs
from pytest_httpserver import HTTPServer
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    CouponCreateRequest,
    LotteryAcquisitionConditionRequest,
    CouponDiscountRewardRequest,
    DiscountFixedPriceInfoRequest,
    CouponMessage
)


class TestCouponAPI(unittest.TestCase):

    def test_coupon_create(self):
        expected_coupon_id = "COUPON123"
        expected_response_create = {
            "couponId": expected_coupon_id
        }
        expected_body = {
            "acquisitionCondition": {
                "type": "lottery",
                "lotteryProbability": 50,
                "maxAcquireCount": 1000
            },
            "barcodeImageUrl": "https://example.com/barcode.png",
            "couponCode": "UNIQUECODE123",
            "description": "Get 100 Yen off your purchase",
            "endTimestamp": 1700000000,
            "imageUrl": "https://example.com/image.png",
            "maxUseCountPerTicket": 1,
            "startTimestamp": 1600000000,
            "title": "100 Yen OFF",
            "usageCondition": "Minimum purchase of 500 Yen",
            "reward": {
                "type": "discount",
                "priceInfo": {
                    "type": "fixed",
                    "fixedAmount": 100
                }
            },
            "visibility": "PUBLIC",
            "timezone": "ASIA_TOKYO"
        }

        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/coupon",
                method="POST",
            ).respond_with_json(
                expected_response_create,
                status=200
            )

            configuration = Configuration(
                access_token="dummy-channel-access-token",
                host=httpserver.url_for("/")
            )

            with ApiClient(configuration) as api_client:
                line_bot_api = MessagingApi(api_client)

                req = CouponCreateRequest(
                    acquisitionCondition=LotteryAcquisitionConditionRequest(
                        lotteryProbability=50,
                        maxAcquireCount=1000
                    ),
                    barcodeImageUrl="https://example.com/barcode.png",
                    couponCode="UNIQUECODE123",
                    description="Get 100 Yen off your purchase",
                    endTimestamp=1700000000,
                    imageUrl="https://example.com/image.png",
                    maxUseCountPerTicket=1,
                    startTimestamp=1600000000,
                    title="100 Yen OFF",
                    usageCondition="Minimum purchase of 500 Yen",
                    reward=CouponDiscountRewardRequest(
                        priceInfo=DiscountFixedPriceInfoRequest(
                            fixedAmount=100
                        )
                    ),
                    visibility="PUBLIC",
                    timezone="ASIA_TOKYO"
                )

                response = line_bot_api.create_coupon(coupon_create_request=req)

            self.assertEqual(response.coupon_id, expected_coupon_id)
            self.assertEqual(len(httpserver.log), 1)

            request, _ = httpserver.log[0]
            got_body = json.loads(request.data.decode('utf-8'))
            self.assertEqual(got_body, expected_body)

    def test_coupon_close(self):
        expected_coupon_id = "COUPON123"

        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri=f"/v2/bot/coupon/{expected_coupon_id}/close",
                method="PUT",
            ).respond_with_json({}, status=200)

            configuration = Configuration(
                access_token="dummy-channel-access-token",
                host=httpserver.url_for("/")
            )

            with ApiClient(configuration) as api_client:
                line_bot_api = MessagingApi(api_client)
                response = line_bot_api.close_coupon(expected_coupon_id)

            self.assertIsNone(response)
            self.assertEqual(len(httpserver.log), 1)

    def test_list_coupon(self):
        expected_response_list = {
            "items": [
                {"couponId": "COUPON123", "title": "Discount Coupon"},
                {"couponId": "COUPON456", "title": "Special Offer"}
            ],
            "next": "nextPageToken"
        }

        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/v2/bot/coupon",
                method="GET",
            ).respond_with_json(
                expected_response_list,
                status=200
            )

            configuration = Configuration(
                access_token="dummy-channel-access-token",
                host=httpserver.url_for("/")
            )

            with ApiClient(configuration) as api_client:
                line_bot_api = MessagingApi(api_client)
                response = line_bot_api.list_coupon(
                    status=["RUNNING", "CLOSED"],
                    limit=10,
                )

            self.assertEqual(len(response.items), 2)
            self.assertEqual(response.items[0].coupon_id, "COUPON123")
            self.assertEqual(response.items[0].title, "Discount Coupon")
            self.assertEqual(response.items[1].coupon_id, "COUPON456")
            self.assertEqual(response.items[1].title, "Special Offer")
            self.assertEqual(response.next, expected_response_list["next"])
            self.assertEqual(len(httpserver.log), 1)

            request, _ = httpserver.log[0]
            parsed_url = urlparse(request.url)
            query_params = parse_qs(parsed_url.query)

            self.assertIn("status", query_params)
            self.assertIn("limit", query_params)
            self.assertEqual(query_params["status"], ["RUNNING", "CLOSED"])
            self.assertEqual(query_params["limit"], ["10"])

    def test_get_coupon_detail(self):
        expected_coupon_id = "COUPON123"
        expected_response_detail = {
            "couponId": expected_coupon_id,
            "title": "Discount Coupon",
            "status": "RUNNING"
        }

        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri=f"/v2/bot/coupon/{expected_coupon_id}",
                method="GET",
            ).respond_with_json(
                expected_response_detail,
                status=200
            )

            configuration = Configuration(
                access_token="dummy-channel-access-token",
                host=httpserver.url_for("/")
            )

            with ApiClient(configuration) as api_client:
                line_bot_api = MessagingApi(api_client)
                response = line_bot_api.get_coupon_detail(expected_coupon_id)

            self.assertEqual(response.coupon_id, expected_coupon_id)
            self.assertEqual(response.title, expected_response_detail["title"])
            self.assertEqual(len(httpserver.log), 1)

    def test_coupon_message(self):
        expected_coupon_id = "COUPON123"
        coupon_message = CouponMessage(couponId=expected_coupon_id)
        self.assertEqual(coupon_message.to_dict()["couponId"], expected_coupon_id)
        self.assertEqual(coupon_message.to_dict()["type"], "coupon")


if __name__ == '__main__':
    unittest.main()
