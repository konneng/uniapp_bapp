
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  uid TEXT UNIQUE NOT NULL,
  email TEXT
);

CREATE TABLE IF NOT EXISTS devices (
  id SERIAL PRIMARY KEY,
  owner_uid TEXT REFERENCES users(uid),
  mac_address TEXT UNIQUE NOT NULL,
  alias_personal TEXT,
  alias_public TEXT,
  type TEXT,
  connection TEXT,
  battery INTEGER,
  last_seen_gps TEXT,
  registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ownership_requests (
  id SERIAL PRIMARY KEY,
  device_id INTEGER REFERENCES devices(id),
  from_uid TEXT,
  to_uid TEXT,
  status TEXT DEFAULT 'pending',
  requested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  responded_at TIMESTAMP
);
