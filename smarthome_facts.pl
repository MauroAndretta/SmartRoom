
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
preferencesInstance(movie, light, 0, [light_desk, mainLight]).
preferencesInstance(movie, temp, 25, [ac, window]).
preferencesInstance(movie, noise, 15, [ac, window]).