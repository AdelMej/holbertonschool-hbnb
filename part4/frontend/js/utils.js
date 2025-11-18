export const Cookie = {
	set: (name, value, days = 1) => {
		const maxAge = days * 24 * 60 * 60;
		document.cookie =
			`${encodeURIComponent(name)}=${encodeURIComponent(value)};` +
			` path=/; max-age=${maxAge}; samesite=strict`;
	},
	get: (name) => {
		const value = `; ${document.cookie}`;
		const parts = value.split(`; ${name}=`);
		if (parts.length === 2) return parts.pop().split(";").shift();
		return null;
	},
	delete: (name) => {
		document.cookie = `${name}=; path=/; max-age=0`;
	}
};
