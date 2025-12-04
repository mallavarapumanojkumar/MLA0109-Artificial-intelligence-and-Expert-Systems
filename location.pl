location(chennai,tamilnadu).
location(ongole,andhrapradesh).
location(hyderabad,telengana).


stays(dharma,chennai).
stays(manoj,ongole).
stays(mahesh,hyderaad).

display(Person,City,State):-
  stays(Person,City),
  location(City,State).

state_of_person(Person,State):-
   stays(Person,City),
   location(City,State).
