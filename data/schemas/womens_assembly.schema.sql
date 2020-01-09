DROP TABLE IF EXISTS womens_assembly;
CREATE TABLE IF NOT EXISTS womens_assembly (
  province TEXT,
  ser INTEGER,
  name TEXT,
  gender NCHAR(1),
  party TEXT,
  PRIMARY KEY(ser, province)
);