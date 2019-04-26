%%
%clf

figure(1)
plot(x_ref(1),x_ref(2),'x',xcar.Data(:,1),xcar.Data(:,2),xcar.Data(1,1),xcar.Data(1,2),'*',xcar.Data(end,1),xcar.Data(end,2),'o')
Cta = xcar.Data(end,3);
hold on
plot(obj_points(1,:),obj_points(2,:),'s')
quiver(xcar.Data(end,1),xcar.Data(end,2),cos(Cta),sin(Cta),'r');
legend('Ref','Tracking path','Init Pose','Final Pose','Objects','Location','Best')
grid on
hold off

fig=figure(10)
fig.Position = [1,1,1000,280]
plot(x_ref(1),x_ref(2),'o',xcar.Data(:,1),xcar.Data(:,2),'-',xcar.Data(1,1),xcar.Data(1,2),'+',xcar.Data(end,1),xcar.Data(end,2),'x')
Cta = xcar.Data(end,3);
hold on
plot(obj_points(1,:),obj_points(2,:),'s')
% quiver(xcar.Data(end,1),xcar.Data(end,2),cos(Cta),sin(Cta),'r');
plot_baseballbase(x_ref(1),x_ref(2),x_ref(3),0.1);
plot_baseballbase(xcar.Data(end,1),xcar.Data(end,2),Cta,0.1);
plot_baseballbase(xcar.Data(1,1),xcar.Data(1,2),xcar.Data(1,3),0.1);

legend('Goal','Tracking path','Init Pose','Final Pose','Objects','Location','Best')
xlabel('x [m]')
ylabel('y [m]')
grid on
hold off


%%
figure(2)
plot(x_ref(1),x_ref(2),'x',xcar.Data(:,1),xcar.Data(:,2))
hold on

t = time.Data;
len = 20;
margin = floor(size(t,1)/len);
vwdata = squeeze(vw.Data);
for i = 1:len
    index = (i-1)*margin+1;
    v = vwdata(index,1);
    w = vwdata(index,2);
    Cta = xcar.Data(index,3);
    quiver(xcar.Data(index,1),xcar.Data(index,2),v*cos(Cta),v*sin(Cta),'ro');
    quiver(xcar.Data(index,1),xcar.Data(index,2),-w*sin(Cta),w*cos(Cta),'k')
end
hold off
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
legend('u1_{ref}','u2_{ref}','u3_{ref}','u1_{tracked}','u2_{tracked}','u3_{tracked}','Location','Best')
xlabel('time [s]')
ylabel('horizontal image coordinate [pix]')
title('horizontal feature')
grid on;



%%

figure(4)

image_v = squeeze(vs.Data).';
image_vref = squeeze(vref.Data).';


plot(t,image_vref,'--',t,image_v)
legend('v1_{ref}','v2_{ref}','v3_{ref}','v1_{tracked}','v2_{tracked}','v3_{tracked}','Location','Best')
xlabel('time [s]')
ylabel('Vertical image coordinate [pix]')
title('vertical feature')
grid on;

%%

figure(5)

vwinput = squeeze(vw.Data).';
plot(t,vwinput)
legend('v','w','Location','Best')
xlabel('time [s]')
ylabel('reference velocity')
title('input')
grid on;


%% image view

figure(6)
plot(image_uref(1,:),image_vref(1,:),'bo',image_u(1,:),image_v(1,:),'r+',image_u(end,:),image_v(end,:),'mx')
hold on
for i = 1:4
plot(image_u(:,i),image_v(:,i),'-.')
end
hold off
grid on
xlabel('horizontal u[pix]')
ylabel('vertical v[pix]')
legend('reference','start','Final Pose','trajectory')
title('Image Plane')
%% depth view
figure(7)

depth = squeeze(ds.Data).';
d_ref = squeeze(dref.Data).';

plot(t,d_ref,'--',t,depth);
title('depth plot')