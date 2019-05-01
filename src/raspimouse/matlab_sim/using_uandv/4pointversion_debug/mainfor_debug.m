
addpath('../4pointversion')

%%
% init state
%theta_0 = -0.15; x_0 = -1.0; y_0 = 0.2;
theta_0 = 0; x_0 = -1.0; y_0 = 0.2;
theta_0 = 0.15; x_0 = -1.0; y_0 = 0.0;
%theta_0 = 0.3; x_0 = 0.0; y_0 = 0.0;


f = 610;
K = [f 0 0;0 f 0; 0 0 1];


h = 0.05;
delta = 0;

obj_points = [1 0.1 0.2;1 0 0.1;1 -0.1 0.2;1 0 -0.1]';
obj_points = [1.2 0.1 -0.2;1.2 -0.1 -0.2;1 0.1 -0.2;1 -0.1 -0.2]';

x_ref = [0; 0; 0];


%
delta_ref = 0;
delta_0 = 0.1;
%%
ST = 1e-3;
open('VS_uandv_4pointver_debug.slx')


%%
sim('VS_uandv_4pointver_debug.slx')
plotfig4

