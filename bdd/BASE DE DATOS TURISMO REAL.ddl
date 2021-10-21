-- Generado por Oracle SQL Developer Data Modeler 21.2.0.183.1957
--   en:        2021-10-20 15:49:45 CLST
--   sitio:      Oracle Database 21c
--   tipo:      Oracle Database 21c



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE SEQUENCE cualidaddep_cualidaddep_id_seq START WITH 1 NOCACHE ORDER;

CREATE SEQUENCE cualidadhab_cualidad_id_seq START WITH 1 NOCACHE ORDER;

CREATE SEQUENCE recepcion_recepcionista_id_seq START WITH 1 NOCACHE ORDER;

CREATE SEQUENCE tour_tour_id_seq START WITH 1 NOCACHE ORDER;

CREATE TABLE acompañante (
    rut         INTEGER NOT NULL,
    cliente_rut INTEGER NOT NULL,
    nombre      VARCHAR2(15),
    apellido    VARCHAR2(15),
    edad        INTEGER,
    telefono    INTEGER
)
LOGGING;

ALTER TABLE acompañante ADD CONSTRAINT acompañante_pk PRIMARY KEY ( rut );

CREATE TABLE admin (
    id          INTEGER NOT NULL,
    usuario     VARCHAR2(12),
    contraseña VARCHAR2(10)
)
LOGGING;

ALTER TABLE admin ADD CONSTRAINT admin_pk PRIMARY KEY ( id );

CREATE TABLE CHECK_IN_OUT (
    folio                      INTEGER NOT NULL,
    check_in                   DATE,
    check_out                  DATE,
    recepcion_recepcionista_id NUMBER NOT NULL
)
LOGGING;

ALTER TABLE CHECK_IN_OUT ADD CONSTRAINT check_pk PRIMARY KEY ( folio );

CREATE TABLE chofer (
    transporte_id INTEGER NOT NULL,
    nombre        VARCHAR2(15),
    licencia      VARCHAR2(15)
)
LOGGING;

ALTER TABLE chofer ADD CONSTRAINT chofer_pk PRIMARY KEY ( transporte_id );

CREATE TABLE clasificacion (
    id                INTEGER NOT NULL,
    clasificacion     VARCHAR2(20),
    habitacion_id_num INTEGER
)
LOGGING;

ALTER TABLE clasificacion ADD CONSTRAINT clasificacion_pk PRIMARY KEY ( id );

CREATE TABLE cliente (
    rut      INTEGER NOT NULL,
    nombre   VARCHAR2(15),
    apellido VARCHAR2(15),
    telefono INTEGER,
    correo   VARCHAR2(25),
    tarjeta  INTEGER,
    clave    VARCHAR2(255)
)
LOGGING;

ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( rut );

CREATE TABLE cualidaddep (
    atributo        VARCHAR2(20),
    inventario      VARCHAR2(20),
    valorizacion    INTEGER,
    imagen          BLOB,
    departamento_id INTEGER NOT NULL,
    cualidaddep_id  NUMBER NOT NULL
)
LOGGING;

ALTER TABLE cualidaddep ADD CONSTRAINT cualidaddep_pk PRIMARY KEY ( cualidaddep_id );

CREATE TABLE cualidadhab (
    atributo           VARCHAR2(20),
    valor              INTEGER,
    imagen             BLOB,
    habitacion_id_num  INTEGER NOT NULL,
    cualidad_id        NUMBER NOT NULL,
    habitacion_id_num1 INTEGER NOT NULL
)
LOGGING;

CREATE UNIQUE INDEX cualidad__idx ON
    cualidadhab (
        habitacion_id_num
    ASC );

ALTER TABLE cualidadhab ADD CONSTRAINT cualidadhab_pk PRIMARY KEY ( cualidad_id );

CREATE TABLE departamento (
    id        INTEGER NOT NULL,
    nombre    VARCHAR2(15),
    direccion VARCHAR2(20),
    telefono  INTEGER,
    admin_id  INTEGER NOT NULL
)
LOGGING;

ALTER TABLE departamento ADD CONSTRAINT departamento_pk PRIMARY KEY ( id );

CREATE TABLE habitacion (
    id_num               INTEGER NOT NULL,
    disponibilidad       NUMBER,
    cliente_rut          INTEGER NOT NULL,
    cualidad_cualidad_id NUMBER NOT NULL,
    admin_id             INTEGER NOT NULL,
    departamento_id      INTEGER NOT NULL
)
LOGGING;

