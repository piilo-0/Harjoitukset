const form = document.querySelector("form");
const input = document.querySelector("#query");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const value = input.value;

  const response = await fetch(`https://api.tvmaze.com/search/shows?q=${value}`);
  const data = await response.json();

  console.log(data);
});