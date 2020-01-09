DROP TABLE IF EXISTS senate;
CREATE TABLE IF NOT EXISTS senate (
  province TEXT,
  ser INTEGER,
  name TEXT,
  gender NCHAR(1),
  party TEXT,
  PRIMARY KEY (province, ser)
);