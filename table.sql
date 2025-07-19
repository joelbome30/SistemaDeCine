-- table.sql
DROP TABLE IF EXISTS sillas;

CREATE TABLE sillas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ocupada BOOLEAN NOT NULL DEFAULT 0
);

-- Insertar 34 sillas (todas libres)
INSERT INTO sillas (ocupada) VALUES
    (0),(0),(0),(0),(0),(0),(0),(0),(0),(0),
    (0),(0),(0),(0),(0),(0),(0),(0),(0),(0),
    (0),(0),(0),(0),(0),(0),(0),(0),(0),(0),
    (0),(0),(0),(0);
    
