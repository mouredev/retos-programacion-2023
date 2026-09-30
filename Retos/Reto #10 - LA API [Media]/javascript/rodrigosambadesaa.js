'use strict';

async function getPokemon(name, fetchImplementation = globalThis.fetch) {
  if (typeof fetchImplementation !== 'function') throw new Error('Fetch no está disponible');
  const response = await fetchImplementation(`https://pokeapi.co/api/v2/pokemon/${encodeURIComponent(String(name).toLowerCase())}`);
  if (!response.ok) throw new Error(`La API respondió con ${response.status}`);
  const pokemon = await response.json();
  return {
    id: pokemon.id,
    name: pokemon.name,
    types: pokemon.types.map(item => item.type.name)
  };
}

module.exports = { getPokemon };

if (require.main === module) getPokemon(process.argv[2] ?? 'pikachu').then(console.log).catch(console.error);
