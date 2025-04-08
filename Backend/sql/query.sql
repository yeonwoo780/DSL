CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT exists vector;

DROP TABLE IF EXISTS public.langchain_pg_embedding;
DROP table IF EXISTS public.langchain_pg_collection;
DROP TABLE IF EXISTS public.user_info;
DROP TABLE IF EXISTS public.user_model_info;
DROP TABLE IF EXISTS public.gen_model_info;
DROP TABLE IF EXISTS public.search_model_info;

CREATE TABLE public.langchain_pg_collection (
    uuid uuid NOT NULL,
    name character varying,
    cmetadata json,
    PRIMARY KEY (uuid)
);

CREATE TABLE public.langchain_pg_embedding (
    uuid uuid NOT NULL,
    collection_id uuid,
    embedding public.vector,
    document character varying,
    cmetadata jsonb,
    custom_id character varying,
    PRIMARY KEY (uuid),
    FOREIGN KEY(collection_id) REFERENCES langchain_pg_collection (uuid) ON DELETE CASCADE
);

CREATE TABLE public.user_info(
    id serial primary key,
    uid varchar(128),
    email varchar(256),
    password varchar(256)
);

CREATE TABLE public.user_model_info(
    id serial primary key,
    uid varchar(128),
    email varchar(256),
    g_model_name varchar(256),
    api_key varchar(256)
);

CREATE TABLE public.gen_model_info(
    id serial primary key,
    g_model_name varchar(256)
);

CREATE TABLE public.search_model_info(
    id serial primary key,
    s_model_name varchar(256)
);