DROP TABLE IF EXISTS national_assembly;
CREATE TABLE IF NOT EXISTS national_assembly (
  province TEXT,
  constituency TEXT,
  name TEXT,
  gender NCHAR(1),
  party TEXT,
  votes INTEGER,
  PRIMARY KEY (constituency, name)
);