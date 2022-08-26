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
sensor(monitor, light).
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
actuator(monitor, light).
actuator(window, temp).
actuator(roller_shutter, light).



%inside(Id).
:-dynamic(inside/1).
inside(brightness).
inside(temperature).
inside(desk).
inside(monitor).
inside(bed).
inside(chair_desk).
inside(light_desk).
inside(mainLight).
inside(cornerLight).
inside(ac).
inside(monitor).

%outside(Id).
outside(Id) :- 
	\+ inside(Id).

%actuatorValue(ActuatorId, Value).
:-dynamic(actuatorValue/2).
actuatorValue(light_desk, 0).
actuatorValue(mainLight, 0).
actuatorValue(cornerLight, 0).
actuatorValue(ac, 0).
actuatorValue(monitor, 0).
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

preferencesInstance(movie, light, 15, [cornerLight]).
preferencesInstance(movie, light, 0, [light_desk, mainLight]).
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
    sensorValue(brightness_outside, X),
    preferencesInstance(PIId, light, Y, Actuators),
    X >= Y,
	setOutsideActuators(Actuators, Y),
	setInsideActuators(Actuators, 0).
    %replace_existing_fact(actuatorValue(roller_shutter,_), actuatorValue(roller_shutter, Y)),
    %replace_existing_fact(actuatorValue(light_desk,_), actuatorValue(light_desk, 0)),
    %replace_existing_fact(actuatorValue(mainLight,_), actuatorValue(mainLight, 0)),
    %replace_existing_fact(actuatorValue(cornerLight,_), actuatorValue(cornerLight, 0)).

set(PIId, light) :- 
    sensorValue(brightness_outside, X),
    preferencesInstance(PIId, light, Y, Actuators),
    X < Y,
	setOutsideActuators(Actuators, 0),
	setInsideActuators(Actuators, Y).
    %replace_existing_fact(actuatorValue(light_desk,_), actuatorValue(light_desk, Y)),
    %replace_existing_fact(actuatorValue(mainLight,_), actuatorValue(mainLight, Y)),
    %replace_existing_fact(actuatorValue(cornerLight,_), actuatorValue(cornerLight, 0)).

%-----------------------------------------------
    %temperatura dentro < desiderata
        %fuori > desiderata 
            %window = aperta
        %fuori < desiderata 
            %ac = ON
    %temperatura dentro > desiderata
        %fuori > desiderata
            %ac = ON
        %fuori < desiderata 
            %window = aperta

%--------
    %temperatura dentro < desiderata
        %fuori > desiderata 
            %window = aperta
        %fuori < desiderata 
            %ac = ON

set(PIId, temp) :-
    preferencesInstance(PIId, temp, Y, Actuators),
    sensorValue(temperature_outside, X_outside),
    sensorValue(temperature, X_inside),
    X_inside < Y,
    X_outside > Y,
	setOutsideActuators(Actuators, Y),
	setInsideActuators(Actuators, 0).

set(PIId, temp) :-
    preferencesInstance(PIId, temp, Y, Actuators),
    sensorValue(temperature_outside, X_outside),
    sensorValue(temperature, X_inside),
    X_inside < Y,
    X_outside < Y,
	setOutsideActuators(Actuators, 0),
	setInsideActuators(Actuators, Y).
    %replace_existing_fact(actuatorValue(ac,_), actuatorValue(ac, Y)).


    %temperatura dentro > desiderata
        %fuori > desiderata
            %ac = ON
        %fuori < desiderata 
            %window = aperta

set(PIId, temp) :-
    preferencesInstance(PIId, temp, Y, Actuators),
    sensorValue(temperature_outside, X_outside),
    sensorValue(temperature, X_inside),
    X_inside > Y,
    X_outside > Y,
	setOutsideActuators(Actuators, 0),
	setInsideActuators(Actuators, Y).
    %replace_existing_fact(actuatorValue(ac,_), actuatorValue(ac, Y)).


set(PIId, temp) :-
    preferencesInstance(PIId, temp, Y, Actuators),
    sensorValue(temperature_outside, X_outside),
    sensorValue(temperature, X_inside),
    X_inside > Y,
    X_outside < Y,
	setOutsideActuators(Actuators, Y),
	setInsideActuators(Actuators, 0).
    %replace_existing_fact(actuatorValue(window,_), actuatorValue(window, Y)).

set(PIId, noise) :-
    preferencesInstance(PIId, noise, Y_noise, Actuators),
    sensorValue(outside_noise, X_noise_outside),
    X_noise_outside > Y_noise,
    sensorValue(temperature, X_temp_inside),
    preferencesInstance(PIId, temp, Y_temp, Actuators),
    X_temp_inside \== Y_temp,
    setOutsideActuators(Actuators, 0),
    setInsideActuators(Actuators, Y_temp).

%memberCheck(Element, List).
memberCheck(H,[H|_]).
memberCheck(H,[_|T]) :- memberCheck(H,T).


:- use_module(library(qsave)).




	



