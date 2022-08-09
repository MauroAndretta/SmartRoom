replace_existing_fact(OldFact, NewFact) :-
    call(OldFact), 
    !,
    retract(OldFact),
    assertz(NewFact).

%propertyType(TypeId).
propertyType(light).
propertyType(temp).
propertyType(position).

%sensor(SensorId, TypeId).
:-dynamic(sensor/2).
sensor(brightness, light).
sensor(brightness_outside, light).
sensor(temperature, temp).
sensor(temperature_outside, temp).
sensor(desk, position).
sensor(monitor, light).
sensor(bed, position).
sensor(chair_desk, position).

%sensorValue(SensorId, Value).
:-dynamic(sensorValue/2).
sensorValue(brightness, 15).
sensorValue(brightness_outside, 15).
sensorValue(temperature, 10).
sensorValue(temperature_outside, 8).

%actuator(ActuatorId, TypeId).
:-dynamic(actuator/2).
actuator(light_desk, light).
actuator(mainLight, light).
actuator(cornerLight, light).
actuator(ac, temp).
actuator(monitor, light).
actuator(window, temp).
actuator(roller_shutter, light).

%actuatorValue(ActuatorId, Value).
:-dynamic(actuatorValue/2).
actuatorValue(light_desk, 0).
actuatorValue(mainLight, 0).
actuatorValue(cornerLight, 0).
actuatorValue(ac, 0).
actuatorValue(monitor, 0).
actuatorValue(window, 0).
actuatorValue(roller_shutter, 0).


%preferncesInstaces(PiiD, TypeId, ExpectedValueSensor, Actuators).
preferncesInstaces(study, light, 20, [light_desk, mainLight, roller_shutter]).
preferncesInstaces(study, temp, 24, [ac, window]).
preferncesInstaces(strunz, temp, 24, [ac, window]).

%set(PIId).
set(study) :-  set(study, light), set(study, temp).

%set(PIId, TypeId).
set(study, light) :- 
    sensorValue(brightness_outside, X),
    preferncesInstaces(study, light, Y, _),
    X >= Y,
    !,
    replace_existing_fact(actuatorValue(roller_shutter,_), actuatorValue(roller_shutter, Y)),
    replace_existing_fact(actuatorValue(light_desk,_), actuatorValue(light_desk, 0)),
    replace_existing_fact(actuatorValue(mainLight,_), actuatorValue(mainLight, 0)),
    replace_existing_fact(actuatorValue(cornerLight,_), actuatorValue(cornerLight, 0)).

set(study, light) :- 
    preferncesInstaces(study, light, Y, _),
    replace_existing_fact(actuatorValue(light_desk,_), actuatorValue(light_desk, Y)),
    replace_existing_fact(actuatorValue(mainLight,_), actuatorValue(mainLight, Y)),
    replace_existing_fact(actuatorValue(cornerLight,_), actuatorValue(cornerLight, 0)).

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

set(study, temp) :-
    preferncesInstaces(study, temp, Y, _),
    sensorValue(temperature_outside, X_outside),
    sensorValue(temperature, X_inside),
    X_inside < Y,
    X_outside > Y,
    replace_existing_fact(actuatorValue(window,_), actuatorValue(window, Y)).

set(study, temp) :-
    preferncesInstaces(study, temp, Y, _),
    sensorValue(temperature_outside, X_outside),
    sensorValue(temperature, X_inside),
    X_inside < Y,
    X_outside < Y,
    replace_existing_fact(actuatorValue(ac,_), actuatorValue(ac, Y)).


    %temperatura dentro > desiderata
        %fuori > desiderata
            %ac = ON
        %fuori < desiderata 
            %window = aperta

set(study, temp) :-
    preferncesInstaces(study, temp, Y, _),
    sensorValue(temperature_outside, X_outside),
    sensorValue(temperature, X_inside),
    X_inside > Y,
    X_outside > Y,
    replace_existing_fact(actuatorValue(ac,_), actuatorValue(ac, Y)).


set(study, temp) :-
    preferncesInstaces(study, temp, Y, _),
    sensorValue(temperature_outside, X_outside),
    sensorValue(temperature, X_inside),
    X_inside > Y,
    X_outside < Y,
    replace_existing_fact(actuatorValue(window,_), actuatorValue(window, Y)).







	



