const form = document.querySelector('#searchForm');
const input = document.querySelector('#query');
const resultsDiv = document.querySelector('#results');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const value = input.value;

  const response = await fetch(`https://api.tvmaze.com/search/shows?q=${value}`);
  const data = await response.json();

  console.log(data);

  resultsDiv.innerHTML = '';

  for (const tvShow of data) {
    const article = document.createElement('article');

    const name = document.createElement('h2');
    name.textContent = tvShow.show.name;

    const link = document.createElement('a');
    link.href = tvShow.show.url;
    link.target = '_blank';
    link.textContent = 'View details';

    const image = document.createElement('img');
    image.src = tvShow.show.image?.medium || '';
    image.alt = tvShow.show.name;

    const summary = document.createElement('div');
    summary.innerHTML = tvShow.show.summary || '';

    article.appendChild(name);
    article.appendChild(link);
    article.appendChild(image);
    article.appendChild(summary);

    resultsDiv.appendChild(article);
  }
});