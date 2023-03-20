function getUrlParamValues(url) {
  const regex = /[\?|\&][\w,.]+\=\w+/g
  return url.match(regex).map(couple => couple.split('=')[1])
}

const sampleUrls = [
  'http://example.com?param=value',
  'https://retosdeprogramacion.com?year=2023&challenge=0',
  'https://www.youtube.com/watch?v=zj14pKjAETw',
  'https://swapi.dev/api/people/?search=r2',
  'https://fonts.google.com/icons?icon.query=s',
  'http://example.com?param=value&param2=hello&next=js&good=bye'
]

for(const url of sampleUrls) {
  console.log(`${url} => ${getUrlParamValues(url)}`)
}