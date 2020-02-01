%%

close all
clear

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

%%

%%



ST = 1e-3;
open('VS_uandv_4pointver.slx')


%% plot
%plotfig4

sim('VS_uandv_4pointver');
plotfig4

%% get final jacob
fjacob = Jacob.Data(:,:,end);


%%

ucontrol.vw=vwinput;
ucontrol.u = image_u;
ucontrol.u_ref = image_uref;
ucontrol.v = image_v;
ucontrol.v_ref = image_vref;
ucontrol.xcar = xcar.Data;
ucontrol.t = t;
