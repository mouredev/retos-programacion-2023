print("piedra papel tijera  lagarto spock")
local options={"piedra","papel","tijera","lagarto","spock"}
local optionsVictory={
    piedra={"tijera","lagarto"},
    papel={"piedra","spock"},
    tijera={"papel","lagarto"},
    lagarto={"papel","spock"},
    spock={"piedra","tijera"}
}
local PointP1=0
local PointP2=0
local empate=0

local function victory(P1,P2)
    if P1==P2 then
        print("empate")
        empate=empate+1
    elseif optionsVictory[P1][1]==P2 or optionsVictory[P1][2]==P2  then
        print("victoria para P1")
        PointP1=PointP1+1
    else
        print("victoria para P2")
        PointP2=PointP2+1
    end
    print("PointsP1: "..PointP1)
    print("PointsP2: "..PointP2)
    print("empates: "..empate)
end

for i = 1, 100, 1 do
    print(math.randomseed(i*os.time()).."time")
    local P1=options[math.random(1,5)]
    local P2=options[math.random(1,5)]
    print("P1 escoge: ".. P1 .. " y el P2 escoge: ".. P2 )
    victory(P1,P2)
    
end

print("-------------------------------------------------------------------------------")
print("PointsP1: "..PointP1)
print("PointsP2: "..PointP2)
print("empates: "..empate)