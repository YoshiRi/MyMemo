%% add basic visual feedback function

addpath('../4pointversion')

%% Initialize
% init state
%theta_0 = -0.15; x_0 = -1.0; y_0 = 0.2;
theta_0 = 0; x_0 = -1.0; y_0 = 0.2;
% theta_0 = 0.15; x_0 = -1.0; y_0 = 0.0;
%theta_0 = 0.3; x_0 = 0.0; y_0 = 0.0;

f = 610;
K = [f 0 0;0 f 0; 0 0 1];


h = 0.05;
delta = 0;

%obj_points = [1 0.1 0.2;1 0 0.1;1 -0.1 0.2;1 0 -0.1]';
 obj_points = [1.2 0.1 -0.2;1.2 -0.1 -0.2;1 0.1 -0.2;1 -0.1 -0.2]';
% obj_points = [1.2 0.2 -0.2;1.2 -0.2 -0.2;1.2 0.2 -0.2;1.2 -0.2 -0.2;]';% 2points

x_ref = [0; 0; 0];


%
delta_ref = 0;
delta_0 = 0.1;
%%
ST = 1e-3;
open('withdelta.slx')


%%
theta = -0;
delta_0 = 0;

sim('withdelta')
plotfig4



figure(20)
plot(t,delta.Data,t,xcar.Data(:,3),t,delta.Data+xcar.Data(:,3))
grid on
legend('delta','\theta_{car}','\theta_{camera}')

figure(21)
plot(t,ddelta.Data)