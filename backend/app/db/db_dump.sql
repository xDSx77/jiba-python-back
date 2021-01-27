--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3
-- Dumped by pg_dump version 12.2

-- Started on 2021-01-26 17:06:30

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
-- TOC entry 2999 (class 1262 OID 17017)
-- Name: python-rpg-api; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "python-rpg-api" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'French_France.1252' LC_CTYPE = 'French_France.1252';


ALTER DATABASE "python-rpg-api" OWNER TO postgres;

\connect -reuse-previous=on "dbname='python-rpg-api'"

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 207 (class 1259 OID 17102)
-- Name: armor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.armor (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    protection integer DEFAULT 1 NOT NULL,
    price integer DEFAULT 1 NOT NULL
);


ALTER TABLE public.armor OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 17100)
-- Name: armor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.armor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.armor_id_seq OWNER TO postgres;

--
-- TOC entry 3000 (class 0 OID 0)
-- Dependencies: 206
-- Name: armor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.armor_id_seq OWNED BY public.armor.id;


--
-- TOC entry 205 (class 1259 OID 17087)
-- Name: monster; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monster (
    id integer NOT NULL,
    monster_type_id integer NOT NULL,
    hp integer DEFAULT 1 NOT NULL
);


ALTER TABLE public.monster OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 17085)
-- Name: monster_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monster_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.monster_id_seq OWNER TO postgres;

--
-- TOC entry 3001 (class 0 OID 0)
-- Dependencies: 204
-- Name: monster_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monster_id_seq OWNED BY public.monster.id;


--
-- TOC entry 203 (class 1259 OID 17072)
-- Name: monster_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monster_type (
    id integer NOT NULL,
    name varchar(50) NOT NULL,
    hp_max integer DEFAULT 1 NOT NULL,
    damage integer DEFAULT 1 NOT NULL,
    xp_value integer DEFAULT 1 NOT NULL,
    gold_value integer DEFAULT 1 NOT NULL
);


ALTER TABLE public.monster_type OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 17206)
-- Name: monster_info; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.monster_info AS
 SELECT monster.id AS id,
    monster.monster_type_id,
    monster.hp,
    monster_type.damage,
    monster_type.hp_max,
    monster_type.gold_value,
    monster_type.xp_value,
    monster_type.name
   FROM (public.monster
     JOIN public.monster_type ON ((monster.monster_type_id = monster_type.id)));


ALTER TABLE public.monster_info OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 17070)
-- Name: monster_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monster_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.monster_type_id_seq OWNER TO postgres;

--
-- TOC entry 3002 (class 0 OID 0)
-- Dependencies: 202
-- Name: monster_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monster_type_id_seq OWNED BY public.monster_type.id;


--
-- TOC entry 213 (class 1259 OID 17153)
-- Name: player; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player (
    id integer NOT NULL,
    username character varying(50) NOT NULL,
    level integer DEFAULT 1 NOT NULL,
    xp integer DEFAULT 0 NOT NULL,
    xp_max integer DEFAULT 100 NOT NULL,
    hp integer DEFAULT 10 NOT NULL,
    hp_max integer DEFAULT 10 NOT NULL,
    gold integer DEFAULT 0 NOT NULL,
    weapon_id integer,
    armor_id integer
);


ALTER TABLE public.player OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 17151)
-- Name: player_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.player_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.player_id_seq OWNER TO postgres;

--
-- TOC entry 3003 (class 0 OID 0)
-- Dependencies: 212
-- Name: player_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.player_id_seq OWNED BY public.player.id;


--
-- TOC entry 215 (class 1259 OID 17182)
-- Name: player_quest; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_quest (
    player_id integer NOT NULL,
    quest_id integer NOT NULL,
    progress integer DEFAULT 0 NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.player_quest OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 17180)
-- Name: player_quest_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.player_quest_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.player_quest_id_seq OWNER TO postgres;

--
-- TOC entry 3004 (class 0 OID 0)
-- Dependencies: 214
-- Name: player_quest_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.player_quest_id_seq OWNED BY public.player_quest.id;


--
-- TOC entry 211 (class 1259 OID 17132)
-- Name: quest; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.quest (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    monster_type_id integer NOT NULL,
    goal integer DEFAULT 1 NOT NULL,
    xp_value integer DEFAULT 1 NOT NULL,
    gold_value integer DEFAULT 1 NOT NULL
);


ALTER TABLE public.quest OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 17130)
-- Name: quest_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.quest_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.quest_id_seq OWNER TO postgres;

--
-- TOC entry 3005 (class 0 OID 0)
-- Dependencies: 210
-- Name: quest_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.quest_id_seq OWNED BY public.quest.id;


--
-- TOC entry 209 (class 1259 OID 17115)
-- Name: weapon; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.weapon (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    damage integer DEFAULT 1 NOT NULL,
    price integer DEFAULT 1 NOT NULL
);


ALTER TABLE public.weapon OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 17113)
-- Name: weapon_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.weapon_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.weapon_id_seq OWNER TO postgres;

--
-- TOC entry 3006 (class 0 OID 0)
-- Dependencies: 208
-- Name: weapon_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.weapon_id_seq OWNED BY public.weapon.id;


--
-- TOC entry 2816 (class 2604 OID 17105)
-- Name: armor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.armor ALTER COLUMN id SET DEFAULT nextval('public.armor_id_seq'::regclass);


--
-- TOC entry 2814 (class 2604 OID 17090)
-- Name: monster id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster ALTER COLUMN id SET DEFAULT nextval('public.monster_id_seq'::regclass);


