CREATE TABLE bitcoin (
  id INT NOT NULL AUTO_INCREMENT,
  fecha DATE NOT NULL,
  precio_usd DECIMAL(10,2) NOT NULL,
  precio_gbp DECIMAL(10,2) NOT NULL,
  precio_eur DECIMAL(10,2) NOT NULL,
  precio_pen DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id)
);
