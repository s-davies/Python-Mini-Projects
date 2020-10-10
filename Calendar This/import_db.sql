DROP TABLE IF EXISTS appointments;

create table appointments
(
    id serial PRIMARY KEY,
    name varchar(200) not null,
    start_datetime timestamp not null,
    end_datetime timestamp not null,
    description text not null,
    private boolean not null
);

insert into appointments
    (name, start_datetime, end_datetime, description, private)
values
    ('My appointment', '2020-10-10 14:00:00', '2020-10-10 15:00:00',
 'An appointment for me', false);