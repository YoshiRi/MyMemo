%%

close all
clear

%%
% init state
theta_0 = 0.15;
x_0 = -0.06;
y_0 = 0.2; 
f = 610;

h = 0.05;
delta = 0;

obj_points = [1 0.1;1 0;1 -0.1]';
obj_points = [1 0.1;1 0.1;1 -0.1]';

x_ref = [0; 0; 0];

%%
ST = 1e-3;
open('VS_test.slx')
sim('VS_test')


%%
clf

figure(1)
plot(x_ref(1),x_ref(2),'x',xc.Data(:,1),xc.Data(:,2),xc.Data(1,1),xc.Data(1,2),'*',xc.Data(end,1),xc.Data(end,2),'o')
legend('Ref','Tracking path','Init Pose','After 5s','Location','Best')
grid on

%%
figure(2)
plot(x_ref(1),x_ref(2),'x',xc.Data(:,1),xc.Data(:,2))
hold on

t = time.Data;
len = 20;
margin = floor(size(t,1)/len);
vwdata = squeeze(vw.Data).';
for i = 1:len
    index = (i-1)*margin+1;
    v = vwdata(index,1);
    w = vwdata(index,2);
    Cta = xc.Data(index,3);
    quiver(xc.Data(index,1),xc.Data(index,2),v*cos(Cta),v*sin(Cta),'ro');
    quiver(xc.Data(index,1),xc.Data(index,2),-w*sin(Cta),w*cos(Cta),'k')
end

grid on
legend('Goal','Trajectory','v','w','Location','Best')
xlabel('x [m]')
ylabel('y [m]')
title('tracked trajectory')

%%

figure(3)

image_u = squeeze(us.Data).';
image_uref = squeeze(uref.Data).';


plot(t,image_uref,'--',t,image_u)
legend('ref','ref','ref','tracked','tracked','tracked')
xlabel('time [s]')
ylabel('horizontal image coordinate [pix]')
title('horizontal feature')
grid on;

%%

figure(4)

vwinput = squeeze(vw.Data).';
plot(t,vwinput)
legend('v','w','Location','Best')
xlabel('time [s]')
ylabel('reference velocity')
title('input')
grid on;
