replace_existing_fact(OldFact, NewFact) :-
    call(OldFact), 
    !,
    retract(OldFact),
    assertz(NewFact).


remove_existing_fact(OldFact) :-
    call(OldFact), 
    retract(OldFact).

%propertyType(TypeId).
propertyType(light).
propertyType(temp).
propertyType(noise).

%sensor(SensorId, TypeId).
:-dynamic(sensor/2).
sensor(brightness, light).
sensor(brightness_outside, light).
sensor(temperature, temp).
sensor(temperature_outside, temp).
sensor(outside_noise, noise).


%sensorValue(SensorId, Value).
:-dynamic(sensorValue/2).
sensorValue(brightness, 0).
sensorValue(brightness_outside, 0).
sensorValue(temperature, 10).
sensorValue(temperature_outside, 8).
sensorValue(outside_noise, 20).


%actuator(ActuatorId, TypeId).
:-dynamic(actuator/2).
actuator(X, noise) :-
    actuator(X, temp).
actuator(light_desk, light).
actuator(mainLight, light).
actuator(cornerLight, light).
actuator(ac, temp).
actuator(window, temp).
actuator(roller_shutter, light).



%inside(Id).
:-dynamic(inside/1).
inside(brightness).
inside(temperature).
inside(desk).
inside(bed).
inside(chair_desk).
inside(light_desk).
inside(mainLight).
inside(cornerLight).
inside(ac).

%outside(Id).
outside(Id) :- 
	\+ inside(Id).

%actuatorValue(ActuatorId, Value).
:-dynamic(actuatorValue/2).
actuatorValue(light_desk, 0).
actuatorValue(mainLight, 0).
actuatorValue(cornerLight, 0).
actuatorValue(ac, 0).
actuatorValue(window, 0).
actuatorValue(roller_shutter, 0).


%preferencesInstance(PiiD, TypeId, ExpectedValueSensor, Actuators).
:-dynamic(preferencesInstance/4).
preferencesInstance(nullPreference, _, 0, []).
preferencesInstance(study, light, 20, [light_desk, mainLight,roller_shutter]).
preferencesInstance(study, temp, 24, [ac, window]).
preferencesInstance(study, noise, 10, [ac, window]).

preferencesInstance(sleep, light, 0, [light_desk, cornerLight, mainLight,roller_shutter]).
preferencesInstance(sleep, temp, 25, [ac, window]).
preferencesInstance(sleep, noise, 10, [ac, window]).

preferencesInstance(turn_off, TypeId, 0, Actuators) :- setof(X, actuator(X,TypeId),Actuators).
preferencesInstance(turn_on, TypeId, 100, Actuators) :- setof(X, actuator(X,TypeId),Actuators).


preferencesInstance(movie, light, 15, [cornerLight,roller_shutter]).
preferencesInstance(movie, light, 3, [light_desk, mainLight]).
preferencesInstance(movie, temp, 25, [ac, window]).
preferencesInstance(movie, noise, 15, [ac, window]).


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