CREATE UNIQUE INDEX habitacion__idx ON
    habitacion (
        cualidad_cualidad_id
    ASC );

ALTER TABLE habitacion ADD CONSTRAINT habitacion_pk PRIMARY KEY ( id_num );

CREATE TABLE mantencion (
    check_folio INTEGER NOT NULL,
    id          INTEGER NOT NULL,
    reparacion  NUMBER,
    mejora      NUMBER,
    dano        NUMBER,
    costo       INTEGER
)
LOGGING;

ALTER TABLE mantencion ADD CONSTRAINT mantencion_pk PRIMARY KEY ( check_folio );

CREATE TABLE recepcion (
    recepcionista_id NUMBER NOT NULL,
    id               INTEGER,
    nombre           VARCHAR2(15),
    apellido         VARCHAR2(15),
    categoria        VARCHAR2(15),
    admin_id         INTEGER NOT NULL
)
LOGGING;

ALTER TABLE recepcion ADD CONSTRAINT recepcion_pk PRIMARY KEY ( recepcionista_id );

CREATE TABLE reserva (
    id                         INTEGER NOT NULL,
    cliente_rut                INTEGER,
    recepcion_recepcionista_id NUMBER NOT NULL,
    pendiente                  NUMBER,
    monto                      INTEGER
)
LOGGING;

ALTER TABLE reserva ADD CONSTRAINT reserva_pk PRIMARY KEY ( id );

CREATE TABLE servicio (
    id               INTEGER NOT NULL,
    transporte_id    INTEGER NOT NULL,
    tour_tour_id     NUMBER NOT NULL,
    clasificacion_id INTEGER NOT NULL,
    departamento_id  INTEGER NOT NULL,
    cliente_rut      INTEGER
)
LOGGING;

ALTER TABLE servicio ADD CONSTRAINT servicio_pk PRIMARY KEY ( id );

CREATE TABLE tour (
    tour_id     NUMBER NOT NULL,
    id          INTEGER,
    nombre      VARCHAR2(15),
    ubicacion   VARCHAR2(20),
    descripcion VARCHAR2(50),
    imagen      BLOB
)
LOGGING;

ALTER TABLE tour ADD CONSTRAINT tour_pk PRIMARY KEY ( tour_id );

CREATE TABLE transaccion (
    id              INTEGER NOT NULL,
    num_transaccion INTEGER,
    check_folio     INTEGER NOT NULL,
    metodo_pago     VARCHAR2(15),
    reserva_id      INTEGER NOT NULL
)
LOGGING;

ALTER TABLE transaccion ADD CONSTRAINT transaccion_pk PRIMARY KEY ( id );

CREATE TABLE transporte (
    id     INTEGER NOT NULL,
    nombre VARCHAR2(15),
    ruta   VARCHAR2(20),
    km     INTEGER
)
LOGGING;

ALTER TABLE transporte ADD CONSTRAINT transporte_pk PRIMARY KEY ( id );

ALTER TABLE acompañante
    ADD CONSTRAINT acompañante_cliente_fk FOREIGN KEY ( cliente_rut )
        REFERENCES cliente ( rut )
    NOT DEFERRABLE;

ALTER TABLE CHECK_IN_OUT
    ADD CONSTRAINT check_recepcion_fk FOREIGN KEY ( recepcion_recepcionista_id )
        REFERENCES recepcion ( recepcionista_id )
    NOT DEFERRABLE;

ALTER TABLE chofer
    ADD CONSTRAINT chofer_transporte_fk FOREIGN KEY ( transporte_id )
        REFERENCES transporte ( id )
    NOT DEFERRABLE;

ALTER TABLE clasificacion
    ADD CONSTRAINT clasificacion_habitacion_fk FOREIGN KEY ( habitacion_id_num )
        REFERENCES habitacion ( id_num )
    NOT DEFERRABLE;

ALTER TABLE cualidaddep
    ADD CONSTRAINT cualidaddep_departamento_fk FOREIGN KEY ( departamento_id )
        REFERENCES departamento ( id )
    NOT DEFERRABLE;

ALTER TABLE cualidadhab
    ADD CONSTRAINT cualidadhab_habitacion_fk FOREIGN KEY ( habitacion_id_num1 )
        REFERENCES habitacion ( id_num )
    NOT DEFERRABLE;

ALTER TABLE departamento
    ADD CONSTRAINT departamento_admin_fk FOREIGN KEY ( admin_id )
        REFERENCES admin ( id )
    NOT DEFERRABLE;

