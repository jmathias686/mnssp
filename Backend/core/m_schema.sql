CREATE TABLE users(--user information, and their votes also
    userID serial PRIMARY KEY,
    email text NOT NULL,
    pass text not null,
    first_name text NOT NULL,
    last_name text NOT NULL,
    vote_id int NOT NULL,
    dining_order text
)

CREATE TABLE events(--actual event
    eventsID serial PRIMARY KEY,
    dates   character(10),
    selected_movie references poll(movieID),
    movie_goers int[],
    dining_goers int []
);

CREATE TABLE poll( --only has movie objects
    movieID serial PRIMARY KEY,
    movie_details   json
);
