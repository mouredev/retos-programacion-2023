'use strict';

function decodeHtml(text) {
  const entities = { '&amp;': '&', '&quot;': '"', '&#39;': "'", '&lt;': '<', '&gt;': '>', '&nbsp;': ' ' };
  return text.replace(/&(?:amp|quot|#39|lt|gt|nbsp);/g, entity => entities[entity]);
}

function parseAgenda(html) {
  const lines = decodeHtml(String(html)
    .replace(/<(?:br|\/p|\/div|\/li|\/h\d)>/gi, '\n')
    .replace(/<[^>]+>/g, ' '))
    .split(/\r?\n/)
    .map(line => line.replace(/\s+/g, ' ').trim())
    .filter(Boolean);
  const events = [];
  for (let index = 0; index < lines.length; index++) {
    const match = lines[index].match(/\b([01]\d|2[0-3]):[0-5]\d\b/);
    if (!match) continue;
    let description = lines[index].slice(match.index + match[0].length).replace(/^[\s|–—:-]+/, '');
    if (!description && lines[index + 1]) description = lines[++index];
    const event = `${match[0]} | ${description}`;
    if (description && !events.includes(event)) events.push(event);
  }
  return events;
}

async function scrapeAgenda(fetchImplementation = globalThis.fetch) {
  const response = await fetchImplementation('https://holamundo.day');
  if (!response.ok) throw new Error(`La web respondió con ${response.status}`);
  return parseAgenda(await response.text());
}

module.exports = { parseAgenda, scrapeAgenda };

if (require.main === module) scrapeAgenda().then(events => events.forEach(console.log)).catch(console.error);
