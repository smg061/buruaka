--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1 (Debian 14.1-1.pgdg110+1)
-- Dumped by pg_dump version 14.1 (Debian 14.1-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: app
--



--
-- Data for Name: auth_refresh_token; Type: TABLE DATA; Schema: public; Owner: app
--



--
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: app
--

INSERT INTO public.students ( first_name, last_name, email, profile_picture, sprite, phone_number, relationship_level, profile_message, dob) VALUES ( 'Noa', 'Ushio', 'ushio_noa@momotalk.com', 'https://static.miraheze.org/bluearchivewiki/2/23/Noa.png', 'path_to_noa_sprite.jpg', '0987654321', 1, 'The Melancholy of Kivotos', '2000-04-13 00:00:00');
INSERT INTO public.students (first_name, last_name, email, profile_picture, sprite, phone_number, relationship_level, profile_message, dob) VALUES ('Himari', 'Akeboshi', 'alabaster-white-beautiful-hacker@momotalk.com', 'https://static.miraheze.org/bluearchivewiki/5/5a/Himari.png', 'path_to_himari_sprite.jpg', '1234567890', 4, 'Millenium''s greatest genius is here!', '2000-12-10 00:00:00');
INSERT INTO public.students (first_name, last_name, email, profile_picture, sprite, phone_number, relationship_level, profile_message, dob) VALUES ('Yuuka', 'Hayase', 'hayase_yuuka@momotalk.com', 'https://static.miraheze.org/bluearchivewiki/3/3e/Yuuka.png', 'path_to_yuuka_sprite.jpg', '1234567890', 11, 'Just as I calculated', '2000-03-14 00:00:00');
INSERT INTO public.students ( first_name, last_name, email, profile_picture, sprite, phone_number, relationship_level, profile_message, dob) VALUES ('Ui', 'Kozeki', 'ui_kozeki@momotalk.com', 'https://static.miraheze.org/bluearchivewiki/1/18/Ui.png', 'path_to_ui_sprite.jpg', '233234', 2, 'AFK', '2000-04-23 00:00:00');
INSERT INTO public.students ( first_name, last_name, email, profile_picture, sprite, phone_number, relationship_level, profile_message, dob) VALUES ('Koyuki', 'Kurosaki', 'white_rabbit@momotalk.com', 'https://static.miraheze.org/bluearchivewiki/a/af/Koyuki.png', 'path_to_koyuki_sprite.jpg', '233234', 69, 'Gracias por dollaris, idiota', '2000-02-14 00:00:00');
INSERT INTO public.students ( first_name, last_name, email, profile_picture, sprite, phone_number, relationship_level, profile_message, dob) VALUES ('Aru', 'Rikuhachima', 'aru_outlaw@momotalk.com', 'https://static.miraheze.org/bluearchivewiki/d/db/Aru.png', 'path_to_aru_sprite.jpg', '888-888-888', 1, 'I''ll solve any problem!', '2000-03-12 00:00:00');
INSERT INTO public.students ( first_name, last_name, email, profile_picture, sprite, phone_number, relationship_level, profile_message, dob) VALUES ('Mika', 'Misono ', 'princess_mikaw@momotalk.com', 'https://static.miraheze.org/bluearchivewiki/c/c8/Mika.png', 'path_to_mika_sprite.jpg', '888-888-888', 8, 'Looking for new people to chat with!', '2000-05-08 00:00:00');
INSERT INTO public.students ( first_name, last_name, email, profile_picture, sprite, phone_number, relationship_level, profile_message, dob) VALUES ('Toki', 'Asuma ', 'strongest_maid_toki@momotalk.com', 'https://static.miraheze.org/bluearchivewiki/e/e4/Toki.png', 'path_to_toki_sprite.jpg', '888-888-888', 8, 'On standby.', '2000-08-16 00:00:00');
INSERT INTO public.students ( first_name, last_name, email, profile_picture, sprite, phone_number, relationship_level, profile_message, dob) VALUES ('Aris', 'Tendou ', 'gamer_hero_aris@momotalk.com', 'https://static.miraheze.org/bluearchivewiki/0/0f/Arisu.png', 'path_to_aris_sprite.jpg', '888-888-888', 11, 'Aris: Game Dev Dep.', '2000-03-25 00:00:00');


--
-- Data for Name: sensei_messages; Type: TABLE DATA; Schema: public; Owner: app
--



--
-- Data for Name: student_messages; Type: TABLE DATA; Schema: public; Owner: app
--



--
-- Data for Name: student_phrases; Type: TABLE DATA; Schema: public; Owner: app
--



--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: app
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);


--
-- Name: sensei_messages_id_seq; Type: SEQUENCE SET; Schema: public; Owner: app
--

SELECT pg_catalog.setval('public.sensei_messages_id_seq', 1, false);


--
-- Name: student_messages_id_seq; Type: SEQUENCE SET; Schema: public; Owner: app
--

SELECT pg_catalog.setval('public.student_messages_id_seq', 1, false);


--
-- Name: student_phrases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: app
--

SELECT pg_catalog.setval('public.student_phrases_id_seq', 1, false);


--
-- Name: students_id_seq; Type: SEQUENCE SET; Schema: public; Owner: app
--

SELECT pg_catalog.setval('public.students_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

