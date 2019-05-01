k1 = 0.35;
k2 = 0.01;
k3 = 0.1;
% init state
theta_0 = -0.3;
x_0 = -3;
y_0 = 0.1; 

x_ref = [0 0 0].';
y_th = 0.001;

%%
ST = 1e-3;
sim('vs_paper2002')

%%
figure(1)
plot(x_ref(1),x_ref(2),'x',xc.Data(:,1),xc.Data(:,2),xc.Data(1,1),xc.Data(1,2),'*',xc.Data(end,1),xc.Data(end,2),'o')
legend('Ref','Tracking path','Init Pose','After 5s')
grid on


%%
clf
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
    Cta = xc.Data(index,3);
    quiver(xc.Data(index,1),xc.Data(index,2),v*cos(Cta),v*sin(Cta),'o');
end

grid on

%% 

figure(3)
plot(t,vw.Data)