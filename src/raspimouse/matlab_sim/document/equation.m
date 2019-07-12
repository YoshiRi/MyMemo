%% calculation

% object position
syms px py pz

% vehicle position
syms vx vy vz theta
% camera orientation
syms cx cy cz phi
syms d f

CS = cos(theta);
SN = sin(theta);

%% projection
% camera pose
cpose =[vx; vy; vz]+[CS SN 0;-SN CS 0; 0 0 1]*[cx ;cy; cz;];
% soutaiteki pose
ctoobj = [px ;py; pz;]-cpose;


%%