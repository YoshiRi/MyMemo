%%%
% Input: (x,y,theta) of point and baseballbase size
% Output: handle of plot
%%% 

function  handle = plot_baseballbase(x,y,theta,hsize)
d = hsize/2;
pts = [d 2*d d -d -d d;d 0 -d -d d d];
R = [cos(theta) -sin(theta); sin(theta) cos(theta)];
rpts = R*pts;

handle = plot(x+rpts(1,:),y+rpts(2,:),'k')
end