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
vwdata = squeeze(vw.Data);
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
title('horizontal feature')
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
plot(image_uref(1,:),image_vref(1,:),'bo',image_u(1,:),image_v(1,:),'rx')
hold on
for i = 1:3
plot(image_u(:,i),image_v(:,i))
end
hold off
grid on
xlabel('horizontal u[pix]')
ylabel('vertical v[pix]')


