CREATE TABLE "trainers" (
    "id" int   NOT NULL,
    "first_name" varchar   NOT NULL,
    "last_name" varchar   NOT NULL,
    "DOB" Date   NOT NULL,
    "gender" varchar   NOT NULL,
    "hired_on" Date   NOT NULL,
    "phone" varchar   NOT NULL,
    "email" varchar   NOT NULL,
    "active" varchar   NOT NULL,
    "gym_id" int   NOT NULL,
    CONSTRAINT "pk_trainers" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "members" (
    "id" int   NOT NULL,
    "first_name" varchar   NOT NULL,
    "last_name" varchar   NOT NULL,
    "gender" varchar   NOT NULL,
    "DOB" Date   NOT NULL,
    "phone" varchar   NOT NULL,
    "email" varchar   NOT NULL,
    "street" varchar   NOT NULL,
    "city" varchar   NOT NULL,
    "zipcode" varchar   NOT NULL,
    "joined_on" Date   NOT NULL,
    "active" varchar   NOT NULL,
    "trainer_ID" Int   NOT NULL,
    "gym_id" Int   NOT NULL,
    CONSTRAINT "pk_members" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "gym" (
    "id" int   NOT NULL,
    "name" varchar   NOT NULL,
    "street" varchar   NOT NULL,
    "city" varchar   NOT NULL,
    "zipcode" varchar   NOT NULL,
    "phone" varchar   NOT NULL,
    "email" varchar   NOT NULL,
    "manager" varchar   NOT NULL,
    "status" varchar   NOT NULL,
    CONSTRAINT "pk_gym" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "payments" (
    "id" int   NOT NULL,
    "member_ID" Int   NOT NULL,
    "Name" Varchar   NOT NULL,
    "CreditCardNumber" varchar   NOT NULL,
    "ExpiryDate" Date   NOT NULL,
    "Address" varchar   NOT NULL,
    "CCV" varchar   NOT NULL,
    CONSTRAINT "pk_payments" PRIMARY KEY (
        "id"
     )
);

ALTER TABLE "trainers" ADD CONSTRAINT "fk_trainers_gym_id" FOREIGN KEY("gym_id")
REFERENCES "gym" ("id");

ALTER TABLE "members" ADD CONSTRAINT "fk_members_trainer_ID" FOREIGN KEY("trainer_ID")
REFERENCES "trainers" ("id");

ALTER TABLE "members" ADD CONSTRAINT "fk_members_gym_id" FOREIGN KEY("gym_id")
REFERENCES "gym" ("id");

ALTER TABLE "payments" ADD CONSTRAINT "fk_payments_member_ID" FOREIGN KEY("member_ID")
REFERENCES "members" ("id");

SELECT * FROM members;