--
-- TOC entry 2809 (class 2604 OID 17075)
-- Name: monster_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_type ALTER COLUMN id SET DEFAULT nextval('public.monster_type_id_seq'::regclass);


--
-- TOC entry 2826 (class 2604 OID 17156)
-- Name: player id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player ALTER COLUMN id SET DEFAULT nextval('public.player_id_seq'::regclass);


--
-- TOC entry 2834 (class 2604 OID 17186)
-- Name: player_quest id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_quest ALTER COLUMN id SET DEFAULT nextval('public.player_quest_id_seq'::regclass);


--
-- TOC entry 2822 (class 2604 OID 17135)
-- Name: quest id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.quest ALTER COLUMN id SET DEFAULT nextval('public.quest_id_seq'::regclass);


--
-- TOC entry 2819 (class 2604 OID 17118)
-- Name: weapon id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.weapon ALTER COLUMN id SET DEFAULT nextval('public.weapon_id_seq'::regclass);


--
-- TOC entry 2842 (class 2606 OID 17112)
-- Name: armor armor_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.armor
    ADD CONSTRAINT armor_name_key UNIQUE (name);


--
-- TOC entry 2844 (class 2606 OID 17110)
-- Name: armor armor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.armor
    ADD CONSTRAINT armor_pkey PRIMARY KEY (id);


--
-- TOC entry 2840 (class 2606 OID 17092)
-- Name: monster monster_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster
    ADD CONSTRAINT monster_pkey PRIMARY KEY (id);


--
-- TOC entry 2836 (class 2606 OID 17094)
-- Name: monster_type monster_type_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_type
    ADD CONSTRAINT monster_type_name_key UNIQUE (name);


--
-- TOC entry 2838 (class 2606 OID 17084)
-- Name: monster_type monster_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_type
    ADD CONSTRAINT monster_type_pkey PRIMARY KEY (id);


--
-- TOC entry 2854 (class 2606 OID 17167)
-- Name: player player_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_pkey PRIMARY KEY (id);


--
-- TOC entry 2858 (class 2606 OID 17188)
-- Name: player_quest player_quest_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_quest
    ADD CONSTRAINT player_quest_pkey PRIMARY KEY (id);


--
-- TOC entry 2860 (class 2606 OID 17190)
-- Name: player_quest player_quest_player_id_quest_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_quest
    ADD CONSTRAINT player_quest_player_id_quest_id_key UNIQUE (player_id, quest_id);


--
-- TOC entry 2856 (class 2606 OID 17169)
-- Name: player player_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_username_key UNIQUE (username);


--
-- TOC entry 2850 (class 2606 OID 17145)
-- Name: quest quest_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.quest
    ADD CONSTRAINT quest_name_key UNIQUE (name);


--
-- TOC entry 2852 (class 2606 OID 17143)
-- Name: quest quest_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.quest
    ADD CONSTRAINT quest_pkey PRIMARY KEY (id);


--
-- TOC entry 2846 (class 2606 OID 17127)
-- Name: weapon weapon_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.weapon
    ADD CONSTRAINT weapon_name_key UNIQUE (name);


--
-- TOC entry 2848 (class 2606 OID 17125)
-- Name: weapon weapon_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.weapon
    ADD CONSTRAINT weapon_pkey PRIMARY KEY (id);


--
-- TOC entry 2861 (class 2606 OID 17095)
-- Name: monster monster_monster_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster
    ADD CONSTRAINT monster_monster_type_id_fkey FOREIGN KEY (monster_type_id) REFERENCES public.monster_type(id) NOT VALID;


--
-- TOC entry 2864 (class 2606 OID 17175)
-- Name: player player_armor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_armor_id_fkey FOREIGN KEY (armor_id) REFERENCES public.armor(id) NOT VALID;


--
-- TOC entry 2865 (class 2606 OID 17191)
-- Name: player_quest player_quest_player_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_quest
    ADD CONSTRAINT player_quest_player_id_fkey FOREIGN KEY (player_id) REFERENCES public.player(id) NOT VALID;


--
-- TOC entry 2866 (class 2606 OID 17196)
-- Name: player_quest player_quest_quest_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_quest
    ADD CONSTRAINT player_quest_quest_id_fkey FOREIGN KEY (quest_id) REFERENCES public.quest(id) NOT VALID;


--
-- TOC entry 2863 (class 2606 OID 17170)
-- Name: player player_weapon_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_weapon_id_fkey FOREIGN KEY (weapon_id) REFERENCES public.weapon(id) NOT VALID;


--
-- TOC entry 2862 (class 2606 OID 17146)
-- Name: quest quest_monster_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.quest
    ADD CONSTRAINT quest_monster_type_id_fkey FOREIGN KEY (monster_type_id) REFERENCES public.monster_type(id) NOT VALID;


-- Completed on 2021-01-26 17:06:30

--
-- PostgreSQL database dump complete
--

-- Initialize DB with default data
INSERT INTO public.monster_type ("id", "name", "hp_max", "damage", "xp_value", "gold_value") VALUES
    (1, 'rat', 3, 1, 3, 1),
    (2, 'spider', 4, 2, 4, 2),
    (3, 'wolf', 7, 5, 6, 6),
    (4, 'dragon', 50, 14, 48, 48);

INSERT INTO public.monster("id", "monster_type_id", "hp") VALUES
    (1, 1, 3),
    (2, 1, 3),
    (3, 1, 3),
    (4, 2, 4),
    (5, 2, 4),
    (6, 3, 7),
    (7, 4, 50);