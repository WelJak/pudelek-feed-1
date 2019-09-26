--SCRIPT WHICH INITIALISE pudelekfeed DATABASE
CREATE TABLE entries (
    uuid varchar PRIMARY KEY ,
    type varchar NOT NULL ,
    entry_id varchar NOT NULL ,
    add_date varchar NOT NULL ,
    title varchar NOT NULL ,
    description varchar NOT NULL ,
    tags varchar NOT NULL ,
    link varchar NOT NULL

);