'use strict';

function parameterValues(url) {
  const queryStart = String(url).indexOf('?');
  if (queryStart === -1) return [];
  const fragmentStart = String(url).indexOf('#', queryStart);
  const query = String(url).slice(queryStart + 1, fragmentStart === -1 ? undefined : fragmentStart);
  if (!query) return [];
  return query.split('&').filter(Boolean).map(parameter => {
    const separator = parameter.indexOf('=');
    const value = separator === -1 ? '' : parameter.slice(separator + 1);
    return decodeURIComponent(value.replace(/\+/g, ' '));
  });
}

module.exports = { parameterValues };

if (require.main === module) {
  console.log(parameterValues(process.argv[2] ?? 'https://retosdeprogramacion.com?year=2023&challenge=0'));
}
