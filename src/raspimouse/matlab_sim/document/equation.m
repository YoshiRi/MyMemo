%% calculation
clear 

% object position
syms t
syms px py pz

% vehicle position
syms vx(t) vy(t) vz(t) theta(t)
% camera orientation
syms cx cy cz phi
syms d f

CS = cos(theta(t));
SN = sin(theta(t));

%% projection
cRw = [CS -SN 0;SN CS 0; 0 0 1];
v2c = [0 -1 0;0 0 -1;1 0 0];
% camera pose
cpose =[vx(t); vy(t); vz(t)]+cRw*[cx ;cy; cz;];
% soutaiteki pose
Cobj = simplify(v2c*cRw.'*([px ;py; pz;]-cpose));

imagepoints = simplify(f*[Cobj(1);Cobj(2)]/Cobj(3));

%%
% replace dots
syms vxdot vydot vzdot omega
uvdot = simplify(diff(imagepoints,t));
uvdot_ = subs(uvdot,{diff(vx(t),t),diff(vy(t),t),diff(vz(t),t),diff(theta(t),t)},{vxdot,vydot,vzdot,omega});

% replace u,v,Z
syms Z u v

uvdot_Z = subs(uvdot_,Cobj(3),Z)

%u= subs(imagepoints(1),Cobj(3),Z)
% (f*(cy - py*cos(theta(t)) + px*sin(theta(t)) + cos(theta(t))*vy(t) - sin(theta(t))*vx(t)))
%u=(f*(cos(conj(theta(t)))*(vy(t) - py + cy*cos(theta(t)) + cx*sin(theta(t))) + sin(conj(theta(t)))*(px - vx(t) - cx*cos(theta(t)) + cy*sin(theta(t)))))/Z
%v= subs(imagepoints(2),Cobj(3),Z)
%v=(f*(cz - pz + vz(t)))/Z

%%
uv = {subs(imagepoints(1),Cobj(3),Z),(f*(cz - pz + vz(t)))};
uvdot_uvz = simplify(subs(uvdot_Z,uv,{u,v*Z}))

% uv = {(f*(- py*cos(theta(t)) + px*sin(theta(t)) + cos(theta(t))*vy(t) - sin(theta(t))*vx(t))),(f*(- pz + vz(t)))};
% uvdot_uvz = simplify(subs(uvdot_Z,uv,{u*Z-f*cy,v*Z-f*cz}))

% replace u
eqn = [uvdot_uvz == [0;0]];



%%
vars = [vxdot vydot omega];

A = simplify(equationsToMatrix(eqn,vars));

before={(- py*cos(theta(t)) + px*sin(theta(t)) + cos(theta(t))*vy(t) - sin(theta(t))*vx(t)),px*cos(theta(t))  + py*sin(theta(t)) - cos(theta(t))*vx(t) - sin(theta(t))*vy(t)};
A_ = simplify(subs(A,before,{u*Z/f-cy,Z+cx}))

%A_(6)=v*(Zu/f-cy)/Z ?
%% jimichi
syms h X
J1 = [f/Z -u/Z];
J2 = [-SN CS Z+h;
    -CS -SN -X];

J12 = J1*J2

J3 = [CS 0;SN 0; 0 1];

J123 = simplify(J12*J3)