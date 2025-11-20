export class FetchPlace {
	constructor(id) {
		this.id = id;
		this.data = null;
		this.error = null;
	}

	async load() {
		try {
			if (!this.id) {
				this.error = "Where id?";
				return null;
			}
			const response = await fetch("http://127.0.0.1:5000/api/v1/places/" + this.id)

			if (!response.ok) {
				this.error = "HTTP " + response.status;
				return null;
			}

			this.data = await response.json();
			return this.data;

		} catch (err) {
			this.error = err;
			return null;
		}
	}

	getId() { return this.data?.id ?? null };
	getTitle() { return this.data?.title ?? null };
	getPrice() { return this.data?.price ?? null };
	getDescription() { return this.data?.description ?? null };
	getLatitude() { return this.data?.latitude ?? null };
	getLongitude() { return this.data?.longitude ?? null };
	getAmenities() { return this.data?.amenities ?? null };
	getRooms() { return this.data?.rooms ?? null };
	getSurface() { return this.data?.surface ?? null };
	getCapacity() { return this.data?.capacity ?? null };
	getOwner() { return this.data?.owner ?? null };
}
