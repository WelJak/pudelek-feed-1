--SCRIPT WHICH INITIALISE pudelekfeed DATABASE FK6c6b4ige2mhlafoty7tye1ku5

create table news (uuid varchar(255) not null,
                    description varchar(255) not null,
                    entryid varchar(255) not null,
                    link varchar(255) not null,
                    post_date varchar(255) not null,
                    title varchar(255) not null,
                    type varchar(255) not null,
                    was_sent boolean,
                    primary key (uuid))

create table tags (id  bigserial not null,
                    tag varchar(255) not null,
                    uuid varchar(255),
                    primary key (id))

alter table if exists tags add constraint tags_uuid_unq foreign key (uuid) references news