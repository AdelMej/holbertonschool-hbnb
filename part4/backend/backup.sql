PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (
	email VARCHAR(120) NOT NULL, 
	first_name VARCHAR(60) NOT NULL, 
	last_name VARCHAR(60) NOT NULL, 
	password VARCHAR(128) NOT NULL, 
	is_admin BOOLEAN, 
	id VARCHAR(36) NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email)
);
INSERT INTO users VALUES('admin@email.com','adel','mej','$2b$12$fwLE.TwA/cKsLtpZ3/9XDutqb3uS.fpsptoAt9iuctu4Lj5i3IsmS',1,'1','2025-11-13 13:04:33','2025-11-13 13:04:33');
INSERT INTO users VALUES('test@test.com','jean','claude','$2b$12$0sZFIq7O0tE87ajaiUuDdezhPZ7MrXQGtVTrBQmC1hSoqmqwHDa8u',0,'234d760e-1339-4263-9d33-0192ef47e81c','2025-11-13 13:04:41.918434','2025-11-13 13:04:41.918552');
INSERT INTO users VALUES('review@gmail.com','reviewtester','lolz','$2b$12$jkGX0jXWvqtOtgHtkVNd2uYRV4t0x1kZt10AlYet2zOOMbvmhUBF2',0,'44a23175-2c3e-4b25-96c2-d630f8e5df51','2025-11-13 14:30:41.532176','2025-11-13 14:30:41.532289');
CREATE TABLE amenities (
	name VARCHAR(50) NOT NULL, 
	id VARCHAR(36) NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO amenities VALUES('sus','75d16869-0f2d-4354-b751-1c248f1e833e','2025-11-13 13:47:13.115235','2025-11-13 14:30:41.532290');
CREATE TABLE places (
	title VARCHAR(100) NOT NULL, 
	description TEXT NOT NULL, 
	price FLOAT NOT NULL, 
	latitude FLOAT NOT NULL, 
	longitude FLOAT NOT NULL, 
	rooms INTEGER NOT NULL, 
	surface INTEGER NOT NULL, 
	capacity INTEGER NOT NULL, 
	owner_id VARCHAR NOT NULL, 
	id VARCHAR(36) NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owner_id) REFERENCES users (id)
);
INSERT INTO places VALUES('rando appart','some random appart',200.0,0.0,0.0,2,3,24,'234d760e-1339-4263-9d33-0192ef47e81c','f2c2c50f-4890-4b05-91aa-d659d85cb2d2','2025-11-13 13:04:41.918434','2025-11-13 13:04:41.918552');
INSERT INTO places VALUES('abcde','string',300.0,23.0,45.0,2,20,12,'234d760e-1339-4263-9d33-0192ef47e81c','f5f055f8-ae04-4940-b991-9684aa18a1c6','2025-11-13 14:15:40.165937','2025-11-13 14:26:28.270384');
CREATE TABLE place_amenity (
	place_id VARCHAR NOT NULL, 
	amenity_id VARCHAR NOT NULL, 
	PRIMARY KEY (place_id, amenity_id), 
	FOREIGN KEY(place_id) REFERENCES places (id), 
	FOREIGN KEY(amenity_id) REFERENCES amenities (id)
);
CREATE TABLE reviews (
	title VARCHAR(50) NOT NULL, 
	user_id VARCHAR NOT NULL, 
	place_id VARCHAR NOT NULL, 
	id VARCHAR(36) NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id), 
	FOREIGN KEY(place_id) REFERENCES places (id)
);
INSERT INTO reviews VALUES('pure luxury','44a23175-2c3e-4b25-96c2-d630f8e5df51','f5f055f8-ae04-4940-b991-9684aa18a1c6','575b9e3e-7d74-4391-a873-0b0513ee1654','2025-11-13 14:50:16.736415','2025-11-13 14:50:16.736544');
COMMIT;
