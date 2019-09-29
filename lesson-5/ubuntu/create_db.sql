create table if not exists users
(
    chat_id   bigint            not null
        constraint users_pk
            primary key,
    username  text,
    full_name text,
    referral  integer,
    id        serial            not null,
    balance   integer default 0 not null
);

alter table users
    owner to postgres;

create unique index if not exists users_id_uindex
    on users (id);