ALTER TABLE habitacion
    ADD CONSTRAINT habitacion_admin_fk FOREIGN KEY ( admin_id )
        REFERENCES admin ( id )
    NOT DEFERRABLE;

ALTER TABLE habitacion
    ADD CONSTRAINT habitacion_cliente_fk FOREIGN KEY ( cliente_rut )
        REFERENCES cliente ( rut )
    NOT DEFERRABLE;

ALTER TABLE habitacion
    ADD CONSTRAINT habitacion_departamento_fk FOREIGN KEY ( departamento_id )
        REFERENCES departamento ( id )
    NOT DEFERRABLE;

ALTER TABLE mantencion
    ADD CONSTRAINT mantencion_check_fk FOREIGN KEY ( check_folio )
        REFERENCES CHECK_IN_OUT ( folio )
    NOT DEFERRABLE;

ALTER TABLE recepcion
    ADD CONSTRAINT recepcion_admin_fk FOREIGN KEY ( admin_id )
        REFERENCES admin ( id )
    NOT DEFERRABLE;

ALTER TABLE reserva
    ADD CONSTRAINT reserva_cliente_fk FOREIGN KEY ( cliente_rut )
        REFERENCES cliente ( rut )
    NOT DEFERRABLE;

ALTER TABLE reserva
    ADD CONSTRAINT reserva_recepcion_fk FOREIGN KEY ( recepcion_recepcionista_id )
        REFERENCES recepcion ( recepcionista_id )
    NOT DEFERRABLE;

ALTER TABLE servicio
    ADD CONSTRAINT servicio_clasificacion_fk FOREIGN KEY ( clasificacion_id )
        REFERENCES clasificacion ( id )
    NOT DEFERRABLE;

ALTER TABLE servicio
    ADD CONSTRAINT servicio_cliente_fk FOREIGN KEY ( cliente_rut )
        REFERENCES cliente ( rut )
    NOT DEFERRABLE;

ALTER TABLE servicio
    ADD CONSTRAINT servicio_departamento_fk FOREIGN KEY ( departamento_id )
        REFERENCES departamento ( id )
    NOT DEFERRABLE;

ALTER TABLE servicio
    ADD CONSTRAINT servicio_tour_fk FOREIGN KEY ( tour_tour_id )
        REFERENCES tour ( tour_id )
    NOT DEFERRABLE;

ALTER TABLE servicio
    ADD CONSTRAINT servicio_transporte_fk FOREIGN KEY ( transporte_id )
        REFERENCES transporte ( id )
    NOT DEFERRABLE;

ALTER TABLE transaccion
    ADD CONSTRAINT transaccion_check_fk FOREIGN KEY ( check_folio )
        REFERENCES CHECK_IN_OUT ( folio )
    NOT DEFERRABLE;

ALTER TABLE transaccion
    ADD CONSTRAINT transaccion_reserva_fk FOREIGN KEY ( reserva_id )
        REFERENCES reserva ( id )
    NOT DEFERRABLE;

CREATE OR REPLACE TRIGGER cualidaddep_cualidaddep_id_trg BEFORE
    INSERT ON cualidaddep
    FOR EACH ROW
    WHEN ( new.cualidaddep_id IS NULL )
BEGIN
    :new.cualidaddep_id := cualidaddep_cualidaddep_id_seq.nextval;
END;
/

CREATE OR REPLACE TRIGGER cualidadhab_cualidad_id_trg BEFORE
    INSERT ON cualidadhab
    FOR EACH ROW
    WHEN ( new.cualidad_id IS NULL )
BEGIN
    :new.cualidad_id := cualidadhab_cualidad_id_seq.nextval;
END;
/

CREATE OR REPLACE TRIGGER recepcion_recepcionista_id_trg BEFORE
    INSERT ON recepcion
    FOR EACH ROW
    WHEN ( new.recepcionista_id IS NULL )
BEGIN
    :new.recepcionista_id := recepcion_recepcionista_id_seq.nextval;
END;
/

CREATE OR REPLACE TRIGGER tour_tour_id_trg BEFORE
    INSERT ON tour
    FOR EACH ROW
    WHEN ( new.tour_id IS NULL )
BEGIN
    :new.tour_id := tour_tour_id_seq.nextval;
END;
/



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            17
-- CREATE INDEX                             2
-- ALTER TABLE                             38
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           4
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          4
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
