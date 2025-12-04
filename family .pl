parent(john, bill).
parent(linda, bill).
parent(john, alice).
parent(linda, alice).
parent(bill, bob).
parent(alice, sue).
parent(tom, marry).
parent(susan, marry).
parent(bob, sam).

male(john).
male(bill).
male(bob).
male(tom).
male(sam).

female(linda).
female(alice).
female(sue).
female(marry).
female(susan).

father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
grandfather(X, Y) :- grandparent(X, Y), male(X).
grandmother(X, Y) :- grandparent(X, Y), female(X).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
brother(X, Y) :- sibling(X, Y), male(X).
sister(X, Y) :- sibling(X, Y), female(X).
uncle(X, Y) :- brother(X, Z), parent(Z, Y).