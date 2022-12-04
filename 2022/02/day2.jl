data = split.(readlines(open("in.txt")))

shapes = Dict(
    "A"=>[1;0;0],
    "B"=>[0;1;0],
    "C"=>[0;0;1],
    "X"=>[1;0;0],
    "Y"=>[0;1;0],
    "Z"=>[0;0;1]
)

resultPoints1 = [3 6 0; # In part 1, we're just playing rock paper scissors
                 0 3 6;
                 6 0 3]
shapePoints1 = [1;2;3]

resultPoints2 = [0;3;6]
shapePoints2 = [3 1 2; # In part 2, we need to determine our throw based on
                1 2 3; # what we want the result to be
                2 3 1]

score1 = (opponent, me) -> opponent' * resultPoints1 * me + shapePoints1' * me
score2 = (opponent, me) -> opponent' * shapePoints2 * me + resultPoints2' * me

opponent = 1
me = 2

p1 = sum(game->score1(shapes[game[opponent]], shapes[game[me]]), data)
p2 = sum(game->score2(shapes[game[opponent]], shapes[game[me]]), data)


println(p1)
println(p2)
