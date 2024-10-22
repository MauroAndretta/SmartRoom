replace_existing_fact(OldFact, NewFact) :-
    call(OldFact), 
    !,
    retract(OldFact),
    assertz(NewFact).


remove_existing_fact(OldFact) :-
    call(OldFact), 
    retract(OldFact).


%outside(Id).
outside(Id) :- 
	\+ inside(Id).


%setInsideActuators(Actuators, Value).
setInsideActuators([H|T], Y) :-
    extractInsideActuators([H|T], [], L),
    setActuators(L, Y).

%setOutsideActuators(Actuators, Value).
setOutsideActuators([H|T], Y) :-
    extractOutsideActuators([H|T], [], L),
    setActuators(L, Y).

%setActuators(Actuators, Value).
setActuators([H|T], Y) :-
    T \== [],
    !,
    setActuators(T, Y),
	replace_existing_fact(actuatorValue(H,_), actuatorValue(H, Y)).

setActuators([H|_], Y) :-
    !,
	replace_existing_fact(actuatorValue(H,_), actuatorValue(H, Y)).

setActuators(_, _).
    

%extractInsideActuators(List, NewList, variable).
extractInsideActuators([H|T], L,X) :-
    T \== [],
    inside(H),
    !,
    extractInsideActuators(T, [H|L], X).

extractInsideActuators([H|T], L, X) :-
    T\== [],
    \+ inside(H),
    !,
    extractInsideActuators(T, L, X).

extractInsideActuators([H|_], L,X) :-
    \+ inside(H),
    !,
    X = L.

extractInsideActuators([H|_], L, X) :-
    inside(H),
    !,
    X = [H|L].

extractInsideActuators(_, L, X) :-
    X = L.
 

%extractOutsideActuators(List, NewList, variable).
extractOutsideActuators([H|T], L,X) :-
    T \== [],
    outside(H),
    !,
    extractOutsideActuators(T, [H|L], X).

extractOutsideActuators([H|T], L, X) :-
    T\== [],
    \+ outside(H),
    !,
    extractOutsideActuators(T, L, X).

extractOutsideActuators([H|_], L,X) :-
    \+ outside(H),
    !,
    X = L.

extractOutsideActuators([H|_], L, X) :-
    outside(H),
    !,
    X = [H|L].

extractOutsideActuators(_, L, X) :-
    X = L.

%set(PIId).
set(PIId) :-  set(PIId, _).

%set(PIId, TypeId).
set(PIId, light) :- 
    sensor(SensorId_outside, light),
    outside(SensorId_outside),
    sensorValue(SensorId_outside, X),
    preferencesInstance(PIId, light, Y, Actuators),
    X >= Y,
	setOutsideActuators(Actuators, Y),
	setInsideActuators(Actuators, 0).
    
set(PIId, light) :- 
    sensor(SensorId_outside, light),
    outside(SensorId_outside),
    sensorValue(SensorId_outside, X),
    preferencesInstance(PIId, light, Y, Actuators),
    X < Y,
	setOutsideActuators(Actuators, 0),
	setInsideActuators(Actuators, Y).


set(PIId, temp) :-
    preferencesInstance(PIId, temp, Y, Actuators),
    sensor(SensorId_outside, temp),
    outside(SensorId_outside),
    sensorValue(SensorId_outside, X_outside),
    sensor(SensorId_inside, temp),
    inside(SensorId_inside),
    sensorValue(SensorId_inside, X_inside),
    X_inside < Y,
    X_outside > Y,
	setOutsideActuators(Actuators, Y),
	setInsideActuators(Actuators, 0).

set(PIId, temp) :-
    preferencesInstance(PIId, temp, Y, Actuators),
    sensor(SensorId_outside, temp),
    outside(SensorId_outside),
    sensorValue(SensorId_outside, X_outside),
    sensor(SensorId_inside, temp),
    inside(SensorId_inside),
    sensorValue(SensorId_inside, X_inside),
    X_inside < Y,
    X_outside < Y,
	setOutsideActuators(Actuators, 0),
	setInsideActuators(Actuators, Y).

set(PIId, temp) :-
    preferencesInstance(PIId, temp, Y, Actuators),
    sensor(SensorId_outside, temp),
    outside(SensorId_outside),
    sensorValue(SensorId_outside, X_outside),
    sensor(SensorId_inside, temp),
    inside(SensorId_inside),
    sensorValue(SensorId_inside, X_inside),
    X_inside > Y,
    X_outside > Y,
	setOutsideActuators(Actuators, 0),
	setInsideActuators(Actuators, Y).

set(PIId, temp) :-
    preferencesInstance(PIId, temp, Y, Actuators),
    sensor(SensorId_outside, temp),
    outside(SensorId_outside),
    sensorValue(SensorId_outside, X_outside),
    sensor(SensorId_inside, temp),
    inside(SensorId_inside),
    sensorValue(SensorId_inside, X_inside),
    X_inside > Y,
    X_outside < Y,
	setOutsideActuators(Actuators, Y),
	setInsideActuators(Actuators, 0).

set(PIId, noise) :-
    preferencesInstance(PIId, noise, Y_noise, Actuators),
    sensor(SensorId_outside, noise),
    outside(SensorId_outside),
    sensorValue(SensorId_outside, X_noise_outside),
    X_noise_outside > Y_noise,
    sensor(SensorId_inside, temp),
    inside(SensorId_inside),
    sensorValue(SensorId_inside, X_temp_inside),
    preferencesInstance(PIId, temp, Y_temp, Actuators),
    X_temp_inside \== Y_temp,
    setOutsideActuators(Actuators, 0),
    setInsideActuators(Actuators, Y_temp).

%memberCheck(Element, List).
memberCheck(H,[H|_]).
memberCheck(H,[_|T]) :- memberCheck(H,T).