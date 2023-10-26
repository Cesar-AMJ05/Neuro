clear; clc
% Declaración de Patrones y valores objetivo.
%Letra a%
Pa0=[1 1 1 1 1 0 0 0 0 0 1 1 0 1 1 1 1 1 1 1 0 0 1 1 1 1 0 0 1 1 0 1 1 1 1 1];
Pa1=[1 1 1 1 1 0 0 0 0 1 1 1 0 1 1 1 1 1 1 1 0 0 1 1 1 1 0 0 1 1 1 1 1 1 1 1];
Pa2=[0 1 1 1 1 0 0 0 0 0 1 0 0 1 1 1 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1 1 1 1 0];
Pa3=[0 1 1 1 1 0 0 0 0 0 1 1 0 1 1 1 1 1 1 1 0 0 1 1 1 1 0 0 1 1 0 1 1 1 1 0];
Ta=[1 0 0 0 0];
%Letra e%
Pe0=[0 1 1 1 1 0 1 1 0 0 1 1 1 1 1 1 1 1 1 1 0 0 0 0 1 1 0 0 1 1 0 1 1 1 1 0];
Pe1=[0 1 1 1 1 0 1 1 0 0 1 1 1 1 1 1 1 1 1 1 0 0 0 0 1 1 0 0 1 1 1 1 1 1 1 1];
Pe2=[0 1 1 1 1 0 1 1 0 0 1 1 1 1 1 1 1 1 1 0 0 0 0 0 1 1 0 0 1 0 0 1 1 1 1 0];
Pe3=[0 0 1 1 1 1 1 1 0 0 1 1 1 1 1 1 1 1 1 1 0 0 0 0 1 1 0 0 0 1 0 1 1 1 1 0];
Te=[0 1 0 0 0];
%Letra i%
Ti=[0 0 1 0 0];
%Letra o%
To=[0 0 0 1 0];
%Letra u%
Tu=[0 0 0 0 1];

Pgod=[Pa0.',Pa1.',Pa2.', Pa3.'];
T=[Ta.', Te.',Ti.',To.',Tu.'];
% P=[0 0 1 1;
% 0 1 0 1]
% T=[0 0 0 1];
% % Creación de la red Perceptrón.
% net=newp(P,T)
% % Declaración de valores iniciales de entrenamiento.
% net.IW{1,1}=[0 0]
% net.b{1}=0
% Wi=net.IW{1,1}
% Bi= net.b{1}
% % Entrenamiento del Perceptron con los patrones y valores objetivos.
% net=train(net,P,T)
% % Lectura de los parámetros finales de entrenamiento.
% Wf=net.IW{1,1}
% Bf= net.b{1}
% % Simulación del Perceptron entrenado, respuesta a los patrones de entrada.
% a=sim(net,P)
% % Funciones de graficación de Patrones y frontera de decisión.
% plotpv(P,T)
% plotpc(net.IW{1,1}, net.b{1})
% plotpv(P,a)
% plotpv(P,T)
% plotpc(net.IW{1,1},net.b{1})