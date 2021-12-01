var data = File.ReadLines(@"c:\projects\AdventOfCode\2021\1\day1.txt")
    .Select(line => int.Parse(line.Trim()))
    .ToList();

var part1 = (List<int> data) => data
    .Select((x, i) => x < data[i+1] ? 1 : 0)
    .Take(data.Count - 1)
    .Sum();

var part2 = (List<int> data) => data
    .Select((x, i) => x < data[i+3] ? 1 : 0)
    .Take(data.Count - 3)
    .Sum();

Console.WriteLine(part1(data));
Console.WriteLine(part2(data));