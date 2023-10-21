# AirBnB_clone

The goal of the AirBnB Clone project is to deploy a simple copy of the [AirBnB Website.](https://www.airbnb.com/)

## 0x00. AirBnB clone - The console

This project involves writing a command interpreter to manage the AirBnB objects.

---
---
**Usage:**

```
$ ./console.py
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)create BaseModel
0e9a245a-7240-4ff8-a51a-300bccffbf40
(hbnb)create BaseModel
74feb4f5-ffd9-4010-8f93-24fec573f0a8
(hbnb)show BaseModel 74feb4f5-ffd9-4010-8f93-24fec573f0a8
[BaseModel] (74feb4f5-ffd9-4010-8f93-24fec573f0a8) {'id': '74feb4f5-ffd9-4010-8f93-24fec573f0a8', 'created_at': datetime.datetime(2023, 10, 21, 22, 32, 36, 713064), 'updated_at': datetime.datetime(2023, 10, 21, 22, 32, 36, 713096)}
(hbnb)create User
9f49c41e-71d9-4bbb-aeb0-2e6b99f43733
(hbnb)update User 9f49c41e-71d9-4bbb-aeb0-2e6b99f43733 "Favourite Movie" "Kungfu Panda"
(hbnb)show User 9f49c41e-71d9-4bbb-aeb0-2e6b99f43733
[User] (9f49c41e-71d9-4bbb-aeb0-2e6b99f43733) {'id': '9f49c41e-71d9-4bbb-aeb0-2e6b99f43733', 'created_at': datetime.datetime(2023, 10, 21, 22, 34, 22, 951722), 'updated_at': datetime.datetime(2023, 10, 21, 22, 35, 1, 435457), 'Favourite Movie': 'Kungfu Panda'}
(hbnb)destroy BaseModel 0e9a245a-7240-4ff8-a51a-300bccffbf40
(hbnb)show BaseModel 0e9a245a-7240-4ff8-a51a-300bccffbf40
** no instance found **
(hbnb)all
[State] (b2c7d1ca-0c74-433a-bd9f-8778e388db2f) {'id': 'b2c7d1ca-0c74-433a-bd9f-8778e388db2f', 'created_at': datetime.datetime(2023, 10, 21, 0, 12, 58, 91202), 'updated_at': datetime.datetime(2023, 10, 21, 0, 12, 58, 91204)}
[State] (c02b47e2-fddb-4485-9564-e4f18498f41b) {'id': 'c02b47e2-fddb-4485-9564-e4f18498f41b', 'created_at': datetime.datetime(2023, 10, 21, 0, 12, 58, 91373), 'updated_at': datetime.datetime(2023, 10, 21, 0, 12, 58, 91375)}
[User] (6e7a68a0-75d4-46b4-af1d-623c2b7ef5a8) {'id': '6e7a68a0-75d4-46b4-af1d-623c2b7ef5a8', 'created_at': datetime.datetime(2023, 10, 21, 0, 12, 58, 91471), 'updated_at': datetime.datetime(2023, 10, 21, 0, 12, 58, 91473)}
[User] (09b2652d-fcb9-4dc1-9e5b-6484475f48e8) {'id': '09b2652d-fcb9-4dc1-9e5b-6484475f48e8', 'created_at': datetime.datetime(2023, 10, 21, 0, 12, 58, 91522), 'updated_at': datetime.datetime(2023, 10, 21, 0, 12, 58, 91524), 'email': True, 'first_name': True, 'password': True, 'last_name': False}
[User] (765f8219-89bb-47f5-8884-e6ec8b5b8ec1) {'id': '765f8219-89bb-47f5-8884-e6ec8b5b8ec1', 'created_at': datetime.datetime(2023, 10, 21, 0, 12, 58, 91610), 'updated_at': datetime.datetime(2023, 10, 21, 0, 12, 58, 91622)}
[BaseModel] (74feb4f5-ffd9-4010-8f93-24fec573f0a8) {'id': '74feb4f5-ffd9-4010-8f93-24fec573f0a8', 'created_at': datetime.datetime(2023, 10, 21, 22, 32, 36, 713064), 'updated_at': datetime.datetime(2023, 10, 21, 22, 32, 36, 713096)}
[User] (9f49c41e-71d9-4bbb-aeb0-2e6b99f43733) {'id': '9f49c41e-71d9-4bbb-aeb0-2e6b99f43733', 'created_at': datetime.datetime(2023, 10, 21, 22, 34, 22, 951722), 'updated_at': datetime.datetime(2023, 10, 21, 22, 35, 1, 435457), 'Favourite Movie': 'Kungfu Panda'}
(hbnb)destroy Review e7abfdc3-c044-498e-8d67-b63abbb3f04a
(hbnb)destroy Review e7abfdc3-c044-498e-8d67-b63abbb3f04a
(hbnb)show Review e7abfdc3-c044-498e-8d67-b63abbb3f04a
** no instance found **
(hbnb)Review.all()
[Review] (ddf88271-98e3-40c7-9fcb-73f5c277ccaa) {'id': 'ddf88271-98e3-40c7-9fcb-73f5c277ccaa', 'created_at': datetime.datetime(2023, 10, 21, 0, 11, 27, 60946), 'updated_at': datetime.datetime(2023, 10, 21, 0, 11, 27, 60948), 'place_id': True, 'user_id': True, 'text': True}
[Review] (986f92cd-6cd4-4361-a245-23710c19bac8) {'id': '986f92cd-6cd4-4361-a245-23710c19bac8', 'created_at': datetime.datetime(2023, 10, 21, 0, 12, 43, 235444), 'updated_at': datetime.datetime(2023, 10, 21, 0, 12, 43, 235445), 'place_id': True, 'user_id': True, 'text': True}
[Review] (49692366-c789-4818-a33f-94e7e88a88e2) {'id': '49692366-c789-4818-a33f-94e7e88a88e2', 'created_at': datetime.datetime(2023, 10, 21, 0, 12, 58, 72527), 'updated_at': datetime.datetime(2023, 10, 21, 0, 12, 58, 72530), 'place_id': True, 'user_id': True, 'text': True}
(hbnb)
(hbnb)Review.count()
3
(hbnb)
(hbnb)User.show(9f49c41e-71d9-4bbb-aeb0-2e6b99f43733)
[User] (9f49c41e-71d9-4bbb-aeb0-2e6b99f43733) {'id': '9f49c41e-71d9-4bbb-aeb0-2e6b99f43733', 'created_at': datetime.datetime(2023, 10, 21, 22, 34, 22, 951722), 'updated_at': datetime.datetime(2023, 10, 21, 22, 35, 1, 435457), 'Favourite Movie': 'Kungfu Panda'}
(hbnb)
(hbnb)City.destroy("8fe5009d-212e-40a3-aded-a86cf10f5b22")
(hbnb)City.show("8fe5009d-212e-40a3-aded-a86cf10f5b22")
** no instance found **
(hbnb)
(hbnb)User.update("09b2652d-fcb9-4dc1-9e5b-6484475f48e8", email, "mitten.mia@cats.pet")
(hbnb)User.show(09b2652d-fcb9-4dc1-9e5b-6484475f48e8)
[User] (09b2652d-fcb9-4dc1-9e5b-6484475f48e8) {'id': '09b2652d-fcb9-4dc1-9e5b-6484475f48e8', 'created_at': datetime.datetime(2023, 10, 21, 0, 12, 58, 91522), 'updated_at': datetime.datetime(2023, 10, 21, 22, 49, 30, 831392), 'email': 'mitten.mia@cats.pet', 'first_name': True, 'password': True, 'last_name': False}
(hbnb)
(hbnb)User.update("09b2652d-fcb9-4dc1-9e5b-6484475f48e8", {'email': 'mitten.mia@cats.pet', 'first_name': 'Mitten', 'password': 'GimmeMilkNowHuman', 'last_name': 'Mia'})
(hbnb)User.show(09b2652d-fcb9-4dc1-9e5b-6484475f48e8)
[User] (09b2652d-fcb9-4dc1-9e5b-6484475f48e8) {'id': '09b2652d-fcb9-4dc1-9e5b-6484475f48e8', 'created_at': datetime.datetime(2023, 10, 21, 0, 12, 58, 91522), 'updated_at': datetime.datetime(2023, 10, 21, 22, 52, 10, 433400), 'email': 'mitten.mia@cats.pet', 'first_name': 'Mitten', 'password': 'GimmeMilkNowHuman', 'last_name': 'Mia'}
(hbnb)
```
