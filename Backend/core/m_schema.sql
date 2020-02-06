CREATE TABLE if not exists users(--user information, and their votes also
    user_id serial PRIMARY KEY,
    email text NOT NULL,
    pass_word text,
    first_name text NOT NULL,
    last_name text NOT NULL,
    vote_id int NOT NULL,
    attending boolean
);

CREATE TABLE if not exists poll( --only has movie objects
    movie_id serial PRIMARY KEY,
    movie_title text,
    movie_details json,
    votes int not null,
    to_show  boolean
);

CREATE TABLE if not exists events(--actual event
    events_id serial PRIMARY KEY,
    dates   character(10),
    selected_movie int references poll(movie_id),
    attendees int[]
);
