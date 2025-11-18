import { Cookie } from "./utils.js"

document.addEventListener('DOMContentLoaded', () => {
	document.getElementById("login-form").addEventListener("submit", (event) => {
		event.preventDefault();
		const fd = new FormData(document.getElementById("login-form"))

		authentication(fd.get("email"), fd.get("password"));
	})
});

async function authentication(email, password) {
	try {
		const response = await fetch("http://localhost:5000/api/v1/auth/login",
			{
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ email, password })
			})
		if (!response.ok) {
			if (response.status === 401) {
				const data = await response.json()
				window.alert(data.error);
				return;
			}
			else {
				return;
			}
		}
		const data = await response.json();
		Cookie.set("token", data.access_token, 1);
		window.location.replace("/index.html")
	} catch (err) {
		console.error("Error: ", err)
	}
}
