

-- ----------------------------
-- Sequence structure for role_id_role_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."role_id_role_seq";
CREATE SEQUENCE "public"."role_id_role_seq" 
INCREMENT 1
MINVALUE  1000
MAXVALUE 2147483647
START 1000
CACHE 1;

-- ----------------------------
-- Table structure for login
-- ----------------------------
DROP TABLE IF EXISTS "public"."login";
CREATE TABLE "public"."login" (
  "user_id" uuid NOT NULL,
  "username" varchar(20) COLLATE "pg_catalog"."default" NOT NULL,
  "password" varchar(60) COLLATE "pg_catalog"."default" NOT NULL,
  "disable" bool NOT NULL,
  "confirm_email" bool NOT NULL,
  "role_id" int2 NOT NULL
)
;

-- ----------------------------
-- Records of login
-- ----------------------------
INSERT INTO "public"."login" VALUES ('a72941b1-3992-4727-8a1f-06158f51eaf6', 'hacao123', '123', 'f', 'f', 1001);

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS "public"."role";
CREATE TABLE "public"."role" (
  "role_id" int2 NOT NULL DEFAULT nextval('role_id_role_seq'::regclass),
  "name_role" varchar(30) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO "public"."role" VALUES (1001, 'Customer');
INSERT INTO "public"."role" VALUES (1002, 'Employee');

-- ----------------------------
-- Table structure for user_info
-- ----------------------------
DROP TABLE IF EXISTS "public"."user_info";
CREATE TABLE "public"."user_info" (
  "user_id" uuid NOT NULL,
  "full_name" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "email" varchar(60) COLLATE "pg_catalog"."default" NOT NULL,
  "phone_number" varchar(15) COLLATE "pg_catalog"."default" NOT NULL,
  "birthday" date,
  "date_create" timestamp(6)
)
;

-- ----------------------------
-- Records of user_info
-- ----------------------------
INSERT INTO "public"."user_info" VALUES ('a72941b1-3992-4727-8a1f-06158f51eaf6', 'Do Ha Cao', 'hacao@gmail.com', '0586887777', '1999-05-05', '2021-06-10 17:18:57');

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."role_id_role_seq"
OWNED BY "public"."role"."role_id";
SELECT setval('"public"."role_id_role_seq"', 1005, true);

-- ----------------------------
-- Indexes structure for table login
-- ----------------------------
CREATE UNIQUE INDEX "unique_username" ON "public"."login" USING btree (
  "username" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table login
-- ----------------------------
ALTER TABLE "public"."login" ADD CONSTRAINT "login_pkey" PRIMARY KEY ("user_id");

-- ----------------------------
-- Primary Key structure for table role
-- ----------------------------
ALTER TABLE "public"."role" ADD CONSTRAINT "role_pkey" PRIMARY KEY ("role_id");

-- ----------------------------
-- Indexes structure for table user_info
-- ----------------------------
CREATE UNIQUE INDEX "unique_email" ON "public"."user_info" USING btree (
  "email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE UNIQUE INDEX "unique_phone_number" ON "public"."user_info" USING btree (
  "phone_number" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table user_info
-- ----------------------------
ALTER TABLE "public"."user_info" ADD CONSTRAINT "user_info_pkey" PRIMARY KEY ("user_id");

-- ----------------------------
-- Foreign Keys structure for table login
-- ----------------------------
ALTER TABLE "public"."login" ADD CONSTRAINT "login_role_id_fkey" FOREIGN KEY ("role_id") REFERENCES "public"."role" ("role_id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table user_info
-- ----------------------------
ALTER TABLE "public"."user_info" ADD CONSTRAINT "user_info_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."login" ("user_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
