DROP TABLE IF EXISTS polling_stations;
CREATE TABLE IF NOT EXISTS polling_stations (
  ser INTEGER,
  province TEXT,
  district TEXT,
  constituency TEXT,
  local_authority TEXT,
  ward INTEGER,
  polling_station_name TEXT,
  polling_station_code TEXT PRIMARY KEY,
  female INT,
  male INT,
  total INT
);