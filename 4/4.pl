?- use_module(library(clpfd)).

firstpart(Vars) :-
    Vars = [A,B,C,D,E,F],
    Vars ins 0..9,
    F #>= E, E #>= D, D #>= C, C #>= B, B #>= A,
	A*100000 + B*10000 + C*1000 + D*100 + E*10 + F #>= 284639,
    A*100000 + B*10000 + C*1000 + D*100 + E*10 + F #=< 748759,
    (A#=B; B#=C; C#=D;D#=E;E#=F).

% Vars=[A,B,C,D,E,F], firstpart(Vars), label(Vars).

secondpart(Vars):-
    firstpart(Vars),
    findDouble2(Vars,10,CountResult),
    CountResult #>= 1.

% Vars=[A,B,C,D,E,F], secondpart(Vars), label(Vars).

findDouble2([_],_,0).
findDouble2([X,X],Previous,1):-
    X #\= Previous.

findDouble2([X,X,Third|T],Previous,CountResultNew):-
    X #\= Previous,
    X #\= Third,
    findDouble2([Third|T],X,CountResult),
    CountResultNew is CountResult + 1.

findDouble2([X,X,Third],Previous,1):-
    X #\= Previous,
    X #\= Third.

findDouble2([H|T],_,CountResult):-
    findDouble2(T,H,CountResult).

