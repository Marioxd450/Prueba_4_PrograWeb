const btnCargar = document.getElementById('#btn-cargar');
const divPeliculas = document.getElementById('#peliculas');

const url = 'http://www.omdbapi.com/?i=tt3896198&apikey=f3939c1c';
//   var image_url = 'http://img.omdbapi.com/?i=tt3896198&apikey=f3939c1c';
btnCargar.addEventListener('click', async function (event) {
  event.preventDefault();

  const resp = await fetch(url).then((resp) => resp.json());
  console.log(resp);

  const { Title, Poster, Genre, Runtime } = resp;

  const titleParraft = document.createElement('p');
  const genreParraft = document.createElement('p');
  const runtimeParraft = document.createElement('p');
  const image = document.createElement('img');
  const br = document.createElement('br');
  titleParraft.textContent = 'Titulo de la pelicula :' + Title;
  genreParraft.textContent = 'Genero de la pelicula :' + Genre;
  runtimeParraft.textContent = 'Duracion de la pelicula :' + Runtime;

  image.src = Poster;

  divPeliculas.append(titleParraft);
  divPeliculas.append(br);
  divPeliculas.append(genreParraft);
  divPeliculas.append(br);
  divPeliculas.append(runtimeParraft);
  divPeliculas.append(br);
  divPeliculas.append(image);
});
