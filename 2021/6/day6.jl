# Not an original idea.  Borrowed from a matlab solution in the Reddit solutions thread.
# Writing a julia version here to try it out.  Some sort of Markov Chain thing?  Needs research.

data = parse.(Int, split(readline(open("day6.txt")), ','))

fish_by_age = [count(i -> i == x, data) for x in 0:8]
# rotate the matrix each step.  Almost cyclic (m^9 == m), except for the labeled entry
state_transition = [
    0 1 0 0 0 0 0 0 0;
    0 0 1 0 0 0 0 0 0;
    0 0 0 1 0 0 0 0 0;
    0 0 0 0 1 0 0 0 0;
    0 0 0 0 0 1 0 0 0;
    0 0 0 0 0 0 1 0 0;
    1 0 0 0 0 0 0 1 0; # fish on day 6 'come from' fish on day 0
    0 0 0 0 0 0 0 0 1;
    1 0 0 0 0 0 0 0 0
]
println(sum(state_transition^80 * fish_by_age))
println(sum(state_transition^256 * fish_by_age))