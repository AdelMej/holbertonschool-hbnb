import unittest

from flask import json
from app import create_app
from app.models import review


class TestReviewEndpoints(unittest.TestCase):
    """
    Class for testing review-related API endpoints.
    """
    def setUp(self):
        """
        initialize the test client and app context.
        """
        self.app = create_app()
        self.client = self.app.test_client()

    """
    --POST--
    """
    def test_create_review(self):
        """
        Test creating a new review with valid data.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test",
            "last_name": "test",
            "email": "test@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test")
        self.assertEqual(response.json["last_name"], "test")
        self.assertEqual(response.json["email"], "test@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement",
            "description": "",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id,
            "amenities": [],
            "rooms": 3,
            "surface": 2,
            "capacity": 4
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement")
        self.assertEqual(response.json["description"], "")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertTrue(response.json["owner_id"])
        self.assertEqual(response.json["rooms"], 3)
        self.assertEqual(response.json["surface"], 2)
        self.assertEqual(response.json["capacity"], 4)

        placeid = response.json["id"]
        response = self.client.post('/api/v1/users/', json={
            "first_name": "reviewer1",
            "last_name": "reviewer1",
            "email": "reviewer1@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "reviewer1")
        self.assertEqual(response.json["last_name"], "reviewer1")
        self.assertEqual(response.json["email"], "reviewer1@example.com")

        reviewerid = response.json['id']
        response = self.client.post("/api/v1/reviews/",json={
            "title": "rando title",
            "text": "rando text",
            "rating": 5,
            "user_id": reviewerid,
            "place_id": placeid
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], "rando title")
        self.assertEqual(response.json['text'], 'rando text')
        self.assertEqual(response.json["rating"], 5)


    def test_create_review_invalid_text(self):
        """
        Test creating a new review with invalid text.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test2",
            "last_name": "test2",
            "email": "test2@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test2")
        self.assertEqual(response.json["last_name"], "test2")
        self.assertEqual(response.json["email"], "test2@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement2",
            "description": "",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id,
            "amenities": [],
            "rooms": 3,
            "surface": 2,
            "capacity": 4
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement2")
        self.assertEqual(response.json["description"], "")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertTrue(response.json["owner_id"])
        self.assertEqual(response.json["rooms"], 3)
        self.assertEqual(response.json["surface"], 2)
        self.assertEqual(response.json["capacity"], 4)

        placeid = response.json["id"]
        response = self.client.post('/api/v1/users/', json={
            "first_name": "reviewer3",
            "last_name": "reviewer3",
            "email": "reviewer3@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "reviewer3")
        self.assertEqual(response.json["last_name"], "reviewer3")
        self.assertEqual(response.json["email"], "reviewer3@example.com")

        reviewerid = response.json['id']
        response = self.client.post("/api/v1/reviews/",json={
            "title": "valid title",
            "text": "rando text azdzadjaz ajdoiaz aiozdioazjazoijkd azdiopzad azikd aizkdpoazkazdpkaz kpkazdkopdakpoazkdopazkdopakzop kapodkapozkdpozkaopdkpoaz kdkzaoijkiojiojfioeji aepifk aipkfipakpo fkepozapfo kepozfk poeazkfpoez pofk fkaopzkf ozefp kezpokfpoakpof kpoeazkfop akpofkazepo kfpoakf pokapofkpo ezakpofk poaezpfo aopzkfopkpofak pofkzpeakfopaepof kazeopfkpoazekfpo zakefk epozpofkapo kpekfpo akpofk apoek fpokopf kpoakfopakpofka pokpoa kpokzf pokezpof aepf pokepof kpoezf pokapkpkefa pokopa fkpokfa pokpokd azkdp azkpakzdp azd apokdpoazkd poazdpo azkdpoazkd opazkdpoaz poakpod kazopdkazpoâzpoôkdiopkoipedfjzedfjoiejoi fjefjiozejfiajkiopfzkeaf opkfpo aezpof kazepofk poazkfpoa kfpo eapokfpoazkfazk kaopik ezpof opakpof kpokaezof kôazkfopakzopâzeopfkopkfaopkfopazeopâkopf keopfk opakfpoakf opakokoẑkoefoô^fo^opakop fkeopfkopaôazekfpozaekfpeja iojkiofj iojfio jzio jfezpf pzjpif jzpiaf jkapekf piekfpikapofk pokfpoeakpofka zpo",
            "rating": 5,
            "user_id": reviewerid,
            "place_id": placeid
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["error"], 'Invalid input data')

    def test_create_review_invalid_rating(self):
        """
        Test creating a new review with invalid rating.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test3",
            "last_name": "test3",
            "email": "test3@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test3")
        self.assertEqual(response.json["last_name"], "test3")
        self.assertEqual(response.json["email"], "test3@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement3",
            "description": "",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id,
            "amenities": [],
            "rooms": 3,
            "surface": 2,
            "capacity": 4
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement3")
        self.assertEqual(response.json["description"], "")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertTrue(response.json["owner_id"])
        self.assertEqual(response.json["rooms"], 3)
        self.assertEqual(response.json["surface"], 2)
        self.assertEqual(response.json["capacity"], 4)

        placeid = response.json["id"]
        response = self.client.post('/api/v1/users/', json={
            "first_name": "reviewer4",
            "last_name": "reviewer4",
            "email": "reviewer4@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "reviewer4")
        self.assertEqual(response.json["last_name"], "reviewer4")
        self.assertEqual(response.json["email"], "reviewer4@example.com")

        reviewerid = response.json['id']
        response = self.client.post("/api/v1/reviews/",json={
            "title": "rando title",
            "text": "rando text",
            "rating": -12,
            "user_id": reviewerid,
            "place_id": placeid
        })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["error"], 'Invalid input data')

        response = self.client.post("/api/v1/reviews/",json={
            "title": "rando title",
            "text": "rando text",
            "rating": 30,
            "user_id": reviewerid,
            "place_id": placeid
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["error"], 'Invalid input data')

    """
    --GET--
    """
    def test_fetch_review_fetch_all(self):
        """
        Test fetching all reviews.
        """
        response = self.client.get('/api/v1/reviews/')
        self.assertEqual(response.status_code, 200)

    def test_fetch_review_id(self):
        """
        Test fetching review id.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test4",
            "last_name": "test4",
            "email": "test4@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test4")
        self.assertEqual(response.json["last_name"], "test4")
        self.assertEqual(response.json["email"], "test4@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement",
            "description": "",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id,
            "amenities": [],
            "rooms": 3,
            "surface": 2,
            "capacity": 4
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement")
        self.assertEqual(response.json["description"], "")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertTrue(response.json["owner_id"])
        self.assertEqual(response.json["rooms"], 3)
        self.assertEqual(response.json["surface"], 2)
        self.assertEqual(response.json["capacity"], 4)

        placeid = response.json["id"]
        response = self.client.post('/api/v1/users/', json={
            "first_name": "reviewer5",
            "last_name": "reviewer5",
            "email": "reviewer5@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "reviewer5")
        self.assertEqual(response.json["last_name"], "reviewer5")
        self.assertEqual(response.json["email"], "reviewer5@example.com")

        reviewerid = response.json['id']
        response = self.client.post("/api/v1/reviews/",json={
            "title": "rando title",
            "text": "rando text",
            "rating": 5,
            "user_id": reviewerid,
            "place_id": placeid
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], "rando title")
        self.assertEqual(response.json['text'], 'rando text')
        self.assertEqual(response.json["rating"], 5)

        reviewid = response.json["id"]
        response = self.client.get('/api/v1/reviews/' + reviewid)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['title'], "rando title")
        self.assertEqual(response.json['text'], 'rando text')
        self.assertEqual(response.json["rating"], 5)

    def test_fetch_review_invalid_id(self):
        """
        Test fetching invalid id.
        """
        review_id = "invalid_review_id"
        response = self.client.get('/api/v1/reviews/' + review_id)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], 'Review not found')

    def test_fetch_review_place_id(self):
        """
        Test fetching invalid id.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test5",
            "last_name": "test5",
            "email": "test5@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test5")
        self.assertEqual(response.json["last_name"], "test5")
        self.assertEqual(response.json["email"], "test5@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement",
            "description": "",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id,
            "amenities": [],
            "rooms": 3,
            "surface": 2,
            "capacity": 4
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement")
        self.assertEqual(response.json["description"], "")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertTrue(response.json["owner_id"])
        self.assertEqual(response.json["rooms"], 3)
        self.assertEqual(response.json["surface"], 2)
        self.assertEqual(response.json["capacity"], 4)

        placeid = response.json["id"]
        response = self.client.post('/api/v1/users/', json={
            "first_name": "reviewer6",
            "last_name": "reviewer6",
            "email": "reviewer6@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "reviewer6")
        self.assertEqual(response.json["last_name"], "reviewer6")
        self.assertEqual(response.json["email"], "reviewer6@example.com")

        reviewerid = response.json['id']
        response = self.client.post("/api/v1/reviews/",json={
            "title": "rando title",
            "text": "rando text",
            "rating": 5,
            "user_id": reviewerid,
            "place_id": placeid
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], "rando title")
        self.assertEqual(response.json['text'], 'rando text')
        self.assertEqual(response.json["rating"], 5)

        response = self.client.get('/api/v1/places/' + placeid + '/reviews')
        self.assertEqual(response.status_code, 200)

    def test_fetch_review_place_invalid_id(self):
        """
        Test fetching invalid id.
        """
        placeid = "invalid-id"
        response = self.client.get('/api/v1/places/' + placeid + '/reviews')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], 'Place not found')

    """
    --PUT--
    """
    def test_update_review(self):
        """
        Test updating a review with valid data.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test6",
            "last_name": "test6",
            "email": "test6@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test6")
        self.assertEqual(response.json["last_name"], "test6")
        self.assertEqual(response.json["email"], "test6@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement",
            "description": "",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id,
            "amenities": [],
            "rooms": 3,
            "surface": 2,
            "capacity": 4
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement")
        self.assertEqual(response.json["description"], "")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertTrue(response.json["owner_id"])
        self.assertEqual(response.json["rooms"], 3)
        self.assertEqual(response.json["surface"], 2)
        self.assertEqual(response.json["capacity"], 4)

        placeid = response.json["id"]
        response = self.client.post('/api/v1/users/', json={
            "first_name": "reviewer7",
            "last_name": "reviewer7",
            "email": "reviewer7@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "reviewer7")
        self.assertEqual(response.json["last_name"], "reviewer7")
        self.assertEqual(response.json["email"], "reviewer7@example.com")

        reviewerid = response.json['id']
        response = self.client.post("/api/v1/reviews/",json={
            "title": "rando title",
            "text": "rando text",
            "rating": 5,
            "user_id": reviewerid,
            "place_id": placeid
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], "rando title")
        self.assertEqual(response.json['text'], 'rando text')
        self.assertEqual(response.json["rating"], 5)
        
        reviewid = response.json["id"]
        response = self.client.put("/api/v1/reviews/" + reviewid, json={
            "title": "updated title",
            "text": "updated text",
            "rating": 5,
            "user_id": reviewerid,
            "place_id": placeid
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], 'Review updated successfully')


    def test_updating_review_invalid_title(self):
        """
        Test updating a review with invalid title.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test7",
            "last_name": "test7",
            "email": "test7@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test7")
        self.assertEqual(response.json["last_name"], "test7")
        self.assertEqual(response.json["email"], "test7@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement",
            "description": "",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id,
            "amenities": [],
            "rooms": 3,
            "surface": 2,
            "capacity": 4
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement")
        self.assertEqual(response.json["description"], "")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertTrue(response.json["owner_id"])
        self.assertEqual(response.json["rooms"], 3)
        self.assertEqual(response.json["surface"], 2)
        self.assertEqual(response.json["capacity"], 4)

        placeid = response.json["id"]
        response = self.client.post('/api/v1/users/', json={
            "first_name": "reviewer8",
            "last_name": "reviewer8",
            "email": "reviewer8@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "reviewer8")
        self.assertEqual(response.json["last_name"], "reviewer8")
        self.assertEqual(response.json["email"], "reviewer8@example.com")

        reviewerid = response.json['id']
        response = self.client.post("/api/v1/reviews/",json={
            "title": "rando title",
            "text": "rando text",
            "rating": 5,
            "user_id": reviewerid,
            "place_id": placeid
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], "rando title")
        self.assertEqual(response.json['text'], 'rando text')
        self.assertEqual(response.json["rating"], 5)

        reviewid = response.json["id"]
        response = self.client.put("/api/v1/reviews/" + reviewid, json={
            "title": "",
            "text": "updated text",
            "rating": 5,
            "user_id": reviewerid,
            "place_id": placeid
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["error"], 'Invalid input data')

    def test_updating_review_invalid_text(self):
        """
        Test updating a review with invalid title.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test8",
            "last_name": "test8",
            "email": "test8@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test8")
        self.assertEqual(response.json["last_name"], "test8")
        self.assertEqual(response.json["email"], "test8@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement",
            "description": "",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id,
            "amenities": [],
            "rooms": 3,
            "surface": 2,
            "capacity": 4
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement")
        self.assertEqual(response.json["description"], "")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertTrue(response.json["owner_id"])
        self.assertEqual(response.json["rooms"], 3)
        self.assertEqual(response.json["surface"], 2)
        self.assertEqual(response.json["capacity"], 4)

        placeid = response.json["id"]
        response = self.client.post('/api/v1/users/', json={
            "first_name": "reviewer9",
            "last_name": "reviewer9",
            "email": "reviewer9@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "reviewer9")
        self.assertEqual(response.json["last_name"], "reviewer9")
        self.assertEqual(response.json["email"], "reviewer9@example.com")

        reviewerid = response.json['id']
        response = self.client.post("/api/v1/reviews/",json={
            "title": "rando title",
            "text": "rando text",
            "rating": 5,
            "user_id": reviewerid,
            "place_id": placeid
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], "rando title")
        self.assertEqual(response.json['text'], 'rando text')
        self.assertEqual(response.json["rating"], 5)
        
        reviewid = response.json["id"]
        response = self.client.put("/api/v1/reviews/" + reviewid, json={
            "title": "updated review",
            "text": "updated textz lazldpazldlaz)pdlazpdlazp^dlapẑdla pẑldpâzldpâzlp^azpâzldpâz ldpâzld apâz ldpâzldaldazld lazp^aẑpldaz^az ldâpzld pâzldpâzldpazld azlpd lapâzpâzp^lazpâp^lpâ lp^paz ldpâzlda zlp^pzldazl âlp^lapâ z^a lapz^pâzldalz dazld alzâ zpâ zâẑld pâzld laâz pâẑpld aẑldpal dalz^lazp^azpâ zlpâ^azld pâldazldlazâz âp^pâld aldalâlp^ap^p laâẑpl^plkfopzeiopjujujauijio jeijf ioajfijiocfezfjo jajvononfozjuofjozei jijiojzie jfiojoijiojf iojioez ofi,zeoif, ,ofjoizjfiojzeoifjoi ajifojaijf aiojiof jioaj iojioa jiofjioajf oiajiof jaiojf aoijfiojiojaoiz e",
            "rating": 5,
            "user_id": reviewerid,
            "place_id": placeid
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["error"], 'Invalid input data')

    def test_updating_review_invalid_rating(self):
        """
        Test updating a review with invalid data.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test9",
            "last_name": "test9",
            "email": "test9@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test9")
        self.assertEqual(response.json["last_name"], "test9")
        self.assertEqual(response.json["email"], "test9@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement",
            "description": "",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id,
            "amenities": [],
            "rooms": 3,
            "surface": 2,
            "capacity": 4
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement")
        self.assertEqual(response.json["description"], "")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertTrue(response.json["owner_id"])
        self.assertEqual(response.json["rooms"], 3)
        self.assertEqual(response.json["surface"], 2)
        self.assertEqual(response.json["capacity"], 4)

        placeid = response.json["id"]
        response = self.client.post('/api/v1/users/', json={
            "first_name": "reviewer10",
            "last_name": "reviewer10",
            "email": "reviewer10@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "reviewer10")
        self.assertEqual(response.json["last_name"], "reviewer10")
        self.assertEqual(response.json["email"], "reviewer10@example.com")

        reviewerid = response.json['id']
        response = self.client.post("/api/v1/reviews/",json={
            "title": "rando title",
            "text": "rando text",
            "rating": 5,
            "user_id": reviewerid,
            "place_id": placeid
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], "rando title")
        self.assertEqual(response.json['text'], 'rando text')
        self.assertEqual(response.json["rating"], 5)

        reviewid = response.json["id"]
        response = self.client.put("/api/v1/reviews/" + reviewid, json={
            "title": "abcd",
            "text": "updated text",
            "rating": -5,
            "user_id": reviewerid,
            "place_id": placeid
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["error"], 'Invalid input data')

        response = self.client.put("/api/v1/reviews/" + reviewid, json={
            "title": "abcd",
            "text": "updated text",
            "rating": 30,
            "user_id": reviewerid,
            "place_id": placeid
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["error"], 'Invalid input data')

    def test_updating_review_invalid_id(self):
        """
        Test updating a review with invalid id
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test10",
            "last_name": "test10",
            "email": "test10@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test10")
        self.assertEqual(response.json["last_name"], "test10")
        self.assertEqual(response.json["email"], "test10@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement",
            "description": "",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id,
            "amenities": [],
            "rooms": 3,
            "surface": 2,
            "capacity": 4
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement")
        self.assertEqual(response.json["description"], "")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertTrue(response.json["owner_id"])
        self.assertEqual(response.json["rooms"], 3)
        self.assertEqual(response.json["surface"], 2)
        self.assertEqual(response.json["capacity"], 4)

        placeid = response.json["id"]
        response = self.client.post('/api/v1/users/', json={
            "first_name": "reviewer11",
            "last_name": "reviewer11",
            "email": "reviewer11@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "reviewer11")
        self.assertEqual(response.json["last_name"], "reviewer11")
        self.assertEqual(response.json["email"], "reviewer11@example.com")

        reviewerid = response.json['id']
        response = self.client.post("/api/v1/reviews/",json={
            "title": "rando title",
            "text": "rando text",
            "rating": 5,
            "user_id": reviewerid,
            "place_id": placeid
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], "rando title")
        self.assertEqual(response.json['text'], 'rando text')
        self.assertEqual(response.json["rating"], 5)

        reviewid = "invalid_id"
        response = self.client.put("/api/v1/reviews/" + reviewid, json={
            "title": "abcde",
            "text": "updated text",
            "rating": 5,
            "user_id": reviewerid,
            "place_id": placeid
        })
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], 'Review not found')

    """
    --DELETE--
    """
    def test_delete_review_valid(self):
        """
        Test deleting a new review with invalid data.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test11",
            "last_name": "test11",
            "email": "test11@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test11")
        self.assertEqual(response.json["last_name"], "test11")
        self.assertEqual(response.json["email"], "test11@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement",
            "description": "",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id,
            "amenities": [],
            "rooms": 3,
            "surface": 2,
            "capacity": 4
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement")
        self.assertEqual(response.json["description"], "")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertTrue(response.json["owner_id"])
        self.assertEqual(response.json["rooms"], 3)
        self.assertEqual(response.json["surface"], 2)
        self.assertEqual(response.json["capacity"], 4)

        placeid = response.json["id"]
        response = self.client.post('/api/v1/users/', json={
            "first_name": "reviewer12",
            "last_name": "reviewer12",
            "email": "reviewer12@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "reviewer12")
        self.assertEqual(response.json["last_name"], "reviewer12")
        self.assertEqual(response.json["email"], "reviewer12@example.com")

        reviewerid = response.json['id']
        response = self.client.post("/api/v1/reviews/",json={
            "title": "rando title",
            "text": "rando text",
            "rating": 5,
            "user_id": reviewerid,
            "place_id": placeid
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], "rando title")
        self.assertEqual(response.json['text'], 'rando text')
        self.assertEqual(response.json["rating"], 5)

        reviewid = response.json["id"]
        response = self.client.delete("/api/v1/reviews/" + reviewid)
        self.assertEqual(response.status_code, 204)

    def test_delete_review_invalid_id(self):
        """
        Test deleting a new review with invalid data.
        """
        review_id = "invalid-id"
        response = self.client.delete('/api/v1/reviews/' + review_id)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], 'Review not found')
