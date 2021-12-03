data = parse.(Int, readlines(open("day1.txt")))

part1 = sum(data[i-1] < data[i] for i in 2:length(data))
part2 = sum(data[i-3] < data[i] for i in 4:length(data))

println(part1)
println(part2)