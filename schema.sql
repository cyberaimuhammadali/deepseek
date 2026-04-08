-- Supabase SQL editor da ishlating
CREATE TABLE users (
    id BIGINT PRIMARY KEY,
    full_name TEXT,
    phone TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    name_uz TEXT,
    name_ru TEXT,
    price INTEGER,
    duration_min INTEGER,
    image_url TEXT
);

CREATE TABLE masters (
    id SERIAL PRIMARY KEY,
    name TEXT,
    specialty TEXT,
    rating FLOAT,
    photo_url TEXT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES users(id),
    service_id INT REFERENCES services(id),
    master_id INT REFERENCES masters(id),
    booking_time TIMESTAMP,
    status TEXT DEFAULT 'pending', -- pending, confirmed, canceled, completed
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE time_slots (
    id SERIAL PRIMARY KEY,
    master_id INT,
    slot_time TIMESTAMP,
    is_free BOOLEAN DEFAULT TRUE
);
