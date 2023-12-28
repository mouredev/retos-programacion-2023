

function generateKey(length,uppercase,numberscase,symbolscase)
  math.randomseed(os.time())
  local lowcase = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
  local upcase  = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
  local numbers = {"0","1","2","3","4","5","6","7","8","9"}
  local symbols = {"!","#","$","%","&","/","=",".","-",";",",","?","+","*"}
  local base=lowcase
  if uppercase then
    for k,v in pairs(upcase) do table.insert( base, v ) end
  end
  if numberscase then
    for k,v in pairs(numbers) do table.insert( base, v ) end
  end
  if symbolscase then
    for k,v in pairs(symbols) do table.insert( base, v ) end
  end
  local secret = ""
  print(#base)
  for i=1,length do
    secret=secret..base[math.random( 1,#base)]
  end
  return secret
end
l = 8
m,n,b=nil,nil,nil
for i,v in ipairs(arg) do
  if v=="-l" then
    l=arg[i+1]
    if tonumber(l)<8 or tonumber(l)>16 then
      print("Use una longitud -l entre 8 y 16")
      return
    end
  end
  if v=="-m" then
    m=true
  end
  if v=="-n" then
    n=true
  end
  if v=="-s" then
    s=true
  end
end
key = generateKey(l,m,n,s)
print(key)
