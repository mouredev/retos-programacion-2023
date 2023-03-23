simbols={
  a="4",
  b="13",
  c="<",
  d="cl",
  e="3",
  f="/=",
  g="(_+",
  h="#",
  i="!",
  j="._]",
  k="/<",
  l="|",
  m="[V]",
  n="[\\]",
  o="0",
  p="|>",
  q="<|",
  r="/2",
  s="2",
  t="']['",
  u="(_)",
  v="\\/",
  w="VV",
  x="><",
  y="`/",
  z="%",
}
print("Enter your text")
t=io.read()
code = ""
for c in t:gmatch"." do
  local simbol
  if c==" " then
    simbol=" "
  else
    simbol = simbols[c]
  end
  if not simbol == nil then
    code = code..simbol
  end
end
print (code)