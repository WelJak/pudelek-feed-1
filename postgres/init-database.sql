--SCRIPT WHICH INITIALISE pudelekfeed DATABASE
CREATE TABLE news (
    uuid varchar PRIMARY KEY UNIQUE NOT NULL ,
    type varchar NOT NULL ,
    entry_id varchar NOT NULL UNIQUE ,
    add_date varchar NOT NULL ,
    title varchar NOT NULL ,
    description varchar NOT NULL ,
    tags varchar NOT NULL ,
    link varchar NOT NULL

);